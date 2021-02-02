def Selectionsort1():
    A = [-9, -8, 640, 25, 12, 22, 33, 45, 11, -2, -5, 99, 0]
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j

        A[i], A[min] = A[min], A[i]
    print('Selectionsort1排序后得数组：', A)


def Selectionsort2():
    A = [-9, -8, 640, 25, 12, 22, 33, 45, 11, -2, -5, 99, 0]
    counter = 0
    array = []

    for i in A:
        counter += 1
        for j in A[counter:]:
           if i > j:
                i = j
            A.remove(i)
            A.insert(counter - 1, i)
        array.append(i)
    print('Selectionsort2排序后数组：', array)

Selectionsort1()
Selectionsort2()
