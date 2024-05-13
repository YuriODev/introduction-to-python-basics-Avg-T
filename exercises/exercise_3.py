# Exercise 3
# Your solution comes here

n = int(input("how many seconds have passed?\n"))

h = 0
m = 0
s = 0

while n >= 60:
    if n >= 3600:
        n -= 3600
        h += 1
    if n >= 60:
        n -= 60
        m += 1

s = n

print(f"{h}:{m:02d}:{s:02d}")