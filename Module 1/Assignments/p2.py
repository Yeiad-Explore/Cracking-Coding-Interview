def natral_sum(a, b):
    
    if a > b:
        a, b = b, a

    
    return (b - a + 1) * (a + b) // 2


print(natral_sum(1, 4))  
print(natral_sum(10, 6)) 


#Time Complexity = O(1)
#Space Coplexity = O(1)