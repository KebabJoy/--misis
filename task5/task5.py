from io import StringIO
import numpy as np
import json

SEQ_LEN = 10


def createRow(visited: set) -> np.array:
    row = []
    for i in range(SEQ_LEN):
        row.append(1 if i + 1 in visited else 0)
    return np.array(row)


def createMat(data: list) -> np.array:
    visited = set()
    matrix = list()

    for element in data:
        if type(element) == str:
            visited.add(int(element))
            row = createRow(visited=visited)
            matrix.append({'num': int(element), 'row': row})
        else:
            for subelement in element:
                visited.add(int(subelement))
            for subelement in element:
                row = createRow(visited=visited)
                matrix.append({'num': int(subelement), 'row': row})

    matrix.sort(key=(lambda x: x['num']))
    raw = [element['row'] for element in matrix]

    return np.array(raw)


def task(str1, str2) -> list:
    str1 = eval(str1)
    str2 = eval(str2)

    matrix1 = createMat(str1)
    matrix2 = createMat(str2)

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if not criterion[i][j]:
                answer.append([str(j + 1), str(i + 1)])

    return answer
