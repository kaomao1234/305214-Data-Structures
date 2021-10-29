from threading import Thread
Thread(target=lambda : [print("1 =>",i) for i in range(1,10)]).start()
for i in range(1,10):
    print("2 == >",i)