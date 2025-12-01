# def factorail(n):
#     result = 1
# for i in range(1,n+1):
#         result*=1
#     return result
# print(factorail(5))
    
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(8))
