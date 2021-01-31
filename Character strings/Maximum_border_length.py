def maximum_border_length(w):
    n = len(w)
    f = [0] * n
    k = 0
    for i in range(1, n):
        while w[k] != w[i] and k > 0:
            k = f[k - 1]
        if w[k] == w[i]:
            k += 1
        f[i] = k
    return f
