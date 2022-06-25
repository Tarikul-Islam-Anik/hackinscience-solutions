def caesar_cypher_encrypt(s, key):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                index = ord(s[i]) - 97
                new_index = (index + key) % 26
                s[i] = chr(new_index + 97)
            else:
                index = ord(s[i]) - 65
                new_index = (index + key) % 26
                s[i] = chr(new_index + 65)
    return "".join(s)


def caesar_cypher_decrypt(s, key):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                index = ord(s[i]) - 97
                new_index = (index - key) % 26
                s[i] = chr(new_index + 97)
            else:
                index = ord(s[i]) - 65
                new_index = (index - key) % 26
                s[i] = chr(new_index + 65)
    return "".join(s)
