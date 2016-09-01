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

    for k in range(combinedLength):
        print(left, right, combined, i,j,k)
        if left[i] < right[j]:
            combined.append(left[i])
            i+=1
            if combinedLength <3:
                combined.append(right[j])
                break
        elif right[j] < left[i]:
            combined.append(right[j])
            j+=1
            if combinedLength <3:
                combined.append(left[i])
                break
    return combined

my_array = [4,3,6,5,1,2,8,7]

sorted_array = merge_sort(my_array)

print("RESULT: ", sorted_array)
