
# method for finding the longest substring of characters without them repeating

string = "pwwkew"
# start = 0
# end = 0
# count = 0
# empty_set = set()
# longest = 0
#
# #for i in range(len(string)):
#     #while string[i] in empty_set:
#         #empty_set.remove(string[start])
#         #start += 1
#     #empty_set.add(string[i])
#     #longest = max(end, i - start + 1)
#
# #print(longest)

curr = ""
longest = ""
seen = set()

for char in string:
    if char in seen:
        if len(curr) > len(longest):
            longest = curr
        seen = set()
        curr = ""
    seen.add(char)
    curr += char

print("Longest is: ", longest)