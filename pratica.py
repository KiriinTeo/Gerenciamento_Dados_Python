def numeroDePares(a, b):
    qtde = 0
    '''a = [10, 4, 4, 9, 1, 0, 2, 2, 8, 5, 3, 9, 4, 6, 7]
    b = [9, 3, 3, 7, 0, 0, 9, 2, 10, 8, 2, 1, 5, 4, 6]'''
    used_a = set()
    used_b = set()
    pairs = []

    for i in range(len(a)):
        if a[i] > b[i] and a[i] not in used_a and b[i] not in used_b:
            pairs.append((a[i], b[i]))
            used_a.add(a[i])
            used_b.add(b[i])
            qtde += 1

    return qtde, pairs

if __name__ == "__main__":
    print(numeroDePares([], []))
