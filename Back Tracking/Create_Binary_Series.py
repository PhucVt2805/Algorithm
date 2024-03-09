# Bài toán sinh ra mã nhị phân khác nhau có độ dài n
Length = int(input('Nhập độ dài xâu kí tự: '))
X = [-1] * Length
count = int(0)
def Try(i = 1):
    for j in range(2):
        X[i - 1] = j
        if(i == Length):
            print(X)
            count = count + 1
        else:
            Try(i + 1)
if __name__ == '__main__':
    Try()

