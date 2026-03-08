print("---Welcome to Text Frequency Analyzer---")

print("---Welcome to Text Frequency Analyzer---")

text = input("Enter the text: ").lower()

for p in '''!()-[]{};:'"\\,<>./?@#$%^&*_~''':
    text = text.replace(p, "")

print("Your text is", text)

text_list = text.split()
print("words:", text_list)

text_dict = set(text_list)
print("Unique words:", text_dict)

word_frequency = {}

for i in text_dict:
    count = text_list.count(i)
    word_frequency[i] = count

print("word Frequencies")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)

max_freq = max(word_frequency.values())

for word, frequency in word_frequency.items():
    if frequency == max_freq:
        print("Most frequent word:", word, "with frequency:", frequency)