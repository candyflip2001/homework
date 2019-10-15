def select_sort(array) :
    print("Unsorted array:\n",array)
    select_array = array.copy()
    for i in range(0, len(select_array) - 1) :
        min = i
        for k in range(i+1, len(select_array)) :
          if select_array[min] > select_array[k] :
              min = k
        temp = select_array[i] 
        select_array[i] = select_array[min]
        select_array[min] = temp
    return  select_array


def insertion_sort(array) : 
    print("Unsorted array:\n", array)
    insert_array = array.copy()
    for i in range(1, len(insert_array)) :
        j = i
        while(j > 0 and insert_array[j-1] > insert_array[j]) :
            temp = insert_array[j-1]
            insert_array[j-1] = insert_array[j]
            insert_array[j] = temp
            j -=1     
    return insert_array


def bubble_sort(array) :
    print("Unsorted array:\n", array)
    bubble_array = array.copy()
    for i in range (0, len(bubble_array)-1) :
        for k in range (len(bubble_array) - 1, i, -1) :
            if bubble_array[k] < bubble_array[k-1] :
                temp = bubble_array[k-1]
                bubble_array[k-1] = bubble_array[k]
                bubble_array[k] = temp
    return bubble_array


bubble_array = [537, 43, 238, 725, 885, 537, 726, 517, 67, 616, 85, 109, 803, 591, 734]
insert_array = [695, 153, 974, 815, 409, 351, 263, 637, 648, 61, 396, 276, 994, 659, 769]
select_array = [485, 558, 110, 793, 131, 301, 952, 255, 787, 625, 549, 5, 746, 492, 395]
divide_line = "__________________________________________________________________________"
print("Sorting by selection")
print("After sorting by selection:\n", select_sort(select_array),"\n", divide_line)
print("Insertion sorting")
print("After insertion sorting:\n", insertion_sort(insert_array),"\n", divide_line)
print("Bubble sorting")
print("After bubble sorting:\n", bubble_sort(bubble_array),"\n", divide_line)
