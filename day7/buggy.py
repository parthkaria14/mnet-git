def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a / b

def get_first(lst):
    if not lst:
        print("Error: List is empty")
        return None
    return lst[0]

def to_number(s):
    try:
        return int(s)
    except ValueError:
        print(f"Error: '{s}' is not a valid integer")
        return None

if __name__ == "__main__":
    print(divide(10, 0))
    print(get_first([]))
    print(to_number("hello"))
