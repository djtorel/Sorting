# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != cur_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


print(selection_sort([10, 4, 2, 9, 0, 3, 5, 1, 6]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                is_sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


print(bubble_sort([10, 4, 2, 9, 0, 3, 5, 1, 6]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
