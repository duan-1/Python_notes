# 将一些朋友的姓名存储在一个列表中，并将其命名为 names。
# 依次访问该列表的每个元素，从而将朋友的名字都打印出来。
names = ['fox', 'dog', 'pig', 'wolf']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 继续使用上面的列表，但不打印每个朋友的姓名，而是为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
message = ", good morning!"
print(f"{names[0].title()}{message}")
print(f"{names[1].title()}{message}")
print(f"{names[2].title()}{message}")
print(f"{names[3].title()}{message}")