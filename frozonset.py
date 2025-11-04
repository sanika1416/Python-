i= frozenset([1,3,5,6])
print(i)
for j in i:
    print(j)

a= frozenset([1,9,8,7])
print(a)

b= i.intersection(a)
print(b)

c = i.union(a)
print(c)

print(i.symmetric_difference(a))