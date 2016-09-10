#An implementation of the QuickSort algorithm

def choose_pivot(array):
    #naively choose the first element in the array
    return 0

def partition(array, pivot_index):
    left = array[:pivot_index]
    right = array[pivot_index:]
    i = left + 1
    p = array[left]
    for j in range(i, right):
        if array[j] < p:
            array.insert(p - 1, array.pop(j))
            array[j], array[i] = array[i], array[j]
            ++i

    array[left], array[i - 1] = array[i - 1], array[left]

def quick_sort(starting_array):
    if len(starting_array) == 1:
        return starting_array

    pivot_index = choose_pivot(starting_array)

    partition(starting_array, pivot_index)

    quick_sort(starting_array[:pivot_index - 1])
    quick_sort(starting_array[pivot_index + 1:])

    return starting_array

def main():
    starting_array = [3,8,2,5,1,4,7,6]
    sorted_array = quick_sort(starting_array)
    print(sorted_array)

if __name__ == '__main__':
    main()
