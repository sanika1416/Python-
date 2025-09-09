n, n1, n2 = map(int, input("Enter three numbers: ").split())

min = n
if n1 < min and n1 < n2 :
  min = n1
elif n2 < min and n2 < n1:
  min = n2

print("The minimum between three numbers is: ", min)