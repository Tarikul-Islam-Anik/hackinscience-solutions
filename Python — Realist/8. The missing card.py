def missing_card(cards):
    color = ["S", "H", "D", "C"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    total_cards = []
    for i in color:
        for j in values:
            total_cards.append(i + j)
    return str(set(total_cards) - set(cards.split()))[2:-2]
