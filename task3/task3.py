from io import StringIO
import csv


def task(csv_string):
    f = StringIO(csv_string)
    reader = csv.reader(f, delimiter=',')
    gp = []
    for row in reader:
        gp.append(row)

    r1, r2, r3, r4, r5 = {}, {}, {}, {}, {}

    for [i, j] in gp:
        r1[i] = True
        r2[j] = True

    for [l, r] in gp:
        for [i, j] in gp:
            if r == i:
                r3[l] = True
                r4[j] = True
            if (l == i) & (r != j):
                r5[r] = True

    return [list(r1.keys()), list(r2.keys()), list(r3.keys()), list(r4.keys()), list(r5.keys())]

# print(task("1,2\n1,3\n2,4"))
