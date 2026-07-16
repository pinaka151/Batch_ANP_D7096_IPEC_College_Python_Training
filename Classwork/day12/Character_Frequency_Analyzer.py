# Character Frequency Analyzer

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

frequency = {}

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

    # Count frequency of each character
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Find the most frequent character
most_char = ""
max_count = 0

for ch in frequency:
    if frequency[ch] > max_count:
        max_count = frequency[ch]
        most_char = ch

# Display results
print("\n----- Character Analysis -----")
print("Uppercase :", uppercase)
print("Lowercase :", lowercase)
print("Digits :", digits)
print("Special Characters :", special)
print("Most Frequent Character :", most_char)