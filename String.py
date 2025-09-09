sentence = "   hello, how are YOU doing Today?   "

print(sentence.strip())  #removes the left white spaces 

print(sentence.split()) # splits the sentence in a list

print(sentence.strip().capitalize()) #removes the left whitespaces and capatalize the first letter

print(sentence.lower()) #converts the sentence in lower case

print(sentence.upper()) #converts the sentence in upper case

print(sentence.title()) #capitalizes the first letter of every word

print(sentence.swapcase()) #uppercase to lowercase and lowercase to uppercase

print(sentence.startswith('ar'))  #check whether the string starts with prefix

print(sentence.endswith('s'))   #check whether the string ends with suffix

print(sentence.count('re'))   #count the number of occurances of substring

print(sentence.isalpha())   #Checks if all characters are alphabetic

print(sentence.isalnum())  #Checks if all characters are alphanumeric

print(sentence.replace('hello', 'Hey')) #replaces the words with new word