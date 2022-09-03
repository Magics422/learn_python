a = [3, 5, 7, 9, 10.5]
a.append('Python')

print(a)
print(len(a))

print(a[0])
print(a[-1])
print(a[1], a[2], a[3])
a.remove("Python")

b = {'city': 'Москва', 'temper':"20"}

print(b['city'])
b['temper'] = int(b['temper']) -5

print(b)

print(b.get("country"))
b['country'] = 'Россия'
b['date'] = '27.05.2019'
print(b)