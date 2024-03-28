def is_repeat_less_than_half(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for count in char_counts.values():
        if count > len(s) / 2:
            return False
    return True


data = ["aaabb", "abc", "aabbcc", "aabbc", "aabcd"]
filtered_data = [s for s in data if is_repeat_less_than_half(s)]
print(filtered_data)