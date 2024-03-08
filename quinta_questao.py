string = input()
reverse_string = ""

for i in range(0, len(string)):
    reverse_string = string[i] + reverse_string

print(reverse_string)

