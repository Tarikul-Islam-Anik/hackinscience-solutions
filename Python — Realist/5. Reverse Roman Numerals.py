def from_roman_numeral(roman_numeral):
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_num[roman_numeral[i]] > roman_num[roman_numeral[i - 1]]:
            total += roman_num[roman_numeral[i]] - 2 * roman_num[roman_numeral[i - 1]]
        else:
            total += roman_num[roman_numeral[i]]
    return total
