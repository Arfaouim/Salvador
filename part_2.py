def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """

    r = [(numbers.index(x),numbers.index(y)) for x in numbers for y in numbers if x+y == target_sum]
    t = tuple(r)   
             
    return t 

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))