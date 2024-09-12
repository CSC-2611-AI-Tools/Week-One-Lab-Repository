
roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

roman_string = "MCMXCIV"
split_roman_string = list(roman_string)
count = 0

for i in range(len(split_roman_string) - 1):
    if roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]:
        count = count - roman_dict[roman_string[i]]
    else:
        count = count + roman_dict[roman_string[i]]

count += roman_dict[roman_string[-1]]
print(count)

