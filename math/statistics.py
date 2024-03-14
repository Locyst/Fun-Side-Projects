# ---------- Statistics ---------- #

def _organize(input_list):
    """Sorts the input list."""
    return sorted(input_list)

def numeric_check(input_list):
    """Checks if all elements in the list are numeric."""
    return all(isinstance(x, (int, float)) for x in input_list)

def length_check(input_list):
    """Checks if the list is not empty."""
    return len(input_list) > 0

def mean(input_list):
    """Calculates the mean of the input list."""
    if not numeric_check(input_list) or not length_check(input_list):
        raise ValueError("Input list must contain numeric values and cannot be empty")

    return sum(input_list) / len(input_list)

def mode(input_list):
    """Calculates the mode of the input list."""
    if not numeric_check(input_list) or not length_check(input_list):
        raise ValueError("Input list must contain numeric values and cannot be empty")

    return max(set(input_list), key=input_list.count)

def median(input_list):
    """Calculates the median of the input list."""
    if not numeric_check(input_list) or not length_check(input_list):
        raise ValueError("Input list must contain numeric values and cannot be empty")

    sorted_list = _organize(input_list)
    n = len(sorted_list)
    if LocystMath.std.odd_check(n):
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

def range(input_list):
    """Calculates the range of the input list."""
    if not numeric_check(input_list) or not length_check(input_list):
        raise ValueError("Input list must contain numeric values and cannot be empty")

    sorted_list = _organize(input_list)
    return sorted_list[-1] - sorted_list[0]
