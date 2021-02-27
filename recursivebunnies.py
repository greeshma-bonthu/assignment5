def bunnyears(bunnies):
    if (bunnies == 0):
        return 0
    else:
        if (bunnies % 2 == 0):
            return 3 + bunnyears(bunnies-1)
        else:
            return 2 + bunnyears(bunnies-1)

result = bunnyears(1)
print(result)