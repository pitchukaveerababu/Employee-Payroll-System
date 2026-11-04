def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a positive number!")
                continue

            return value

        except ValueError:
            print("Invalid input! Enter numbers only.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Value must be greater than zero!")
                continue

            return value

        except ValueError:
            print("Invalid input! Enter a valid number.")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty!")
def get_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter zero or a positive number!")
                continue

            return value

        except ValueError:
            print("Invalid input! Enter numbers only.")