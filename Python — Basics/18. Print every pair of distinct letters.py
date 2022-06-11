print(
    "\n".join(
        [
            "%s%s" % (i, j)
            for i in __import__("string").ascii_lowercase
            for j in __import__("string").ascii_lowercase
            if i != j
        ]
    )
)
