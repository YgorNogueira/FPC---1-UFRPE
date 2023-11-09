def fib(n):
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (1, 1)
    else:
        fib_n_menos_1, calls_n_menos_1 = fib(n-1)
        fib_n_menos_2, calls_n_menos_2 = fib(n-2)
        return (fib_n_menos_1 + fib_n_menos_2, calls_n_menos_1 + calls_n_menos_2 + 1)

n = int(input())
for i in range(n):
    x = int(input())
    fib_x, calls = fib(x)
    print(f'fib({x}) = {calls-1} calls = {fib_x}')