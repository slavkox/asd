def quicksort(arr):
    '''
    I'd like to think it can be done better
    '''
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]

    right = [x for x in arr[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)
