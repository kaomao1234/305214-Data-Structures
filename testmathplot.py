def insert(idx:int,ele,lst:list):
    imp_var = lst[idx:]
    lst = lst[:idx]
    lst.append(ele)
    lst = lst+imp_var
    return lst
p = []
print(insert(0,2,p))
