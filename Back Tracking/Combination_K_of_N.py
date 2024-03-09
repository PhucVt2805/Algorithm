# Sinh tổ hợp chập K của N
N = int(input('Nhập giới hạn của dãy số: '))
Length = int(input('Nhập độ dài tổ hợp: '))
X = [1] * Length
def Try(i = 1):
    for j in range(X[i - 1] + 1, N - Length + i + 2):
        X[i] = j
        if(i == Length - 1):
            print(X)
        else:
            Try(i+1)
if __name__ == '__main__':
    Try()