

strings = ["flower", "flow", "flight"]
prefix = strings[0]
for string in strings:
    while not string.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            print("")
print(prefix)
