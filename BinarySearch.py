Length = int(input('Nhập chiều dài của mảng: '))
arr = []
for i in range(Length):
    temp = int(input(f'Nhập phần tử thứ {i + 1} của mảng theo thứ tự tăng dần: '))
    arr.append(temp)
left = int(0)
right = Length - 1
element = int(input('Nhập số cần tìm kiếm: '))

def BinarySearch(left, right, element):
    center = int((right + left)/2)
    if left > right: return False
    print(f'Left = {left}, Right = {right}, Center = {center}')
    if(int(arr[center]) == element):
        return f'Phần tử cần tìm kiếm nằm ở vị trí thứ {center + 1} trong mảng đã nhập'
    elif(int(arr[center]) < element):
        return BinarySearch(center, right, element)
    else:
        return BinarySearch(left, center, element)

print(BinarySearch(left, right, element))
