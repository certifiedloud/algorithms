#An implementation of the merge sort algorithm that also counts array inversions

def merge_and_count(my_array):
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
    for k in range(combinedLength):
        if left[i] < right[j]:
            combined.insert(k, left[i])
            if combinedLength == 2:
                combined.insert(k+1, right[j])
                break
            ++i
        else:
            combined.insert(k, right[j])
            if combinedLength == 2:
                combined.insert(k+1, left[i])
                break
            ++j
    print(combined)
    return combined

my_array = [4,3,6,5,1,2,8,7]

sorted_array = merge_and_count(my_array)

print("RESULT: ", sorted_array)
