def caesar_cipher(text_to_encode, shift_value):
    encoded_text= []
    for ch in text_to_encode:
        if ch.isalpha():
            if ch.islower():
                ch_num = ord("a") + ((ord(ch) - ord("a") + shift_value) % 26) 
                encoded_text.append(chr(ch_num))
            else:
                ch_num = ord("A") + ((ord(ch) - ord("A") + shift_value) % 26)  
                encoded_text.append(chr(ch_num))
        else:
            encoded_text.append(ch)
    return ''.join(encoded_text)

            
text_to_encode = input("Please enter the text: ")

while True:
    shift_value = input("Please enter a shift value (1-25): ")
    if shift_value.isdigit():
        shift_value = int(shift_value)
        if shift_value >= 1 and shift_value <= 25:
            break
        else:
            print("You have entered a value out of range!")
    else:
        print("You have entered an invalid value!")

print("Encoded text:", caesar_cipher(text_to_encode, shift_value))
