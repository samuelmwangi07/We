#while loop
from variable import language

number = 100
while number <= 105:
    print(number)
    number += 1

print("Done")
print()

#Program 2

num = 10
while num >= 5:
    print("Number:", num)
    num -= 1


print()




#For loop
for numb in range(100, 106):
    print(numb)

languages = ["Python", "Javascript", "Java"]
for lang in languages:
    print(lang)


    #Break and continue statements

for n in range(1, 20):
    if n == 5:
        continue
    if n == 9:
        break
    print(n)