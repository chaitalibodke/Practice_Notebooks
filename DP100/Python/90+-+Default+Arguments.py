# -----------------------------------------------------------
# Default Arguments in Python Functions
#
# 1. Similar to required arguments but with default values
# 2. Takes from 0 to n arguments
# 3. Accepts default arguments when not provided
# -----------------------------------------------------------

def myFunction(var1, var2=0):
    print("Var1 is : ", var1)
    print("Var2 is : ", var2)
    result = var1 + var2
    return result


a = 10
b = 20

res = myFunction(a,b)
print(res)






























