'''----------------------------Word frequency Counter------------------------'''

sentence = input("Enter the sentence: ")
dic = {}
list2 = []
sp = sentence.split(" ")

for i in sp:
    if i in list2:
        del i

    else :
        dic[i] = sp.count(i)
        del i    




# Find the highest frequency
high = max(dic.values())

# Print all words having the highest frequency
print("\nMost Frequently Occurring Word(s):")
for word in dic:
    if dic[word] == high:
        print(word, ":", high)

# Print words alphabetically
print("\nWords in Alphabetical Order:")
for word in sorted(dic):
    print(word, ":", dic[word])
        





