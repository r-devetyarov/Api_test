import random

a = [i % 4 for i in range(1, 15)]
print(a)
b = [i * 5 for i in 'hello']
print(b)
c = [random.randint(-10, 10) for i in range(10)]
print(c)
d = [elem for elem in c if elem % 2 == 0]
print(d)
n = 5
m = 4
e = [[1] * m for i in range(n)]
for i in e:
    print(i)
t = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(t)


# выражения генераторы (не хранятся в памяти) - можно обходить только один раз

# gen = (i for i in range(10000000000))
# for i in gen:
#     print(i)

# функции генератора

def gen():
    for i in [43, 54, 67, 99]:
        yield i


s = gen()
print(next(s))
print(next(s))
print('work function:')
for i in gen():
    print(i)
