def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input)-d]
    Rsecond = input[len(input)-d:]

    print('头部切片反转：', (Lsecond + Lfirst))
    print('尾部切片反转：', (Rsecond + Rfirst))


if __name__ == "__main__":

    input = 'redaries'
    d = 2
    rotate(input, d)

