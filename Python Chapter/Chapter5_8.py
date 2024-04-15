def count_characters(s):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    other_count = 0

    # 遍历字符串中的每一个字符
    for char in s:
        if char.isupper():  # 检查是否为大写字母
            upper_count += 1
        elif char.islower():  # 检查是否为小写字母
            lower_count += 1
        elif char.isdigit():  # 检查是否为数字
            digit_count += 1
        else:  # 其他所有字符
            other_count += 1

    # 返回一个包含所有计数的元组
    return (upper_count, lower_count, digit_count, other_count)


# 示例使用
result = count_characters("Hello, World! 1234")
print("大写字母：", result[0], "小写字母：", result[1], "数字：", result[2], "其他字符：", result[3])
