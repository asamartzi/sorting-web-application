from random import randrange


def quicksort(list, start, end):
    #The algorithm will complete when the start and end pointers indicate a list with one or zero elements.
    if start >= end:
        return list
    print("Running quicksort on {0}".format(list[start: end + 1]))
    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))
    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(list[i], pivot_element))
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    print("{0} successfully partitioned".format(list[start: end + 1]))
    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)
