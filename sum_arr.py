def _sum(arr, n):
    return(sum(arr))


arr = []
arr = [12, 3, 4, 15]


# def num(x):
#    while x > 0:
#
#        num = int(input('输入需要计算得数：'))
#        arr.append(x)
#        continue
#    else:
#        print('计算结束')
#
#
# print(num)


n = len(arr)
ans = _sum(arr, n)
print('计算元素之和', ans)
print(n)
