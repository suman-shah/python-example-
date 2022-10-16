class InvalidInputError(Exception):
    def __init__(self, input_value):
        """
        Custom invalid input error inheriting from the base Exception class.
        """
        self.input_value = input_value
        self.message = f"Invalid input: {input_value}. Valid inputs are: 1, 2, 3."

        super().__init__(self.message)


class CustomNameError(Exception):
    """
    Custom name error inheriting from the base Exception class.
    """

    def __int__(self):
        self.message = "The application has raised a custom name error."
        super().__init__(self.message)


class CustomTypeError(Exception):
    """
    Custom type error inheriting from the base Exception class.
    """

    def __int__(self):
        self.message = "The application has raised a custom type error."
        super().__init__(self.message)


class CustomValueError(Exception):
    """
    Custom value error inheriting from the base Exception class.
    """

    def __int__(self):
        self.message = "The application has raised a custom value error."
        super().__init__(self.message)


def get_user_input():
    print("\nHello. This application is a demonstration of custom Python exceptions.")
    print("There are four custom exceptions available, all inheriting from the base Exception class:\n")
    print("1 - A custom name error.")
    print("2 - A custom type error.")
    print("3 - A custom value error.")
    print("4 - A custom input error.")
    print("\nPlease enter a name from 1 to 3 to raise one of the corresponding errors and see their output.")
    print("Entering any other input will raise the custom input error instead.")

    user_input = input("\nYour input: ")

    if user_input == "1":
        raise CustomNameError()
    elif user_input == "2":
        raise CustomTypeError
    elif user_input == "3":
        raise CustomValueError
    else:
        raise InvalidInputError(user_input)


get_user_input()


quit()
