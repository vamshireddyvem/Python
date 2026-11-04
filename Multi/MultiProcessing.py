from multiprocessing import Process
from time import sleep,time
#this is a class approach  to get muti threading; here the class should in inherit thread class and it should have a run funcion and to run the function of thread we need call start for example refernce_variable.start()


def caluclate(n1,n2):
    sum=0
    for n in range(n1,n2):
        sum=+n*n
    return sum
if __name__ == '__main__':
    num=5000000
    mid=5000000//2
    start= time()
    result1=caluclate(0,mid)
    result2=caluclate(mid,num)
    result=result1+result2
    end=time()
    print(f'in series calculation time is  { end - start:.2f} seconds the result :{result}')
    start= time()
    t1=Process(target=caluclate,args=(0,mid))
    t2=Process(target=caluclate,args=(mid,num))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time()

    print(f'in parallel calculation time is  { end - start:.2f} seconds the result :{result}')



