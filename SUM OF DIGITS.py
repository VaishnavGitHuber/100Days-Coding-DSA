n = int(input("Enter the number: "))
sum_digits = 0 

while(n > 0):
    digit = n % 10 
    sum_digits += digit
    n = n // 10

print("Sum of digit is: ",sum_digits)