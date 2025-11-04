import array
a=array.array('i',[1,2,3,4,5])

print(a[0])
print(a[4])

b=array.array('f',[2.3,5.6,9.0])
print(b[2])

#functions
a.append(11)
print(a)

a.insert(0,12)
print(a)

a.remove(12)
print(a)

a.pop()
print(a)

a.reverse()
print(a)

