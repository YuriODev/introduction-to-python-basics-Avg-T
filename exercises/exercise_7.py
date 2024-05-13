# Exercise 7
# Your solution comes here

n = int(input("choose a 4-digit interger\n"))

print((n % 10) + ((n//10) % 10) + ((n//100)%10) + ((n//1000)%10))