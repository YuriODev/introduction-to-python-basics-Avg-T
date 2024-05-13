# Exercise 1
# Your solution comes here

number = int(input(" Enter a 5 digit integer:"))
sum1 = number % 10 + (number // 100) % 10 + (number // 10000) % 10
sum2 = (number // 1000) % 10 + (number // 10) % 10
print(f"{sum1}{sum2}")