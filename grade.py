def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


print("----- Gradebook Analyzer -----")

students = []
marks = []

# Take number of students
n = int(input("Enter number of students: "))

# Input student names and marks
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))

    students.append(name)
    marks.append(mark)

# Calculate average
average = sum(marks) / n

print("\n----- RESULT -----")
for i in range(n):
    grade = get_grade(marks[i])
    print(f"{students[i]} : {marks[i]} -> Grade: {grade}")

print("\nClass Average:", average)

# Highest and lowest marks
print("Highest Marks:", max(marks), "by", students[marks.index(max(marks))])
print("Lowest Marks:", min(marks), "by", students[marks.index(min(marks))])

# Students scoring above average
print("\nStudents scoring above average:")
for i in range(n):
    if marks[i] > average:
        print("-", students[i])