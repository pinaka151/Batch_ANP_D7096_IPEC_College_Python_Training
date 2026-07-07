'''----------------------Student Subject Report Card----------------------'''

dict = {}

Adding = True

# Taking Student Details
while(Adding):

    name = input("Enter Student Name: ")
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))

    dict[name] = {
        "Math": math,
        "Science": science,
        "English": english
    }

    choice = input("Do you want to add more students: ")

    if(choice.lower() == "yes"):
        Adding = True
    else:
        Adding = False


# Display Student Details
print("\nStudent Details")
for i in dict:
    print(i, "->", dict[i])


# Total, Average and Topper
print("\nTotal and Average Marks")

high_total = 0
topper = ""

for i in dict:

    total = dict[i]["Math"] + dict[i]["Science"] + dict[i]["English"]
    average = total / 3

    print(i, "Total =", total, "Average =", average)

    if(total > high_total):
        high_total = total
        topper = i

print("\nTopper :", topper)
print("Total Marks :", high_total)


# Subject Wise Highest Marks
subjects = ["Math", "Science", "English"]

for sub in subjects:

    high = 0
    student = ""

    for i in dict:

        if(dict[i][sub] > high):
            high = dict[i][sub]
            student = i

    print("\nHighest in", sub)
    print(student, "->", high)


# Students having Average >= 85
print("\nStudents having Average >= 85")

count = 0

for i in dict:

    total = dict[i]["Math"] + dict[i]["Science"] + dict[i]["English"]
    average = total / 3

    if(average >= 85):
        print(i, "->", average)
        count += 1

if(count == 0):
    print("No Student Found")