def my_range():
    n=0
    while n<5:
        yield n
        n += 1

s = my_range()
for num in s:
    print(num)