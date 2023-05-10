def solution(m, n, puddles):

    matrix = [[0 for j in range(m+1)] for i in range(n+1)]
    matrix[1][1] = 1

    for i, j in puddles:
        matrix[j][i] = -1 #웅덩이가 있는 곳은 -1로 표시

    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
                continue
            matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1]) % 1000000007

   
    return matrix[n][m]


print(solution(4,3,[[2,2]]))