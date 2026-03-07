while True:

    try:
        num = input("Enter the numbers: ")
        number = num.split()

        num_list = []

        # Convert input strings to integers
        for i in number:
            a = int(i)
            num_list.append(a)

        print("Numbers entered:", num_list)

        b = len(num_list)
        print("Total numbers:", b)

        total = sum(num_list)
        print("Sum:", total)

        average = total / b
        print("Average:", average)

        maxi = max(num_list)
        print("Max:", maxi)

        mini = min(num_list)
        print("Min:", mini)

        even_num = []
        odd_num = []

        for i in num_list:
            if i % 2 == 0:
                even_num.append(i)
            else:
                odd_num.append(i)

        print("Even numbers:", even_num)
        print("Odd numbers:", odd_num)

    except ValueError:
        print("Invalid input! Please enter only numbers.")

    # Ask user if they want to run again
    choice = input("Do you want to try again? (y/n): ")

    if choice.lower() != 'y':
        print("Program ended.")
        break