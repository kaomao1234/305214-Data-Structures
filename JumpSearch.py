arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 610


def jumpSearch(arr, key):
    size = len(arr)  # todo วัดความยาวของ array
    jump_size = round(size**1/2)  # todo หาขั้นในแต่ละครั้ง
    last_step = 0  # todo เก็บค่าของ jump_size ในกรณีที่ arr[jumpsize] > key
    for i in range(0, size):
        step = i*(jump_size-1)  # todo คำนวณค่า step ในแต่ละ รอบ
        if step >= size:
            return -1
        # todo ถ้า step เท่ากับ key ส่งค่ากลับเป็น step(ตำแหน่งในarr)
        elif arr[step] == key:
            return step
        # todo เพิ่ม stepไปอีก step แล้วถ้า arr[step] > key กำหนดตัวแปร last_step เก็บค่า step
        elif arr[step+(jump_size-1)] > key:
            last_step = step
            break
    for j in range(last_step, size):
        # todo ทำการเทียบ arr[j] กับ key โดยเริ่มหาจากตำแหน่งที่ last_step ถึงตำแหน่งสุดท้าย
        if arr[j] == key:
            return j  # todo ส่งค่ากลับเป็น j(ตำแหน่งในarr)


# print(jumpSearch(arr, 620))
while score_in > 50:
    score_in = int(input())
print('end')
