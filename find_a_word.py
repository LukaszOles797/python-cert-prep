def find_word(text1, text2):
    index = 0
    for ch in text1:
        index = text2.find(ch, index)
        if index == -1:
            return False
    return True
        

text1 = input("Please enter the first string: ")
text2 = input("Please enter the second string: ")

result = find_word(text1, text2)
if result:
    print("The word was found in the string!")
else:
    print("The word was not found in the string!")
