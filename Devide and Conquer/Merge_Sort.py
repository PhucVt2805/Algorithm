Length = int(input('Nhập chiều dài của mảng: '))
arr = []
for i in range(Length):
    temp = int(input(f'Nhập phần tử thứ {i + 1} của mảng (không theo thứ tự): '))
    arr.append(temp)
TempArr = [0] * Length

def MergeSort(array, left, right, TempArr):
    if left < right:
        mid = (left + right) // 2
        MergeSort(array, left, mid, TempArr)
        MergeSort(array, mid + 1, right, TempArr)
        Merge(array, left, mid, right, TempArr)

def Merge(array, left, mid, right, TempArr):
    for i in range(left, right + 1):
        TempArr[i] = array[i]

    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if TempArr[i] <= TempArr[j]:
            array[k] = TempArr[i]
            i += 1
        else:
            array[k] = TempArr[j]
            j += 1
        k += 1

    while i <= mid:
        array[k] = TempArr[i]
        i += 1
        k += 1

    while j <= right:
        array[k] = TempArr[j]
        j += 1
        k += 1

MergeSort(arr, 0, Length - 1, TempArr)
print(arr)