#
# Insertion Sort
# author: Valentin Lehuger
#
# Complexity: 
#       best: O(n)
#       average: O(n²)
#       worst: O(n²)
#
#       space: O(1)


def insertionSort(l):
    """ 
    Assume that the first element is a sorted list.
    It add the next elements one by one at the right
    position.
    """

    for i in range(1, len(l)):
        
        pos = i
        n = l[i]
        while pos > 0 and l[pos - 1] > n:
            l[pos] = l[pos - 1]
            pos -= 1
        l[pos] = n
    return l


if __name__ == '__main__':

    tests = [
        [1, 2, 3, 4], # Best
        [4, 3, 2, 1], # Worst
        [2, 3, 4, 1],
        [1, 3, 2, 4]
    ]

    for test in tests:
        print "test =", test
        res = insertionSort(test)
        print "result =", res



