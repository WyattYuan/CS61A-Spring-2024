def call_func(times, func):
    for i in range(times):
        func()


def hello():
    print("Hello, world!")


# call_func(3,hello)








def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


# print(curried_pow(2)(3))


def curry2(f):
    """Return a curried version of the given two-argument function."""

    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


def simple_decorator(func):
    def wrapper(*args):
        print("函数执行前的操作")
        result = func(*args)
        print("函数执行后的操作")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"你好，{name}！")

greet("小明")  
# 输出:
# 函数执行前的操作
# 你好，小明！
# 函数执行后的操作
