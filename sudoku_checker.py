def check_lines(sudoku):
    for i in range(9):
        sum = 0
        for num in sudoku[i]:
            sum += int(num)
        if sum != 45:
            return False
    return True
    
def check_columns(sudoku):
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += int(sudoku[j][i])
        if sum != 45:
            return False
    return True

def check_sub_squares(sudoku):
    for p in range(0,9,3):
        for i in range(0,9,3):
            sum = 0
            for k in range(3):
                for j in range(3):
                    sum += int(sudoku[i+k][j+p])
            if sum != 45:
                return False
    return True
        

def sudoku_checker(sudoku):
    return check_lines(sudoku) and check_columns(sudoku) and check_sub_squares(sudoku)

proceed = True

i = 0
sudoku = []
for i in range(9):
    print("Please enter the sudoku line", i+1, "(after every line press Enter):")
    line = input()
    line_list = list(line)
    if line == "":
        break
    if len(line) != 9:
        print("You have entered an incorrect number of values!")
        proceed = False
        break
    elif not line.isdigit():
        print("You have entered an incorrect value!")
        proceed = False
        break
    else:
        sudoku.append(line_list)
        i += 1
    
if len(sudoku) != 9:
    print("You have entered an incorrect number of lines!")
elif proceed == True:
    if sudoku_checker(sudoku):
        print("The sudoku is valid!")
    else:
        print("The sudoku is invalid!")
