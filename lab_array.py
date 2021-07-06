
# ! 1. ให้เปิดNotepad พิมพ์ค่าต่อไปนี้แล้วsave เป็นชื่อdata.txt ให้อ่านข้อมูลจากไฟล์โดยแต่ละกําหนดindex เริ่มต้นเองให้สร้างfunctionชื่อว่าcreateมาเก็บในarray เพียง12 ค่าและแสดงค่า
# todo 34 24 3 66 47 18 8 26 55 82 29 32 17 6 72 27 23 9 44 12 60 89 10 57 46 54 7 33 95 56 77 22 51 19
class Array:
    def __init__(self, *arg):
        self.get_array = arg[0] if type(arg[0]) in(list ,tuple) else list(arg)
  
        
    #! Bubble sort method 
    @property
    def bubble_sort(self):
        for i in range(len(self.get_array)):
            for j in range(0,len(self.get_array)-1):
                if self.get_array[j] > self.get_array[j+1]: 
                    # todo Swap element 
                    here_ele,next_ele  = self.get_array[j],self.get_array[j+1]
                    self.get_array[j] = next_ele
                    self.get_array[j+1] = here_ele
    
    #! Insert Method
    def insert_ele(self,idx:int,ele):
        imp_array = self.get_array[idx::] 
        self.get_array = self.get_array[0:idx+1] 
        self.get_array[idx] = ele
        self.get_array = self.get_array+imp_array
    
    #! Delete Method
    def delete_ele(self, ele):
        self.get_array.remove(ele)
        
    #! Search Method
    def search_ele(self, ele, start=0):
        return self.get_array.index(ele, start, len(self.get_array)) 
    #! Min element
    @property
    def min_ele(self):
        self.bubble_sort
        return self.get_array[0] 
    #! Max element
    @property
    def max_ele(self):
        self.bubble_sort
        return self.get_array[len(self.get_array)-1]


if __name__ == '__main__':
    with open('data.txt','r') as f :
        get_lst = [int(i) for i in f.read().split(' ')[:12]]
        print('Unsort : {}'.format(get_lst))
        arr_var = Array(get_lst)
        arr_var.bubble_sort
        print('Sorted : {}'.format(get_lst))
    

