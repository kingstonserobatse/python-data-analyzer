"""Collect numbers until 'done', then display a small statistics summary.

Build this program one TODO at a time. The README has the suggested order.
"""


def main():
    # TODO 1: Create your starting values before the loop.
    # Hint: count and total start at 0. What value can smallest/largest use
    # before you've received the first valid number?
    count = 0
    total = 0
    smallest = None
    largest = None
    print("Enter numbers one at a time; type 'done' to finish.")

    while True:
        entry = input("Number: ")

        # TODO 2: If entry is "done", leave the loop with break.
        if entry == 'done':
            break

        # TODO 3: Convert entry to a number with try/except.
        # If conversion fails, print a friendly message and continue.
        try:
            number = float(entry)
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.")
            continue
        # TODO 4: For a valid number, update count, total, smallest, and
        # largest. Keep these updates inside the loop, but don't reinitialize
        # the running values here.
        count = count + 1
        total = total + number

        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
       
    # TODO 5: Print count and total. If count is greater than zero, calculate
    # and print the average, smallest, and largest. Otherwise explain that
    # there were no valid numbers to summarize.

    print("Count:", count)
    print("Total:", total)
    if count > 0:
        average = total / float(count)
        print("Average:", average)
        print("Smallest:", smallest)
        print("Largest:", largest)
    else:
        print("No valid numbers were entered to summarize.")

if __name__ == "__main__":
    main()
