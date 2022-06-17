def love_meet(bob, alice):
    return set(sorted(set(alice) & set(bob)))


def affair_meet(bob, alice, silvester):
    return set([i for i in alice if i not in bob]) & set(silvester)