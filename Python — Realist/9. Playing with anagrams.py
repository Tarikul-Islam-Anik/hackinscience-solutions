import unicodedata


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def special_char_remover(s):
    return "".join(c for c in s if c.isalnum())


def is_anagram(left, right):
    left = left.lower()
    right = right.lower()
    left = strip_accents(left)
    right = strip_accents(right)
    left = special_char_remover(left)
    right = special_char_remover(right)
    left = "".join(sorted(left))
    right = "".join(sorted(right))
    return left == right
