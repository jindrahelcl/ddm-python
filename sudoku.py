#n = int(input("cislo "))

# def fact(m):
#     faktorial = 1
#     for i in range(1, m + 1):
#         faktorial = faktorial * i
#     return faktorial


def factr(m):
    print("ahoj")
    if m == 1:
        print("prase")
        return 1
    return factr(m - 1) * m

def fibonaccir(m):
    if m == 1:
        return 1
    if m == 2:
        return 1
    return fibonaccir(m - 1) + fibonaccir(m - 2)

def fibonacci(m):
    if m == 1 or m == 2:
        return 1

    a = 1
    b = 1
    for i in range(3, m + 1):
        c = a + b
        a = b
        b = c

    return c


s = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def mozne_doplnit(i, j):
    cisla_v_sudoku = [True] * 9

    for ii in range(9):
        cislo = s[ii][j]
        if cislo != 0:
            cisla_v_sudoku[cislo - 1] = False

    for jj in range(9):
        cislo = s[i][jj]
        if cislo != 0:
            cisla_v_sudoku[cislo - 1] = False

    blok_i = (i // 3) * 3
    blok_j = (j // 3) * 3

    for ii in range(blok_i, blok_i + 3):
        for jj in range(blok_j, blok_j + 3):
            cislo = s[ii][jj]
            if cislo != 0:
                cisla_v_sudoku[cislo - 1] = False

    return cisla_v_sudoku

print(mozne_doplnit(0, 2))

