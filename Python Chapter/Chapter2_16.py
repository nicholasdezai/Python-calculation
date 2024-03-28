# 获取用户输入的列表
input_list_str = input("请输入一个列表，元素之间用逗号分隔：")
# 将输入的字符串转换为列表，这里假设用户输入的都是整数
input_list = [int(item.strip()) for item in input_list_str.split(',')]

# 获取用户输入的两个整数作为下标
start_index = int(input("请输入起始下标："))
end_index = int(input("请输入结束下标："))

# 根据下标截取子列表。注意，因为Python的切片是左闭右开的，所以end_index需要+1
sublist = input_list[start_index:end_index + 1]