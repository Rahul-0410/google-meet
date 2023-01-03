def recurcive_func(n):
    if n==0:
        return 1
    elif n<0:
        return "Please input positive integer"
    return n*recurcive_func(n-1)

n=int(input())
print(f"Factorial of {n} = {recurcive_func(n)}")