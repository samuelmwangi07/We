

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "it's the largest number")
else:
    print(third,"is the largest number")