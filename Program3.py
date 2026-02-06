# Richard Perez

import heapq

array_1 = [
    [2, 5, 9, 21],
    [-1, 0, 2],
    [-10, 81, 121],
    [4, 6, 12, 20, 150]
]

array_2 = [
    [10, 17, 18, 21, 29],
    [-3, 0, 3, 7, 8, 11],
    [81, 88, 121, 131],
    [9, 11, 12, 19, 29]
]

array_3 = [
    [-4, -2, 0, 2, 7],
    [4, 6, 12, 14],
    [10, 15, 25],
    [5, 6, 10, 20, 24]
]

def merge_sort(arrays):
    result = []
    min_heap = []
    # pushing the elements on the heap
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))
    # removing the small indexes
    while min_heap:
        value, index, val_index = heapq.heappop(min_heap)
        result.append(value)
        # condition if more elements 
        if val_index + 1 < len(arrays[index]):
            successor = arrays[index][val_index + 1]
            heapq.heappush(min_heap, (successor, index, val_index + 1))

    return result

print("array 1:", merge_sort(array_1))
print("array 2: ", merge_sort(array_2))
print("array 3: ", merge_sort(array_3))