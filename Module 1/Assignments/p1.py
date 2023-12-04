def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  
print(factorial(4))  

#The time complexity is O(n) since the function calls itself recursively n times.