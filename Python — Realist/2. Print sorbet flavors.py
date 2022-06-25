FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

print(
    "\n".join(
        ["%s, %s" % (i, j) for i in FLAVORS for j in FLAVORS if (i != j and i > j)]
    )
)
