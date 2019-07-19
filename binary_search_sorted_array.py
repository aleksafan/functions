def binary_search(arr, begin, end, el):
   
    if end>=begin:
        middle = begin+(end-begin)//2
        if el==arr[middle]:
            return middle
        elif el>arr[middle]:
            return binary_search(arr, middle+1, end, el)
        else:
            return binary_search(arr, begin, middle-1, el)

    else:
        return -1