n = int(input("cislo "))

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



print(fibonacci(n))

s = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

