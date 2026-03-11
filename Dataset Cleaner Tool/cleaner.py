print("---- Dataset Cleaner Tool ----\nThis program cleans messy datasets for analysis.")

data = input("Enter the Data: ")
Original_dataset = data.split(",")
print(Original_dataset)

def remove_spaces(Original_dataset):
    cleaned = list(map(lambda x: x.strip().lower() ,Original_dataset))

    cleaned = [x for x in cleaned if x]  # keep only non-empty items

    return cleaned

cleaned = remove_spaces(Original_dataset)

print("Cleaned Dataset :", ", ".join(cleaned))
