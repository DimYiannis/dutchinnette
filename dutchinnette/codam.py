#!/usr/bin/env python3
"""
Dutchinnette - Codam Python Module Tester
Automated testing tool for Codam's Python curriculum
"""
import os
import io
import sys
import builtins
import contextlib
import importlib.util
import subprocess
from pathlib import Path

# ===================== COLORS =====================
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def ok():
    return f"{GREEN}OK{RESET}"

def ko():
    return f"{RED}KO{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"

# ===================== HELPERS =====================
def capture_output(func, inputs=None, func_args=None):
    """Capture stdout from a function call with optional inputs and function arguments"""
    inputs = inputs or []
    func_args = func_args or []
    input_iter = iter(inputs)
    
    def fake_input(prompt=""):
        try:
            return next(input_iter)
        except StopIteration:
            raise StopIteration("Not enough inputs provided")
    
    old_input = builtins.input
    builtins.input = fake_input
    buf = io.StringIO()
    
    with contextlib.redirect_stdout(buf):
        try:
            if func_args:
                func(*func_args)
            else:
                func()
        except StopIteration:
            pass
        except Exception as e:
            builtins.input = old_input
            raise e
    
    builtins.input = old_input
    return buf.getvalue().strip()

def import_function_from_path(path, func_name):
    """Import a specific function from a file path"""
    if not path or not os.path.exists(path):
        return None
    
    try:
        # Clear any cached version of this module
        module_name = f"temp_module_{func_name}_{os.getpid()}"
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        
        # Don't add to sys.modules to avoid caching issues
        spec.loader.exec_module(module)
        return getattr(module, func_name, None)
    except Exception:
        return None

def run_script(path, timeout=5):
    """Run a Python script and capture its output"""
    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", -1
    except Exception:
        return "", -1

# ===================== TEST RUNNER =====================
def run_test_case(file_path, func_name, inputs, expected):
    """Run a single test case"""
    filename = os.path.basename(file_path)
    
    # If func_name is None, run as script
    if func_name is None:
        output, returncode = run_script(file_path)
        if returncode != 0 and returncode != -1:
            return False, f"Script exited with code {returncode}"
    else:
        # Import and call function
        func = import_function_from_path(file_path, func_name)
        if not func:
            return False, "Function not found or import failed"
        
        try:
            # Check if inputs are actually function arguments (not input() responses)
            # For ex7, inputs will be like ["tomato", "15", "packets"]
            if inputs and all(not isinstance(i, str) or i not in ["", " "] for i in inputs):
                # Try calling with arguments first (for functions like ft_seed_inventory)
                try:
                    output = capture_output(func, func_args=inputs)
                except TypeError:
                    # If that fails, treat as input() responses
                    output = capture_output(func, inputs=inputs)
            else:
                output = capture_output(func, inputs=inputs)
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    # Check if expected string is in output
    if expected in output:
        return True, output
    else:
        return False, output

def run_exercise(ex_name, ex_data, base_path):
    """Run all test cases for one exercise"""
    file_path = base_path / ex_data["file"]
    
    if not file_path.exists():
        print(f"  {YELLOW}⊘{RESET} {ex_name:<8} {ex_data['file']:<35} SKIPPED (file not found)")
        return 0, 0
    
    func_name = ex_data.get("func")
    cases = ex_data.get("cases", [])
    
    # For script execution (func=None), run once and check all expected strings
    if func_name is None:
        output, returncode = run_script(file_path)
        
        if returncode != 0 and returncode != -1:
            print(f"  {RED}✗{RESET} {ex_name:<8} {ex_data['file']:<35} {ko()} (exit code: {returncode})")
            return 0, len(cases)
        
        passed = 0
        failed_checks = []
        for inputs, expected in cases:
            if expected in output:
                passed += 1
            else:
                failed_checks.append(expected)
        
        total = len(cases)
        if passed == total:
            print(f"  {GREEN}✓{RESET} {ex_name:<8} {ex_data['file']:<35} {ok()}")
        else:
            print(f"  {RED}✗{RESET} {ex_name:<8} {ex_data['file']:<35} {ko()} ({passed}/{total} checks passed)")
            for missing in failed_checks[:3]:  # Show max 3 missing items
                print(f"      {YELLOW}Missing:{RESET} '{missing}'")
        
        return passed, total
    
    # For function calls, test each case separately
    passed = 0
    total = len(cases)
    all_success = True
    first_failure = None
    
    for i, (inputs, expected) in enumerate(cases):
        success, output = run_test_case(file_path, func_name, inputs, expected)
        
        if success:
            passed += 1
        else:
            all_success = False
            if first_failure is None:
                first_failure = (expected, output)
    
    if all_success:
        print(f"  {GREEN}✓{RESET} {ex_name:<8} {ex_data['file']:<35} {ok()}")
    else:
        print(f"  {RED}✗{RESET} {ex_name:<8} {ex_data['file']:<35} {ko()} ({passed}/{total} tests passed)")
        if first_failure:
            print(f"      {YELLOW}Expected:{RESET} '{first_failure[0]}'")
            print(f"      {YELLOW}Got:{RESET}      '{first_failure[1]}'")
    
    return passed, total

