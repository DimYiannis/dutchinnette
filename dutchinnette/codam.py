import os
import io
import sys
import builtins
import contextlib
import importlib.util

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def capture_output(func, inputs=None):
    inputs = inputs or []
    input_iter = iter(inputs)
    def fake_input(prompt=""):
        return next(input_iter)
    old_input = builtins.input
    builtins.input = fake_input
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        try:
            func()
        except StopIteration:
            print(f"{YELLOW}Not enough input provided!{RESET}")
    builtins.input = old_input
    return f.getvalue().strip()

def import_function_from_path(path, func_name):
    spec = importlib.util.spec_from_file_location(func_name, path)
    if spec is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, func_name, None)

def run_module00_tests():
    TESTS = {
        "ex0/ft_hello_garden.py": [([], "Hello, Garden Community!")],
        "ex1/ft_plot_area.py": [(["5","3"], "Plot area: 15")],
        "ex2/ft_harvest_total.py": [(["5","8","3"], "Total harvest: 16")],
        "ex3/ft_plant_age.py": [(["75"], "Plant is ready to harvest!"),
                                (["45"], "Plant needs more time to grow.")],
        "ex4/ft_water_reminder.py": [(["4"], "Water the plants!"),
                                     (["1"], "Plants are fine")],
    }

    cwd = os.getcwd()
    print(f"{YELLOW}=== Checking module00 in {cwd} ==={RESET}")

    total, passed = 0, 0
    for file_rel_path, cases in TESTS.items():
        file_path = os.path.join(cwd, file_rel_path)
        func_name = os.path.splitext(os.path.basename(file_path))[0]
        func = import_function_from_path(file_path, func_name)
        if not func:
            print(f"{RED}Missing {func_name} ({file_rel_path}){RESET}")
            continue
        for inputs, expected in cases:
            total += 1
            output = capture_output(func, inputs)
            if output == expected:
                passed += 1
                print(f"{GREEN}{func_name:<20} Inputs: {str(inputs):<25} -> PASS{RESET}")
            else:
                print(f"{RED}{func_name:<20} Inputs: {str(inputs):<25} -> FAIL (got '{output}'){RESET}")


    print(f"{YELLOW}=== Finished module00: {passed}/{total} tests passed ==={RESET}")

def main():
    run_module00_tests()

if __name__ == "__main__":
    main()
