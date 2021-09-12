def delete(tmp:list,key,idx =0): 
    if idx == len(tmp):
        return
    if tmp[idx] == key:
        tmp[idx] = None
    else:
        delete(tmp,key,idx+1)
array = [1,6,7,1]
print(array)