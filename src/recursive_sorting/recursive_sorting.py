# TO-DO: complete the helper function below to merge 2 sorted lists
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # # TO-DO
    merged_list = []
    while len(arrA) > 0 and len(arrB) > 0:
        if(arrA[0] < arrB[0]):
            merged_list.append(arrA[0])
            # print(merged_list)
            arrA.pop(0)
        else:
            merged_list.append(arrB[0])
            arrB.pop(0)      
    if(len(arrA) == 0):
        left_list = arrB
    
    elif(len(arrB) == 0):
        left_list = arrA
    
    while len(left_list) > 0:
        merged_list.append(left_list[0])
        left_list.pop(0)
    
    return merged_list

print(merge([1,10,50], [2,14,99]))

##########################

########################
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0:
        return arr
    middle = len(arr) // 2    
    # start 0 end middle point 
    left_side = arr[0: middle] 
    # start middle +1 end len(arr)  
    right_side = arr[middle:] 
    left_result = merge_sort(left_side)
    right_result = merge_sort(right_side)         
   

    return merge(left_result,right_result)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
