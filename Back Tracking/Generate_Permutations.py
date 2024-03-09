# Sinh hoán vị của N phần tử
Length = int(input('Nhập số phần tử: '))
used = [0] * Length
X = [0] * Length

def Try(i = 1):
    for j in range(Length):
        if used[j] == 0:
            used[j] = 1
            X[i-1] = j + 1
            if i == Length:
                print(X)
            else:
                Try(i + 1)
            used[j] = 0
if __name__ == '__main__':
    Try()

