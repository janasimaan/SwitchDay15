def is_rotation(word1, word2):
    if len(word1) != len(word2):
        return False

    doubled_word = word1 + word1

    return word2 in doubled_word


word1 = "waterbottle"
word2 = "erbottlewat"

result = is_rotation(word1, word2)
print(f"Is '{word2}' a rotation of '{word1}'? {result}")
