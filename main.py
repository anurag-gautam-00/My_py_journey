import time as t

name = input("What's your name ? ")
hour = int(t.strftime("%H"))

if 0 < hour < 12:
    print(f"Good morning {name}")

elif 12 <= hour < 16:
    print(f"Good afternoon {name}")

else:
    print(f"Good evening {name}")