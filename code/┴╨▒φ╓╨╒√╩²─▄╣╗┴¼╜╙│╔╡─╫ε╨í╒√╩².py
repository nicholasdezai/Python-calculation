'''程序功能：   给定一个含有多个整数的列表，将这些整数任意组合和连接，   返回能得到的最小值。   代码思路：   将这些整数变为相同长度（按最大的进行统一），短的右侧使用个位数补齐，   然后将这些新的数字升序排列，补齐后一样大小的数字按原始数据降序排列，   排序后，将低位补齐的数字删掉，   把剩下的数字连接起来，即可得到满足要求的数字'''lst = [321, 30, 32, 300, 1, 3000, 3210, 3]print(lst)def mergeMinValue(lst):    # 生成字符串列表    lst = list(map(str, lst))    # 最长的数字长度    m = len(max(lst, key=len))    # 根据原来的整数得到新的列表，改造形式    newLst = [(i,i+i[-1]*(m-len(i))) for i in lst]    # 根据补齐的数字字符串进行排序    newLst.sort(key=lambda item:(item[1],-int(item[0])))    # 对原来的数字进行拼接    result = ''.join((item[0] for item in newLst))    # 返回结果    return int(result)print(mergeMinValue(lst))print(int(''.join(map(str,                      sorted(lst,                             key=lambda x: (str(x).ljust(max(map(lambda i: len(str(i)),                                                                 lst)),                                                         str(x)[0]),                                            -x)                             )                      )                  )          )      )from itertools import permutationsprint(min(map(lambda item:int(''.join(map(str,                                          item)                                      )                              ),              permutations(lst, len(lst))              )          )      )from functools import cmp_to_keyprint(int(''.join(sorted(map(str, lst),                         key=cmp_to_key(lambda x,y:int(x+y)-int(y+x))                         )                  )          )      )