def clean_pycache(base_path):
    """Remove all __pycache__ directories"""
    import shutil
    for root, dirs, files in os.walk(base_path):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
            except Exception:
                pass

def run_module(module_name, tests, base_path=None):
    """Run all exercises for a module"""
    if base_path is None:
        base_path = Path.cwd()
    else:
        base_path = Path(base_path)
    
    # Clean pycache before testing
    clean_pycache(base_path)
    
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Testing {module_name.upper()}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    total_passed = 0
    total_tests = 0
    
    for ex_name in sorted(tests.keys()):
        ex_data = tests[ex_name]
        passed, total = run_exercise(ex_name, ex_data, base_path)
        total_passed += passed
        total_tests += total
    
    # Summary
    print(f"\n{BLUE}{'-'*60}{RESET}")
    percentage = (total_passed / total_tests * 100) if total_tests > 0 else 0
    print(f"Result: {total_passed}/{total_tests} tests passed ({percentage:.1f}%)")
    
    if total_passed == total_tests:
        print(f"Status: {GREEN}ALL TESTS PASSED ✔{RESET}")
    else:
        print(f"Status: {RED}SOME TESTS FAILED ✖{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    return total_passed == total_tests

# ===================== MODULE DETECTION =====================
def detect_module():
    """Detect which module is in the current directory"""
    cwd = Path.cwd()
    
    # Try to import module tests
    try:
        from dutchinnette.modules import MODULE00, MODULE01
        
        # Check for module01 first (has if __name__ == "__main__" structure)
        if (cwd / "ex0" / "ft_garden_intro.py").exists():
            return "module01", MODULE01
        
        # Check for module00 (has simple function files)
        if (cwd / "ex0" / "ft_hello_garden.py").exists():
            return "module00", MODULE00
        
    except ImportError:
        print(f"{RED}Error: Could not import module definitions{RESET}")
        print(f"{YELLOW}Make sure dutchinnette is properly installed{RESET}")
        return None, None
    
    return None, None

# ===================== MAIN =====================
def main():
    """Main entry point"""
    print(f"\n{BLUE}🌱 Dutchinnette - Codam Python Tester 🌱{RESET}")
    
    # Check if specific module is requested
    if len(sys.argv) > 1:
        module_name = sys.argv[1].lower()
        try:
            if module_name == "module00":
                from dutchinnette.modules import MODULE00
                run_module("module00", MODULE00)
            elif module_name == "module01":
                from dutchinnette.modules import MODULE01
                run_module("module01", MODULE01)
            else:
                print(f"{RED}Unknown module: {module_name}{RESET}")
                print(f"{YELLOW}Available modules: module00, module01{RESET}")
        except ImportError as e:
            print(f"{RED}Error importing module: {e}{RESET}")
        return
    
    # Auto-detect module
    module_name, tests = detect_module()
    
    if module_name and tests:
        run_module(module_name, tests)
    else:
        print(f"\n{RED}No supported module detected in this directory{RESET}")
        print(f"\n{YELLOW}Usage:{RESET}")
        print(f"  codam                 - Auto-detect and test current module")
        print(f"  codam module00        - Test module00")
        print(f"  codam module01        - Test module01")
        print(f"\n{YELLOW}Supported modules:{RESET}")
        print(f"  - module00 (ft_hello_garden.py)")
        print(f"  - module01 (ft_garden_intro.py)")

if __name__ == "__main__":
    main()