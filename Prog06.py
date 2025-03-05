#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

numbers = []
for i in range(10):
    num = (int(input("Enter a number: ")))
    numbers.append(num)

num1 = numbers[0]

for i in range(1, 10):
    results = num1 - numbers[i]
    print(results)


