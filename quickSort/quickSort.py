#An implementation of the QuickSort algorithm

def partition(array, l, r):
    print("partitioning ", array)
    p = array[l]
    i = l + 1
    for j in range(l+1, r):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i = i+1
    array[l], array[i-1] = array[i-1], array[l]
    print("partitioned ", array, p)
    print(array[:p], array[p+1:])
    return i

def quick_sort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)

        quick_sort(array, l, pivot - 1)
        quick_sort(array, pivot + 1, r)

def main():
    array = [3,8,1,5,2,4,7,6]
    # starting_array = [1,2,3,4,5,6,7,8]
    quick_sort(array, 0, len(array)-1)
    print(array)

if __name__ == '__main__':
    main()
