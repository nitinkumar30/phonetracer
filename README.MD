 __        __        ___ ___  __        __   ___  __  
|__) |__| /  \ |\ | |__   |  |__)  /\  /  ` |__  |__) 
|    |  | \__/ | \| |___  |  |  \ /~~\ \__, |___ |  \ 


# PhoneTracer ⚡️  
**OSINT Phone Number Metadata Toolkit**

[![License](https://img.shields.io/github/license/nitinkumar30/phonetracer)](LICENSE)
[![Github Actions](https://github.com/nitinkumar30/phonetracer/actions/workflows/python-ci.yml/badge.svg)](https://github.com/nitinkumar30/phonetracer/actions)

PhoneTracer is a **modular Python OSINT toolkit** that extracts **public, non-invasive metadata**
from phone numbers using Google’s `libphonenumber` (via `phonenumbers`).

> ❗ PhoneTracer **does NOT track phones**, reveal owners, intercept calls, or provide live locations.

---

## ✨ Features

- 📞 Phone number parsing & validation
- 🌍 Country / region identification
- 🏷 Carrier lookup (when available)
- 🕒 Timezone detection
- 🧠 Spam-style heuristic scoring
- 📄 Scan numbers from text files
- 📊 Automatic JSON export on every run
- 🖥 Argument-based CLI
- 📟 Interactive command-line menu
- 🪟 Desktop GUI (Tkinter)
- 🧪 Built-in sanity tests
- 🤖 GitHub Actions CI

---

## 📦 Installation

```bash
pip install phonetrcer
````

Dependencies are minimal:

* Python **3.7+**
* `phonenumbers`

---

## 🚀 Quick Start

### Launch mode selector

```bash
python main.py
```

You can choose:

```
1. Argument mode
2. Command-line menu
3. GUI
```

---

## 🖥 Usage Modes

### 🔹 Argument Mode (automation-friendly)

```bash
python cli_args.py -n "+1 415 555 2671"
python cli_args.py -f numbers.txt
```

✔ Machine-readable
✔ Always auto-saved

---

### 🔹 Interactive CLI Menu

```bash
python cli_menu.py
```

✔ Human-readable
✔ Auto-saved after each run

---

### 🔹 GUI Mode

```bash
python gui_app.py
```

✔ Desktop UI
✔ Clean formatted output
✔ Auto-save enabled

---

## 📂 Output Files

Every run automatically generates a JSON file:

```
YYYYMMDD_HHMMSS_<mode>.json
```

Example:

```json
{
  "raw_input": "+91 9513717169",
  "valid": true,
  "possible": true,
  "international": "+91 95137 17169",
  "e164": "+919513717169",
  "country": "India",
  "carrier": "Airtel",
  "timezones": ["Asia/Kolkata"],
  "spam_score": 1
}
```

---

## 🧠 Spam Heuristics (Non-AI)

PhoneTracer uses **transparent, rule-based heuristics**, such as:

* Repeated digits
* Excessive zeros
* Abnormal formatting

> ⚠ This is **not a spam classifier**, only a signal.

---

## 🧱 Project Architecture

```
phonetrcer/
│
├── main.py        # Mode selector
├── core.py        # Shared logic (analysis, export, logging)
├── cli_args.py    # Argument-based CLI
├── cli_menu.py    # Interactive CLI
├── gui_app.py     # Tkinter GUI
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## 🤖 Continuous Integration

GitHub Actions automatically:

* Installs dependencies
* Validates imports
* Runs core sanity tests

Workflow:

```
.github/workflows/python-ci.yml
```

---

## 🔐 Privacy & Ethics

PhoneTracer strictly follows ethical OSINT principles:

* ❌ No phone tracking
* ❌ No subscriber identification
* ❌ No surveillance or interception
* ❌ No bypass of telecom systems
* ✅ Public metadata only

This makes the library **safe for PyPI distribution**.

---

## 🧪 Testing

Built-in sanity tests:

```bash
python cli_args.py --test
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Please keep changes **ethical, documented, and tested**.

---

## 📜 License

MIT License © Your Name

---

## ⭐ Support

If you find PhoneTracer useful:

* ⭐ Star the repository
* 🐞 Report issues
* 💡 Suggest features

---

### Built with ❤️ for ethical OSINT & Python automation





