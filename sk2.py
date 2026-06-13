def simple_generator():
    yield 1
    yield 2
    yield "Python"

for i in simple_generator():
    if i == "Python":
        print(i)
for i in simple_generator():
    print(i)
i = simple_generator()
print(next(i))
