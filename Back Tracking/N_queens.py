N = int(input('Nhập giá trị N để bắt đầu giải thuật: '))
X = []
used_col = [0] * N
main_diagonal = [0] * (2*N - 1)
secondary_diagonal = [0] * (2*N - 1)
for i in range(N):
    X.append([0]*N)

def Print_X(X):
    print(' ')
    for i in range(N):
        for j in range(N):
            if X[i][j]:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def Try(row=0):
    for col in range(N):
        if not (used_col[col] or main_diagonal[row - col + N - 1] or secondary_diagonal[row + col]):
            used_col[col] = main_diagonal[row - col + N - 1] = secondary_diagonal[row + col] = 1
            X[row][col] = 1
            if row + 1 == N:
                Print_X(X)
            else:
                Try(row + 1)
            used_col[col] = main_diagonal[row - col + N - 1] = secondary_diagonal[row + col] = 0
            X[row][col] = 0

if __name__=='__main__':
    Try()
