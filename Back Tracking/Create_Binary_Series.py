Length = int(input('Nhập độ dài xâu kí tự: '))
X = [-1] * Length

def Try(i = 0):
    for j in range(2):  # Sinh ra 0 và 1
        X[i] = j
        if i == Length - 1:
            print(X)
        else:
            Try(i + 1)

if __name__ == '__main__':
    Try()
