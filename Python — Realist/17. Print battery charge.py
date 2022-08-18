def battery_charge(n):
    bar_count = round(n / 10)
    print("[" + "❚" * bar_count + " " * (10 - bar_count) + "]")
    print(f"{n}%")
