#twttr.py
string = input("Enter the string: \n")
newstring = ""
name = "aeiou"
nameUpper = "AEIOU"
for i in range(len(string)):
    if (string[i] not in name) and (string[i] not in nameUpper):
        newstring += string[i]

print(newstring)
