# Sinh tổ hợp chập K của N
N = int(input('Nhập giới hạn của dãy số: '))
Length = int(input('Nhập độ dài tổ hợp: '))

# Khởi tạo mảng X với các giá trị ban đầu từ 1 đến Length
X = [i for i in range(1, Length + 1)]

def Try(i):
    # i là chỉ số của phần tử hiện tại trong mảng X mà ta muốn cập nhật giá trị
    # Bắt đầu từ i = 0 cho phần tử đầu tiên trong tổ hợp
    for j in range(X[i - 1] if i > 0 else 1, N - Length + i + 2):
        X[i] = j
        if i == Length - 1:
            print(X)
        else:
            Try(i + 1)

if __name__ == '__main__':
    Try(0)
