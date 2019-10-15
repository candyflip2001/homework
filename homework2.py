from datetime import datetime


#Merger sorting
def merger_array(array) :
    if len(array) < 2 :
        return array
    mid = int(len(array) / 2)
    left_part = merger_array(array[:mid])
    right_part = merger_array(array[mid:])
    return merger(left_part, right_part)

def merger(left_part, right_part) :
    result_array = []
    while len(left_part) > 0 and len(right_part) > 0 :
        if left_part[0] <= right_part[0] :
            result_array.append(left_part[0])
            left_part = left_part[1:] 
        else :
            result_array.append(right_part[0])
            right_part = right_part[1:]
    if len(left_part) > 0 :
        result_array += left_part;
    elif len(right_part) > 0 :
        result_array += right_part;
    return result_array


# Heap sorting
def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


def heap_sort(array):  
    n = len(array)
    array_copy = array.copy();
    for i in range(n, -1, -1):
        heapify(array_copy, n, i)
    for i in range(n - 1, 0, -1):
        array_copy[i], array_copy[0] = array_copy[0], array_copy[i]
        heapify(array_copy, i, 0)  
    return array_copy;


#Quick sorting
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
        return array
    return _quicksort(array, begin, end)


array = [9, 4, 4, 0, 4, 7, 3, 6, 5, 3, 4, 7, 5, 1, 2]
print("Merger sorting\n")
start_time = datetime.now()
print(merger_array(array))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
print("Heap sorting\n")
start_time = datetime.now()
print(heap_sort(array))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
print("Quick sorting\n")
print(quicksort(array))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
