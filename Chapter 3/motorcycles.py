motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表元素
'''
motorcycles[0] = 'ducati'
print(motorcycles)
'''

# 添加列表元素
"""
motorcycles.append('ducati')
print(motorcycles)
"""

# 插入列表元素
'''
motorcycles.insert(0, 'ducati')
print(motorcycles)
'''

# 删除列表元素
"""
del motorcycles[0]
print(motorcycles)
"""
# pop()
'''
popped_motorcycles = motorcycles.pop()
last_owned = popped_motorcycles
print(motorcycles)
print(popped_motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")
'''
