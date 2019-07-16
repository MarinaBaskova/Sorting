# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr

    count_arr = [0] * (max(arr)+1)
    sorted_arr = [None] * len(arr)

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count_arr[num] += 1
    
    for i in range(1,len(count_arr)):
        count_arr[i] = count_arr[i] + count_arr[i-1]
        
    for num in arr:
        sorted_arr[count_arr[num]-1] = num
        count_arr[num] -= 1
    return sorted_arr

