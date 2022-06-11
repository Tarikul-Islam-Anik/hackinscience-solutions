try:
    print(__import__("requests").get(
        "https://api.github.com/users/python").json())
except:
    print("No internet connectivity.")
