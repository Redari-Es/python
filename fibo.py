# 获取用户输入数据
nterms = int(input("你需要几项? "))

n1 = 0
n2 = 1
count = 2

# 判断输入值是否合法
if nterms <= 0:
    print('请输入一个正整数。')
elif nterms == 1:
    print('fibo: ')
    print(n1)
else:
    print("fibo: ")
    print(n1, ',', n2, end=',')
    while count < nterms:
        nth = n1 + n2
        print(nth, end=',')
        # 更新值
        n1 = n2
        n2 = nth
        count += 1

