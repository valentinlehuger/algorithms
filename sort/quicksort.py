def quickSort(l, start, end):
    if end + 1 - start <= 1:
        return
    pivot = l[end]
    size_left = start
    for i in range(start, end):
        if l[i] < pivot:
            l[i], l[size_left] = l[size_left], l[i]
            size_left += 1
    l[end], l[size_left] = l[size_left], l[end]
    #p = sorted(l)
    #if l == p:
    #    return
    print " ".join(map(str, l))
    quickSort(l, start, size_left - 1)
    quickSort(l, size_left + 1, end)
