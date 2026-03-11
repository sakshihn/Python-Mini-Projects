print("---Test Sentiment Counter---")

text = input("Enter your Review:").lower()

words = text.split()
print("your wowrds:",words)

postitve_words = ["amazing", "good", "great", "awesome", "fantastic"]
negative_words = ["bad", "terrible", "awful", "boring", "poor"]

positive_count = 0
negative_Count = 0

for word in words:
    if word in postitve_words:
        positive_count += 1
    elif word in negative_words:
        negative_Count += 1

print("Positive count: ",positive_count)
print("Negative Count: ",negative_Count)

if positive_count > negative_Count:
    print("The statement is Positive!")
elif negative_Count > positive_count:
    print("The statement is Negative!")
else:
    print("The statement is neutral!")