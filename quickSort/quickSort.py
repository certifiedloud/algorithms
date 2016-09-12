#An implementation of the QuickSort algorithm

def partition(array, l, r):
    print("partitioning ", array)
    p = array[l]
    i = l + 1
    print(p,i,l,r)
    for j in range(l+1, r):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i = i+1
    array[l], array[i-1] = array[i-1], array[l]
    print("partitioned ", array, p)
    return i

def quick_sort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)

        quick_sort(array, l, pivot - 1)
        quick_sort(array, pivot, r)

def main():
    array = [3,8,1,5,2,4,7,6]
    # array = [1,2,3,4,5,6,7,8]
    quick_sort(array, 0, len(array))
    print("Finished ",array)

if __name__ == '__main__':
    main()
