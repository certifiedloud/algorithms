#An implementation of the merge sort algorithm
from random import randint

def merge_sort(my_array):
    left = my_array[:round(len(my_array)/2)]
    right = my_array[round(len(my_array)/2):]
    print(left, right, my_array)

    if(len(left) < 2 or len(right) < 2):
        return merge(left, right)

    return merge_sort(left)
    return merge_sort(right)

def merge(left, right):
    #merge the two sorted arrays
    i=0
    j=0
    combined = []
    for k in range(len(left) + len(right)):
        if left[i] < right[j]:
            combined.insert(k, left[i])
            ++i
        elif right[j] < left[i]:
            combined.insert(k, right[j])
            ++j
    return combined


my_array = [4,3,6,5,1,2,8,7]

sorted_array = merge_sort(my_array)

print("RESULT: ", sorted_array)
