import math

def solve(a, b, c):    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the equation has real roots
    if discriminant > 0:
        # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [root1, root2]
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return [root]
    else:
        # No real roots
        return []

print(solve(float(input("Enter Co-efficient of 'a' term: ")),float(input("Enter Co-efficient of 'b' term: ")),float(input("Enter Co-efficient of 'c' term: "))))