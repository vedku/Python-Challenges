#a246
def binarysearch(target, arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            print("the target,",target,",was found at position:", mid)
            break
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    else:
        print("The target,", target, ",was not found in the list")


x = sorted([50, 77, 89, 82, 86, 83, 6, 3, 29])
#[3, 6, 29, 50, 77, 82, 83, 86, 89] when sorted
binarysearch(77,x)
binarysearch(99,x)
