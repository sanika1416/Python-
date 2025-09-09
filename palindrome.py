n = int(input("Enter a number: "))
temp = n
newN = 0

while n != 0:
  digit = n % 10
  newN = 10 * newN + digit
  n = int(n / 10)

if newN == temp:
  print("Given number is palindrome")  
else:
  print("Given number is not palindrome")