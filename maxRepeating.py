def max_repeating_char(str):
    char_count = {}

    max_count = 0
    max_char = None

    for char in str:
        char_count[char] = char_count.get(char, 0) + 1

        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char

    return max_char


string = "abafbch"
result = max_repeating_char(string)
print(f"Max repeating character: {result}")
