def calculate_digit_of_life(birth_date):
    digits_sum = 0
    for ch in birth_date:
        digit = int(ch)
        digits_sum += digit
    if digits_sum >= 10:
        return calculate_digit_of_life(str(digits_sum))
    else:
        return digits_sum


birth_date = input("Please enter the date of your birthday (format MMDDYYYY): ")
digit_of_life = calculate_digit_of_life(birth_date)
print("Your digit of life is equal to:", digit_of_life)
