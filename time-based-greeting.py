import time as t

def great():
    name = input("What's your name? ").strip()
    hour = int(t.strftime("%H"))

    if hour < 12:
        print(f"Good morning {name}")
    elif hour == 12:
        print(f"Good afternoon {name}")
    else:
        print(f"Good evening {name}")

if __name__ == '__main__':
    great()-
