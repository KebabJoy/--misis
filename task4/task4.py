import pandas as pd
import numpy as np

from collections import defaultdict
from queue import SimpleQueue
import math


def findR1AndR2(gp: dict, A: np.array) -> dict:
    for row in A:
        gp[row[0]][0] += 1
        gp[row[1]][1] += 1
    return gp


def findR1to4(gp: dict, A: np.array) -> dict:
    for row in A:
        main = row[0]
        sub = row[1]
        gp[main][0] += 1
        gp[sub][1] += 1
        for subrow in A:
            if subrow[0] == sub:
                gp[main][2] += 1
                gp[subrow[1]][3] += 1
    return gp


def findR5(d: dict, A: np.array) -> dict:
    q = SimpleQueue()
    q.put(1)

    r5 = {}

    while not q.empty():
        main = q.get()
        gp = []
        for row in A:
            if row[0] == main:
                gp.append(row[1])
                q.put(row[1])
        if len(gp) > 1:
            for elem in gp:
                d[elem][4] += gp.__len__() - 1

    return d


def entropyCalc(graph: np.array) -> float:
    def set_def():
        return [0, 0, 0, 0, 0]

    gp = defaultdict(set_def)

    findR1to4(gp, graph)
    findR5(gp, graph)

    gp = pd.DataFrame(gp)
    gp = gp.to_numpy().T
    n = len(gp)

    s = 0.0
    for elem in gp:
        for cond in elem:
            if cond > 0:
                p = cond / (n - 1)
                logp = math.log10(p)
                s += p * logp

    return -s


def pipeline(path):
    csv = pd.read_csv(path).to_numpy()
    entr = entropyCalc(csv)
    print(f"Энтропия: {entr:.4f} \n")


filename = "task4.csv"
pipeline(filename)
