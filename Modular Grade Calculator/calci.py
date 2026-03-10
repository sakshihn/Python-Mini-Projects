print("--- Modular Grade Calculator ---")

def get_marks():
    num_subjects = int(input("Enter the number of Subjects: "))
    marks = []

    for i in range(num_subjects):
        mark = int(input("Enter the marks: "))
        marks.append(mark)
    return marks 
marks = get_marks()
print(f"Marks entered : {marks} ")

def calc_avg(marks):
    total = sum(marks)
    avg = lambda total, count: total / count
    average = avg(total, len(marks))
    return average
avgg = calc_avg(marks)
print("Average Marks: ", avgg )