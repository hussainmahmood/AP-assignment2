def binary(arr, val):
    l = 0
    h = len(arr)-1
    while l <= h:
        m = l + (h - l)//2
        if arr[m] == val:
            return m

        if arr[m] < val:
            l = m + 1
        else:
            h = m - 1

    return None