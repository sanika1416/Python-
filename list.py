tasks = ['buy milk', 'call mom', 'study', 'buy milk']

tasks.append('reading book')   #adding at the end of the list
print(tasks)

tasks.remove('buy milk')  #remove first element
print(tasks)

print(tasks.count('buy milk'))  #count the occurences

tasks.sort()  #sorts the list in alphabetical order
print(tasks)

tasks.reverse() #reverse the list
print(tasks)

print(len(tasks)) #number of elements present in the list

print('walking' in tasks) #membership test

print(tasks[1: 4])   #slicing

tasks.clear()   #removes all elements
print(tasks)



