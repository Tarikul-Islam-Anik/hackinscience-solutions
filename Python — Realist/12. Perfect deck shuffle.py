def perfect_shuffle(deck):
    if len(deck) == 0:
        return deck
    else:
        half = len(deck) // 2
        return [i for j in zip(deck[:half], deck[half:]) for i in j]
