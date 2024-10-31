# 3.4
guests = ['li', 'zhu', 'sun', 'he']
print(f"Hi! {guests[0].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[1].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[2].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[3].title()}, would you like eating dinner with me tonight?")

# 3.5
print(f"{guests[2]} can't enjoy this dinner")
guests[2] = 'chen'
print(f"Hi! {guests[0].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[1].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[2].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[3].title()}, would you like eating dinner with me tonight?")

# 3.6
print(f"I find a big table, that we can invite more friends eating dinner together!")
guests.insert(0, 'jiang')
guests.insert(2, 'hu')
guests.append('huang')
print(f"Hi! {guests[0].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[1].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[2].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[3].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[4].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[5].title()}, would you like eating dinner with me tonight?")
print(f"Hi! {guests[6].title()}, would you like eating dinner with me tonight?")

# 3.7
print("I can only invit two friends, because the table can't deliver in time.:(")
poped_guest = guests.pop()
print(f"{poped_guest.title()},I'm sorry to you can't eating dinner with me!")
poped_guest = guests.pop(0)
print(f"{poped_guest.title()},I'm sorry to you can't eating dinner with me!")
poped_guest = guests.pop()
print(f"{poped_guest.title()},I'm sorry to you can't eating dinner with me!")
poped_guest = guests.pop()
print(f"{poped_guest.title()},I'm sorry to you can't eating dinner with me!")
poped_guest = guests.pop()
print(f"{poped_guest.title()},I'm sorry to you can't eating dinner with me!")
print(guests)
print(f"{guests[0].title()}! You can still have dinner with me.")
print(f"{guests[1].title()}! You can still have dinner with me.")
del guests[0]
del guests[0]
print(guests)
