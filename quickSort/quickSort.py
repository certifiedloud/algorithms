#An implementation of the QuickSort algorithm

def partition(array, l, r):
    # print("partitioning ", array)
    p = array[l]
    i = l + 1
    comps = 0
    # print(p,i,l,r)
    for j in range(l+1, r):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i = i+1
        comps += 1
    array[l], array[i-1] = array[i-1], array[l]
    # print("partitioned ", array, p)
    return i, comps

def quick_sort(array, l, r):
    comps = 0
    if l < r:
        choose_pivot(array,l,r)
        pivot, comps = partition(array, l, r)

        comps += quick_sort(array, l, pivot - 1)
        comps += quick_sort(array, pivot, r)
    return comps

def choose_pivot(array,l,r):
    if len(array) % 2 != 0:
        middle = array[len(array)/2-1]
    elif len(array) % 2 == 0:
        middle = array[len(array)/2]
    first = array[0]
    last = array[len(array)-1]
    the_three = [first, middle, last]
    the_three.sort()
    p = the_three[1]
    array[l], array[array.index(p)] = array[array.index(p)], array[l]


def main():
    # array = [3,8,1,5,2,4,7,6]
    # array = [1,2,3,4,5,6,7,8]
    with open('array.txt') as f:
        string_array = f.read().splitlines()
    array = [int(i) for i in string_array]
    print(quick_sort(array, 0, len(array)))
    # print("Finished ",array)

if __name__ == '__main__':
    main()
