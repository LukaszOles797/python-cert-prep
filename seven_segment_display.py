segments = [["###", "#", "###", "###", "# #", "###", "###", "###", "###", "###"],
["# #", "#","  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"],
["# #", "#","###", "###","###","###","###", "  #","###","###"],
["# #", "#", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"],
["###", "#","###", "###", "  #", "###", "###", "  #", "###", "###"]]

def display_digits(number):
    for i in range(5):
        for ch in number:
            print(segments[i][int(ch)], end=" ")
        print()


number = input("Please enter the number to display: ")
display_digits(number)
