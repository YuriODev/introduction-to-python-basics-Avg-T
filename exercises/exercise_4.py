# Exercise 4
# Your solution comes here

n = int(input("choose a 4-digit interger\n")) 

if (n // 1000) % 10 == n % 10 and (n // 100) % 10 == (n // 10) % 10:
    print(1)
else:
    print(0)