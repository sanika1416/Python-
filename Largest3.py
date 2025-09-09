n, n1, n2 = map(int, input("Enter three numbers: ").split())

max = n
if n1 > max and n1 > n2 :
  max = n1
elif n2 > max and n2 > n1:
  max = n2

print("The maximum between three numbers is: ", max)