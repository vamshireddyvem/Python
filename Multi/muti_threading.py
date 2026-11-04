from threading import Thread
from time import sleep,time
#this is a class approach  to get muti threading; here the class should in inherit thread class and it should have a run funcion and to run the function of thread we need call start for example refernce_variable.start()
class A(Thread):
    def run(self):
        for i in range(5):
            print('Hi.....',i)
            sleep(0.3)

class B(Thread):
    def run(self):
        for i in range(5):
            print('Hello.....',i)
            sleep(0.3)


files=['png','mp3','mp4','jpeg','pdf','docx','csv']

def download(filename):
    print('file downloading.....', filename)
    sleep(0.3)
    print('Download Complete..!')


start=time()
for f in files:
    download(f)
end=time()

print(f'in series the download time is  { end - start:.2f} seconds')

# this is a functional based approach (python way): where an object of Thread has function as its parameter target as function
thread=[]
start1=time()
for f in files:
    t=Thread(target=download, args=(f,))
    thread.append(t)

for t in thread:
    t.start()

for t in thread:
    t.join()
end1=time()

print(f'in parallel the download time is {end1-start1:.2f} seconds')

obj1=A()
sleep(0.1)
obj2=B()
obj1.start()
obj2.start()

