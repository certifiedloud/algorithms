#An implementation of the merge sort algorithm that counts array inversions

def merge_sort_count(my_array):
    if(len(my_array) < 2):
        return my_array, 0

    else:
        left = my_array[:round(len(my_array)/2)]
        right = my_array[round(len(my_array)/2):]

        a, left_count = merge_sort_count(left)
        b, right_count = merge_sort_count(right)
        sorted_array, inv_count =  merge(a,b)
        return sorted_array, inv_count + left_count + right_count


def merge(left, right):
    #merge the two arrays and count inversions
    i=0
    j=0
    inversion_count = 0
    combined = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i+=1
        else:
            #increment the amount of split inversion found
            inversion_count += len(left) - i
            combined.append(right[j])
            j+=1


    while i < len(left):
        combined.append(left[i])
        i += 1

    while j < len(right):
        combined.append(right[j])
        j += 1

    return combined, inversion_count

#this array has 3 inversions
my_array = [1,3,5,2,4,6] # 3
print("sorting and counting inversions")
sorted_array, inv_count = merge_sort_count(my_array)

print("Found inversions ", inv_count)
