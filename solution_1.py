def strict(func):
    'задача 1. декоратор, для отслеживания правильности типов элементов'
    def func_1(*a):
        s = func.__annotations__
        s1 = list(s)[:len(s)-1:]
        l = 0
        for i in s1:
            if s[i] != type(a[l]):
                raise TypeError
            l += 1
        r = func(*a)
        if type(r) == s['return']:
            return r
        else:
            raise TypeError
    return func_1



@strict
def sum_two(a: int, b: int) -> int: #int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError


