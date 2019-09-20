for row in range(1, 10):
    for column in range(1, 10):
        if column >= row:
            print('{} X {} = {}'.format(row, column, row * column), end=' \t')
        else:
            print(' ', end=' \t')

    print(' ')
    #为啥我的99乘法表不是正常的格式呢？
    #DINGDINGDING修正版：
    for row in range(1, 10):
        for column in range(1, 10):
            if column >= row:
                print('{} X {} = {}'.format(row, column, row * column), end=' \t')
            else:
                print('          ', end=' \t')
                #就这个空格，符号和符号之间的空格是不作数的。但是，为什么老师只用了一个空格呢？为啥？
        print(' ')

for row2 in range(1,10):
    for column2 in range(1,10):
        if row2 >= column2:
            print('%sX%s=%s'%(row2, column2, row2 * column2), end=' ')
    print()
