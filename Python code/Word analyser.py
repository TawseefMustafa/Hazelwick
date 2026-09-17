#Main program
word = input("Enter a word: ")
print(f"Reversed: {word[::-1]}")
print(f"Uppercase: {word.upper()}")
print(f"Length: {len(word)}")
print(f"Palindrome: {word.upper() == word[::-1].upper()}")
print(f"First letter character code: {ord(word[0])}")
print(f"Middle character: {word[len(word)//2]}")
#Ext
letter = input("Enter a character: ")
if letter in word:
    print(f"'{letter}' appears {word.lower().count(letter.lower())} times in {word}, making its first appearance on character number {word.lower().find(letter.lower())+1} (index {word.lower().find(letter.lower())})")
else:
    print(f"'{letter}' is not in {word}")
temp = word[0]
secret = chr(ord(temp)+1) + word[1:len(word)]
print(f"The secret word is: {secret}")