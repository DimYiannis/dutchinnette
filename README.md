# 🌱 Dutchinnette

**Dutchinnette** is an automated testing tool for Codam's Python curriculum, inspired by [Francinette](https://github.com/xicodomingues/francinette) for 42.

## 🚀 Installation

### From source (recommended for development)

```bash
git clone https://github.com/yourusername/dutchinnette.git
cd dutchinnette
pip install -e .
```

### Using pip (once published)

```bash
pip install dutchinnette
```

## 📖 Usage

Navigate to your module directory and run:

```bash
codam
```

The tool will automatically detect which module you're working on and run the appropriate tests.

### Manual module selection

```bash
codam module00
codam module01
```

## 📁 Project Structure

```
dutchinnette/
├── dutchinnette/
│   ├── __init__.py
│   ├── codam.py          # Main testing logic
│   └── modules.py        # Test definitions
├── setup.py
├── README.md
└── requirements.txt
```

## 🎯 Supported Modules

- ✅ **Module00** - Basic Python fundamentals
  - ex0: ft_hello_garden
  - ex1: ft_plot_area
  - ex2: ft_harvest_total
  - ex3: ft_plant_age
  - ex4: ft_water_reminder
  - ex5: ft_simple_calculator
  - ex6: ft_grade_checker
  - ex7: ft_count_to_ten

- ✅ **Module01** - Object-Oriented Programming (OOP)
  - ex0: ft_garden_intro (Program structure, `if __name__ == "__main__"`)
  - ex1: ft_garden_data (Classes and `__init__`)
  - ex2: ft_plant_growth (Instance methods)
  - ex3: ft_plant_factory (Multiple instances)
  - ex4: ft_garden_security (Encapsulation, getters/setters)
  - ex5: ft_plant_types (Inheritance with `super()`)
  - ex6: ft_garden_analytics (Advanced OOP: nested classes, static/class methods)

## 🧪 Example Output

```
🌱 Dutchinnette - Codam Python Tester 🌱

============================================================
Testing MODULE01
============================================================

  ✓ ex0      ex0/ft_garden_intro.py              OK
  ✓ ex1      ex1/ft_garden_data.py               OK
  ✗ ex2      ex2/ft_plant_growth.py              KO (6/8 checks passed)
      Missing: 'Growth this week: +6cm'
  ✓ ex3      ex3/ft_plant_factory.py             OK
  ⊘ ex5      ex5/ft_plant_types.py               SKIPPED (file not found)

------------------------------------------------------------
Result: 35/43 tests passed (81.4%)
Status: SOME TESTS FAILED ✖
============================================================
```

### Understanding Output
- ✓ **Green checkmark**: All checks passed
- ✗ **Red X**: Some/all checks failed (shows which strings are missing)
- ⊘ **Yellow circle**: File not found (skipped)

For detailed testing guide, see [MODULE01_TESTING_GUIDE.md](MODULE01_TESTING_GUIDE.md).

## 🛠️ Adding New Tests

To add tests for a new exercise, edit `dutchinnette/modules.py`:

```python
MODULE00 = {
    "ex8": {
        "file": "ex8/ft_my_function.py",
        "func": "ft_my_function",  # or None for script execution
        "cases": [
            (["input1", "input2"], "expected output"),
        ],
    },
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by [Francinette](https://github.com/xicodomingues/francinette) by xicodomingues
- Built for the Codam Coding College community

## 📧 Contact

If you have any questions or suggestions, feel free to open an issue!

---

Made with ❤️ for the Codam community