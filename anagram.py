#create a function that tells user whether or not strings entered as arguments 
#are anagrams
def isanagram(string1,string2):
	string1 = string1.replace(' ','').lower()
	string2 = string2.replace(' ','').lower()
	anagram = []
	for char in string1:
		if char in string2:
			if char not in anagram:
				anagram.append(char)
			else:
				return print('False')
				break
		else:
			return print('False')
			break
	return print("True")

isanagram('Listen', 'Silent')
isanagram("care","race")


