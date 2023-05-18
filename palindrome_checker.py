def check_if_palindrome(text):
    if len(text) == 0:
        return False
    else:
        i = 0
        for i in range(0, len(text)//2):
            if text[i] != text[len(text)-1-i]:
                return False
        return True


text = input("Please enter the text: ")
text = text.replace(" ", "").upper()

result = check_if_palindrome(text)

if result:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
