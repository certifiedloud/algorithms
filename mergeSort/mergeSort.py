#An implementation of the merge sort algorithm
import random

def merge_sort(my_array):
    if(len(my_array) < 2):
        return my_array

    else:
        left = my_array[:round(len(my_array)/2)]
        right = my_array[round(len(my_array)/2):]

        a = merge_sort(left)
        b = merge_sort(right)
        return merge(a,b)


def merge(left, right):
    #merge the two arrays
    i=0
    j=0
    combined = []
    combinedLength = len(left) + len(right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i+=1
        else:
            combined.append(right[j])
            j+=1

    while i < len(left):
        combined.append(left[i])
        i += 1

    while j < len(right):
        combined.append(right[j])
        j += 1

    return combined

print("generating array")
my_array = list(range(1,800000))
print("randomizing array")
random.shuffle(my_array)
print("sorting array")
sorted_array = merge_sort(my_array)

print("unsorted: ", my_array)
print("RESULT: ", sorted_array)
