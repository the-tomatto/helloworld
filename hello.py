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

# กรอบด้านบน
print(Fore.CYAN + "╔" + "═" * 42 + "╗")
print(Fore.CYAN + f"║{title.center(42)}║")
print(Fore.CYAN + "╚" + "═" * 42 + "╝")

print()

# แสดงแมว
print(Fore.YELLOW + cat)

# ข้อความแบบพิมพ์ทีละตัว
typing(Fore.GREEN + "🐾 Hello World")
typing(Fore.MAGENTA + "🐱 Cute ASCII Cat Loaded!")
