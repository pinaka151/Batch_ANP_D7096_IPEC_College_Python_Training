# Word Frequency Counter

def word_frequency(sentence):

    # Remove punctuation
    for ch in ".,!?;:":
        sentence = sentence.replace(ch, "")

    # Convert to lowercase
    sentence = sentence.lower()

    # Convert sentence into list of words
    words = sentence.split()

    # Count frequency
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Display words in alphabetical order
    print("\nWord Frequency:")
    for word in sorted(frequency):
        print(word, ":", frequency[word])

    # Find most repeated word
    most_word = max(frequency, key=frequency.get)

    print("\nMost Repeated:")
    print(most_word)


# Main Program
sentence = input("Enter a sentence: ")
word_frequency(sentence)