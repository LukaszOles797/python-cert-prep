def check_if_anagram(text1, text2):
    if len(text1) != len(text2) or len(text1) == 0:
        return False
    else:
        list1 = list(text1)
        list2 = list(text2)
        for ch in list1:
            if ch in list2:
                list2.remove(ch)
            else:
                return False
    return True
               
    
text1 = input("Please enter the first text: ")
text2 = input("Please enter the second text: ")

text1 = text1.replace(" ", "").upper()
text2= text2.replace(" ", "").upper()

result = check_if_anagram(text1, text2)
if result:
    print("Anagrams")
else:
    print("Not anagrams")
