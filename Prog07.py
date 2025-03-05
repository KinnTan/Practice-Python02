#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

counter = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        counter += 1
print (counter)