# Codam Checker - Module00

This is a local Python checker for **module00 exercises** at Codam/42.  
It mimics the functionality of Francinette, allowing you to run automated tests for your exercises offline.

## Folder Structure

```
/codam_checker/
│
├── codam.py                # CLI script (main checker)
├── modules/
│   └── module00_tests.py   # Test cases for module00 exercises
└── README.md               # This file
```

Your exercise folders (`ex0`, `ex1`, `ex2`, etc.) should be at the **same level** as `codam.py`.

---

## Usage

### Run the checker for module00 (default)

```bash
python3 codam.py
```

### Run the checker with a custom alias (optional)

Add an alias in your shell (`~/.zshrc` or `~/.bashrc`):

```bash
echo 'alias codam="python3 /path/to/codam_checker/codam.py"' >> ~/.zshrc
source ~/.zshrc
```

Now you can run:

```bash
codam
```

### Run the checker for multiple modules

```bash
codam module00 module01
```

> Only module00 is included for now. You can add more modules later in the `modules/` folder.

---

## How it works

1. The script imports your exercise functions dynamically.  
2. Simulates inputs for each function.  
3. Captures printed output.  
4. Compares the output to expected results.  
5. Prints **PASS / FAIL** for each exercise.

---

## Extending for new modules

1. Create a new test file in `modules/` named `moduleXX_tests.py`.  
2. Define a `TESTS` dictionary in the same format as `module00_tests.py`.  
3. Run `codam moduleXX` to test the new module.

---

## Requirements

- Python 3.10+
- Exercise folders (`ex0`, `ex1`, etc.) with functions as specified in Codam’s instructions.

---

## Notes

- The checker is **fully offline**.  
- Designed to be modular and scalable for future modules.  
- Only prints **PASS/FAIL** messages, no changes to your code.
