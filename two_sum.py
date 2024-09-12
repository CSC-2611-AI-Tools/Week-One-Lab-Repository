
# method for finding index number of two elements adding up to 9

# test case one
dictionary_one = [2, 7, 11, 5]
target_one = 9
length_one = len(dictionary_one)

for i in range(0, length_one - 1):
    if dictionary_one[i] + dictionary_one[i + 1] == target_one:
        print("[", i, ",", i + 1, "]")

# test cast two
dictionary_two = [3, 3]
target_two = 6
length_two = len(dictionary_two)

for i in range(0, length_two - 1):
    if dictionary_two[i] + dictionary_two[i + 1] == target_two:
        print("[", i, ",", i + 1, "]")

# test case three
dictionary_three = [3, 2, 4]
target_three = 6
length_three = len(dictionary_three)

for i in range(0, length_three - 1):
    if dictionary_three[i] + dictionary_three[i + 1] == target_three:
        print("[", i, ",", i + 1, "]")