def merge(arr):
    if len(arr) > 1:
        # break array into equal parts
        m = len(arr)//2
        l_arr = arr[:m]
        r_arr = arr[m:]

        # recursively sort each half
        merge(l_arr)
        merge(r_arr)
 
        i = j = k = 0
 
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1
 
        arr[k:k+(len(l_arr)-i)] = l_arr[i:]
        k += len(l_arr)-i
 
        arr[k:k+(len(r_arr)-j)] = r_arr[j:]
        k += len(r_arr)-j