
number = 121
digit_list = list(str(number))
print("digit list: ", digit_list)
reverse_digit_list = digit_list[::-1]
print("reversed digit list: ", reverse_digit_list)

if digit_list == reverse_digit_list:
    print(True)
else:
    print(False)