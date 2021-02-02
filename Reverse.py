# 实例一
'''

   def Reverse(lst):
       return [ele for ele in reversed(lst)]

    '''

# 实例二


'''
def Reverse(lst):
    lst.reverse()
    return lst

'''

# 实例三


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
