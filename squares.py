import math

def squares(a , b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

# Running Examples
print(squares(3, 9))
print(squares(17, 24))
print(squares(1, 1000000000))
