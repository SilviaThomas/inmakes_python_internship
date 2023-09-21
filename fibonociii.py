def fibonacci_series(n):
    fib = [0, 1]
    while len(fib) < n:
        next= fib[-1] + fib[-2]
        fib.append(next)
    return fib
num = 13
seq= fibonacci_series(num)
print(seq)

