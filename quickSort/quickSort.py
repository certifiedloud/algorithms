#An implementation of the QuickSort algorithm

def choose_pivot(array):
    #naively choose the first element in the array
    return array[0]

def partition(array, l, r):
    p = choose_pivot(array)
    i = l + 1
    for j in range(l+1, r):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i = i+1
    array[l], array[i-1] = array[i-1], array[l]

def quick_sort(starting_array):
    if len(starting_array) == 1:
        return starting_array


    partition(starting_array, 0, len(starting_array)-1)

    # quick_sort(starting_array[:pivot_index - 1])
    # quick_sort(starting_array[pivot_index + 1:])

    return starting_array

def main():
    starting_array = [3,8,2,5,1,4,7,6]
    sorted_array = quick_sort(starting_array)
    print(sorted_array)

if __name__ == '__main__':
    main()
