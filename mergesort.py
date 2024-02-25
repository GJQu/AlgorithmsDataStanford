def mergesort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
    else:
         return arr
    
    left = arr[:middle]
    right = arr[middle:]

    mergesort(left)
    mergesort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [3,8,2,14,9,7,91,42,43,54]
    print("Given array is", end="\n")
    printList(arr)
    mergesort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)