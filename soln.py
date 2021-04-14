def replacer(dataset):
    import numpy as np
    ar = np.array(dataset, dtype=float)
    ar = ar.transpose()
    means = []
    stdevs = []
    for row in ar:
        zero_exists = False
        sum_ele = []
        for e in row:
            if e != 0:
                sum_ele.append(e)
        mean = sum(sum_ele) / len(sum_ele)
        means.append(mean)
        for i, e in enumerate(row):
            if e == 0:
                zero_exists = True
                row[i] = mean

        if not zero_exists:
            stdevs.append(np.std(row, ddof=1))
        else:
            stdevs.append(np.std(row))

    for i, r in enumerate(ar):
        for j, e in enumerate(r):
            r[j] = (r[j] - means[j])
            k = r[j]/stdevs[j]
            ar[i][j] = k

    return ar.transpose()


if __name__ == '__main__':
    print(replacer([[1, 2, 0], [0, 1, 1], [5, 6, 5]]))
