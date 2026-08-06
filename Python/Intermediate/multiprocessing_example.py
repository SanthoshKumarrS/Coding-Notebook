from multiprocessing import Process,Lock,Value,Pool
import os,time

def add_100(number,lock):
    
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1
        

#if __name__ == '__main__':

   # lock = Lock()
   # shared_number = Value('i', 0)
   # print("shared number initial value is ",shared_number.value)

   # p1 = Process(target=add_100,args=(shared_number,lock))
   # p2 = Process(target=add_100,args=(shared_number,lock))

   # p1.start()
  #  p2.start()

  #  p1.join()
 #   p2.join()
#
#    print("final shared number value is ",shared_number.value)


#pool
def cube(x):
    return x**3

if __name__ == '__main__':

    numbers = range(15)
    pool = Pool()

    #map,apply,join,close
    results = pool.map(cube,numbers)
    
    pool.close()
    pool.join()

    print(results)