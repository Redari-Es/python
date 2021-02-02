def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


nterms = int(input('您要输出几项？ '))

if nterms <= 0:
    print('请输入正数')
else:
    print('fibo数列: ')
    for i in range(nterms):
        print(recur_fibo(i))
