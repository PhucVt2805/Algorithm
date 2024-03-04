Length = int(input('Nhập chiều dài của mảng: '))
arr = []
for i in range(Length):
    temp = int(input(f'Nhập phần tử thứ {i + 1} của mảng (không theo thứ tự): '))
    arr.append(temp)
left = int(0)
right = len(arr) - 1

def swap(array ,a, b):
    array[a], array[b] = array[b], array[a]

def partition(array, left, right):
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, left, i - 1)
    return i - 1

def QuickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        QuickSort(array, left, p - 1)
        QuickSort(array, p + 1, right)

QuickSort(arr, 0, len(arr) - 1)
print(arr)