def socrashenie(n1, n2):

    for i in range(min(abs(n1), abs(n2)), 2, -1):

        if n1 % i == 0 and n2 % i == 0:

            while n1 % i == 0 and n2 % i == 0:

                n1 /= i

                n2 /= i

    if n1 < 0 and n2 < 0:

        return str(abs(int(n1))) + '/' + str(abs(int(n2)))

    elif n1 * n2 < 0:

        return '-' + str(abs(int(n1))) + '/' + str(abs(int(n2)))

    else:

        return str(int(n1)) + '/' + str(int(n2))



def opredelitel_1_poryadka(mat_1_poryadka):

    return mat_1_poryadka[0][0]



def opredelitel_2_poryadka(mat_2_poryadka):

    return mat_2_poryadka[0][0] * mat_2_poryadka[1][1] - mat_2_poryadka[0][1] * mat_2_poryadka[1][0]



def opredelitel_3_poryadka(mat_3_poryadka):

    ''' Определитель считаестся через вычеркивание

    тк есть функция для определения второго порядка'''



    opredelitel_3 = 0

    i = 0



    for j in range(3):

        mat_new = mat_3_poryadka.copy()

        del mat_new[i]



        for num in range(len(mat_new)):

            mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]



        opredelitel_3 += (-1)**(i + j + 2) * mat_3_poryadka[i][j] * opredelitel_2_poryadka(mat_new)



    return opredelitel_3





def opredelitel_4_poryadka(mat_4_poryadka):

    opredelitel_4 = 0

    i = 0



    for j in range(4):

        mat_new = mat_4_poryadka.copy()

        del mat_new[i]



        for num in range(len(mat_new)):

            mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]



        opredelitel_4 += (-1) ** (i + j + 2) * mat_4_poryadka[i][j] * opredelitel_3_poryadka(mat_new)



    return opredelitel_4







def prisoed_mat(lybaya_mat, poryadok):  # Сначала передаем матрицу, потом ее порядок



    listwow = {1: opredelitel_1_poryadka, 2: opredelitel_2_poryadka, 3: opredelitel_3_poryadka, 4: opredelitel_4_poryadka}



    d = [[]]

    itog = [[]]



    for i in range(poryadok):

        for j in range(poryadok):

            element_new = 0

            mat_new = lybaya_mat.copy()

            del mat_new[i]



            for num in range(len(mat_new)):

                mat_new[num] = mat_new[num][:j] + mat_new[num][j + 1:]



            element_new += (-1) ** (i + j + 2) * listwow[poryadok - 1](mat_new)



            d[-1].append(element_new)

        d.append([])



    for i in range(len(d[:len(d) - 1])):



        for j in range(len(d[:len(d) - 1][i])):

            itog[-1].append(d[j][i])



        itog.append([])



    return itog[:len(itog) - 1]



import numpy as np
def fib(n):
    if n < 2 and n > -2:
        return n
    negative = False
    if n < 0:
        negative = True
        n = abs(n)

    A = np.matrix([[0,1],[1,1]], dtype=object)
    Ap = pow(A, n-1)
    result = Ap * np.matrix([[0],[1]])
    if negative and (abs(n)+1) % 2 != 0:
        return int(-result[1])
    else:
        return int(result[1])
