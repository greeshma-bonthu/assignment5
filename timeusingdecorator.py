import time
def time_cal(func):
    def wrapper():
        start = time.time()
        value = func()
        end = time.time()
        print("Time taken for print statement " +str(end - start))
        return value
    return wrapper()

@time_cal
def func():
    print("test")