def add_matrices(matrix1, matrix2):
    # 행렬의 크기를 맞추기 위해 0으로 채워진 행렬 생성
    result = [[0] * max(len(row1), len(row2)) for row1, row2 in zip(matrix1, matrix2)]

    # 같은 위치에 있는 요소들을 더하여 결과 행렬에 저장
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# 예시 비정방형 행렬
matrix1 = [[1, 2, 3],
           [4, 5, 5]]

matrix2 = [[6, 7],
           [8, 9, 10]]

# 덧셈 수행
result = add_matrices(matrix1, matrix2)

# 결과 출력
for row in result:
    print(row)
