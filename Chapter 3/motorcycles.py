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
## 删除任意位置的元素
'''
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
'''

## 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")