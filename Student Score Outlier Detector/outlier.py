raw_data=input("Enter the Student's score: ")

data=[]
data = raw_data.split(",")
print("Your data: ",data)

cleaned_data=[]
outliers=[]
invalid_data=[]

for i in data:
    try:
        score=int(i)
        if score <= 100:
            cleaned_data.append(score)
        else:
            outliers.append(score)

    except:
        invalid_data.append(i)

print("The outliers are: ",outliers)
print("The invalid data: ",invalid_data)
print("Cleaned dataset is here:",cleaned_data)

print("---Data Analysis---")

total_students = len(cleaned_data)
max_score = max(cleaned_data)
min_score = min(cleaned_data)
avg_score = sum(cleaned_data)/total_students

print("Total number of students: ",total_students)
print("Maximum score: ",max_score)
print("Minimum score: ", min_score)
print("Average score: ",avg_score)