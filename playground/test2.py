def almostIncreasingSequence(sequence):

    stop = False
    prev = last = min(sequence) - 1
    for item in sequence:
        if item <= last:
            if stop:
                return False
            else:
                stop = True
            if item >= prev:
                last = item
        else:
            prev, last = last, item
    return True


print(almostIncreasingSequence([1, 2, 1, 2]))
