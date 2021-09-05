
def trick(command):
    box = ['ball','','']
    for i in command:
        cup_one = box[0]
        cup_two = box[1]
        cup_three = box[2]
        print(box)
        if i == "A":
            box[0],box[1] = cup_two,cup_one
        elif i == "B":
            box[1],box[2] = cup_three,cup_two
        elif i == "C":
            box[0],box[2] = cup_three,cup_one
    print(box)
    if box.index('ball') ==0:
        return 1
    elif box.index('ball') ==1:
        return 2
    else:
        return 3
def trickRE(command:str,box=['ball',None,None],idx=0):
    if idx == len(command):
        if box.index('ball') ==0:
            return 1
        elif box.index('ball') ==1:
            return 2
        else:
            return 3
    else:
        cup_one = box[0]
        cup_two = box[1]
        cup_three = box[2]
        if command[idx] == "A":
            box[0],box[1] = cup_two,cup_one
        elif command[idx] == "B":
            box[1],box[2] = cup_three,cup_two
        elif command[idx] == "C":
            box[0],box[2] = cup_three,cup_one
    return trickRE(command,box,idx+1)

print(trickRE('AB'))