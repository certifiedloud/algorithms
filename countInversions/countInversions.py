#An implementation of the merge sort algorithm that counts array inversions

def merge_sort_count(my_array):
    if(len(my_array) < 2):
        return my_array, 0

    else:
        left = my_array[:round(len(my_array)/2)]
        right = my_array[round(len(my_array)/2):]

        left_count, a = merge_sort_count(left)
        right_count, b = merge_sort_count(right)
        return merge(a,b)


def merge(left, right):
    #merge the two arrays
    #TODO refactor the return the count of inversions
    i=0
    j=0
    combined = []

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

#this array has 3 inversions
my_array = [1,3,5,2,4,6]
print("sorting and counting inversions")
inv_count = merge_sort_count(my_array)

print("This array should have 3 inversions, we found: ", inv_count)
