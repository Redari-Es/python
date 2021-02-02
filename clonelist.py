# 实例一
"""
def clone_redaries(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_redaries(li1)
print('原始列表：', li1)
print('复制列表：', li2)
"""

# 实例二

"""

def clone_redaries(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_redaries(li1)
print('原始列表：', li1)
print('复制列表：', li2)
"""
# 实例三


def clone_redaries(li1):
    li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_redaries(li1)
print('原始列表：', li1)
print('复制列表：', li2)
