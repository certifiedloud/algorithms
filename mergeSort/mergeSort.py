#An implementation of the merge sort algorithm

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

    if combinedLength < 3:
        if left[0] < right[0]:
            combined.append(left[0])
            combined.append(right[0])
            return combined
        else:
            combined.append(right[0])
            combined.append(left[0])
            return combined

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

my_array = [10,4,3,6,11,5,2,1,8,7,9]

sorted_array = merge_sort(my_array)

print("unsorted: ", my_array)
print("RESULT: ", sorted_array)
