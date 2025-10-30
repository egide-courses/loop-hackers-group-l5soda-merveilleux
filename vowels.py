text = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
v = 0
c = 0

for letter in text:
    if letter.isalpha():        # check if it is a letter
        if letter in vowels:
            v = v + 1
        else:
            c = c + 1

print("Vowels:", v)
print("Consonants:", c)
