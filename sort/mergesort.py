#
# Merge Sort
# author: Valentin Lehuger
#
# Complexity:
#       best: O(n log(n))
#       average: O(n log(n))
#       worst: O(n log(n))
#
#       space: O(n)


def  mergeSort(l):

    size = len(l)
    if size == 1:
        return l
    a, b = mergeSort(l[:(size/2)]), mergeSort(l[size/2:])
    new = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i >= len(a):
            n = b[j]
            j+=1
        elif j >= len(b) or a[i] <= b[j]:
            n = a[i]
            i+=1
        else:
            n = b[j]
            j+=1
        new.append(n)
    return new
