def almostIncreasingSequence(sequence):
    stop = False
    prev = last = min(sequence) - 1
    for item in sequence:
        if item <= last:
            if stop:
                return False
            else:
                stop = True

            if item <= prev:
                pass
            elif item > prev:
                last = item
        else:
            prev, last = last, item
    return True


print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))
print(almostIncreasingSequence([1, 2, 1, 2]))
print(almostIncreasingSequence([3, 6, 5, 8, 10, 20, 15]))
print(almostIncreasingSequence([1, 1, 2, 3, 4, 4]))
print(almostIncreasingSequence([1, 1, 1, 2, 3]))
