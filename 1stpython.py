print('hello world')

a = 1
print(type(a))

b = 'hello'
print(type(b))

c = [1, 2  ,       3, 4, 5, 6]
print(type(c))

for dinosaur in c:
	print(dinosaur)

for i in range(1,10):
	print(i)

d = ['apple', 'banana', 'orange']
fruit = d[1]
print(fruit)

e = []
print(e)
e.append('apple')
print(e)
e.append('pineapple')
print(e)
e.append('shark')
print(e)

e.append( [1,2,3,4,5] )
print(e)

r = e.pop()
print(r)
print(e)

r2 = e.pop()
print(r2)
print(e)

r3 = e.remove('apple')
print(r3)
print(e)

