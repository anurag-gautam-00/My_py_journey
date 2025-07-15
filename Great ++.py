def great():
    import time as t

    name = input("What's your name? ").strip()
    hour = int(t.strftime("%H"))

    if hour < 12:
        print(f"Good morning {name}")
    elif hour == 12:
        print(f"Good afternoon {name}")
    else:
        print(f"Good evening {name}")
