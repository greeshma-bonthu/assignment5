def decorators(func):
    str="python"
    for i in str:
        x = i + str
    return func
 
 
@decorators
def func(x):
    print(x)