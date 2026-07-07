'''----------------------Vowel Counter using Function----------------------'''

# Function to count vowels
def count_vowels(text):

    count = 0

    for i in text:

        if(i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u"):
            count += 1

    return count


# Main Program
sentence = input("Enter a sentence: ")

result = count_vowels(sentence)

print("Total Vowels:", result)