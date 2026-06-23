class DataUtils:
    """Utility methods for common data transformations."""

    @staticmethod
    def avg(numbers):
        """Return the arithmetic mean of a list of numbers.

        Args:
            numbers: A list of numeric values to average.

        Returns:
            The average as a float, or an error message string if the list is empty.

        Raises:
            TypeError: If ``numbers`` is not a list.
        """
        if not isinstance(numbers, list):
            raise TypeError(f"Expected list, got {type(numbers).__name__}")
        if len(numbers) == 0:
            return "Error: cannot average an empty list"
        running_total = 0
        for value in numbers:
            running_total += value
        return running_total / len(numbers)

    @staticmethod
    def reverse_string(text):
        """Return a new string with the characters of the input in reverse order.

        Args:
            text: The string to reverse.

        Returns:
            A new string containing the characters of ``text`` from last to first.

        Raises:
            TypeError: If ``text`` is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected str, got {type(text).__name__}")
        reversed_text = ""
        for char_index in range(len(text) - 1, -1, -1):
            reversed_text += text[char_index]
        return reversed_text


print(DataUtils.avg([10, 20, 30]))
print(DataUtils.avg([]))
print(DataUtils.reverse_string("hello"))
