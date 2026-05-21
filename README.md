# 🐱 Hello World ASCII Cat

A simple Python project that displays a cute ASCII cat with colorful terminal effects and typing animation.

## ✨ Preview

```text
╔══════════════════════════════════════════╗
║             ✨ HELLO WORLD ✨             ║
╚══════════════════════════════════════════╝

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀／＞　 フ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| 　_　_|
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀／` ミ＿xノ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ /　　　 　 |
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ /　 ヽ　　 ﾉ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀│　　|　|　|
⠀⠀⠀⠀⠀⠀⠀⠀／￣|　　 |　|　|
⠀⠀⠀⠀⠀⠀⠀| (￣ヽ＿_ヽ_)__)
⠀⠀⠀⠀⠀⠀⠀＼二つ

🐾 Hello World
🐱 Cute ASCII Cat Loaded!
```

---

## 🚀 Features

- Cute ASCII Cat
- Colored Terminal Output
- Typing Animation Effect
- Lightweight Python Script
- Easy to Customize

---

## 📦 Installation

Install the required package:

```bash
pip install colorama
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🧠 Source Code

```python
import time
from colorama import Fore, Style, init

init(autoreset=True)

cat = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀／＞　 フ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀| 　_　_|
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀／` ミ＿xノ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ /　　　 　 |
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ /　 ヽ　　 ﾉ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀│　　|　|　|
⠀⠀⠀⠀⠀⠀⠀⠀／￣|　　 |　|　|
⠀⠀⠀⠀⠀⠀⠀| (￣ヽ＿_ヽ_)__)
⠀⠀⠀⠀⠀⠀⠀＼二つ
'''

title = "✨ HELLO WORLD ✨"

def typing(text, speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

print(Fore.CYAN + "╔" + "═" * 42 + "╗")
print(Fore.CYAN + f"║{title.center(42)}║")
print(Fore.CYAN + "╚" + "═" * 42 + "╝")

print()

print(Fore.YELLOW + cat)

typing(Fore.GREEN + "🐾 Hello World")
typing(Fore.MAGENTA + "🐱 Cute ASCII Cat Loaded!")
```

---

## 📄 License

MIT License

---

## ❤️ Author

Made with Python and ASCII Art