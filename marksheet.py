def addition():
    try:
        marks = [
            float(input(f"Enter marks for subject {i}: "))
            for i in range(1, 6)
        ]

        total = sum(marks)
        average = total / len(marks)

        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")

    except ValueError:
        print("Please enter valid numeric marks.")
    finally:
        print("Marks processing completed.")


addition()