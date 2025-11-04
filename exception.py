n1=int(input("Enter no:"))
n2=int(input("Enter no:"))

try:
    ans=n1/n2
    print("division is ",ans)
except ZeroDivisionError:
    print("can't divide by zero")

print("Reamaining code")