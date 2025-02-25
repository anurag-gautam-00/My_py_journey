def great(fx):
    import time as t

    name = input("What's your name ? ")
    current = t.strftime
    if current("%H") < "12":
        print(f"Good morning {name}")
    elif current("%H") == "12":
        print(f"Good afrnoon {name}")

    else:
        print(f"Good evening {name}")
