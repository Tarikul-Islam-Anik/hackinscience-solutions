from random import *


def pwgen(length, with_digits=True, with_uppercase=True):

    passwd = []
    alpha_lower = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    alpha_upper = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    alpha = alpha_lower + alpha_upper
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphanum_lower = alpha_lower + num
    alphanum_upper = alpha_upper + num
    alphanum = alpha + num

    for i in range(0, length - 2):
        if with_digits == False and with_uppercase == False:
            passwd.append(choice(alpha_lower))
        elif with_digits == False:
            passwd.append(choice(alpha))
        elif with_uppercase == False:
            passwd.append(choice(alphanum_lower))
        else:
            passwd.append(choice(alphanum))

    if with_digits == True and with_uppercase == False:
        num_digit = 0
        for p in passwd:
            if p.isdigit():
                num_digit += 1
        if num_digit == 0:
            passwd.append(choice(num))
            passwd.append(choice(alphanum_lower))
        else:
            passwd.append(choice(alphanum_lower))
            passwd.append(choice(alphanum_lower))

    elif with_digits == False and with_uppercase == True:
        num_upper = 0
        for p in passwd:
            if p.isupper():
                num_upper += 1
        if num_upper == 0:
            passwd.append(choice(alpha_upper))
            passwd.append(choice(alpha))
        else:
            passwd.append(choice(alpha))
            num_lower = 0
            for p in passwd:
                if p.islower():
                    num_lower += 1
            if num_lower == 0:
                passwd.append(choice(alpha_lower))
            else:
                passwd.append(choice(alpha))

    elif with_digits == True and with_uppercase == True:
        num_digit = 0
        for p in passwd:
            if p.isdigit():
                num_digit += 1
        num_upper = 0
        for p in passwd:
            if p.isupper():
                num_upper += 1
        if num_digit == 0 and num_upper == 0:
            passwd.append(choice(num))
            passwd.append(choice(alpha_upper))
        elif num_digit == 0 and num_upper > 0:
            passwd.append(choice(num))
            num_lower = 0
            for p in passwd:
                if p.islower():
                    num_lower += 1
            if num_lower == 0:
                passwd.append(choice(alpha_lower))
            else:
                passwd.append(choice(alphanum))
        elif num_digit > 0 and num_upper == 0:
            passwd.append(choice(alpha_upper))
            passwd.append(choice(alphanum))
        else:
            passwd.append(choice(alphanum))
            num_lower = 0
            for p in passwd:
                if p.islower():
                    num_lower += 1
            if num_lower == 0:
                passwd.append(choice(alpha_lower))
            else:
                passwd.append(choice(alphanum))
    else:
        passwd.append(choice(alpha_lower))
        passwd.append(choice(alpha_lower))

    shuffle(passwd)
    password = "".join(passwd)
    return password
