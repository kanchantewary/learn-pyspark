import threading
import time

def calc_square(number):
    while True:
        print('square:',number*number)
        number+=number
        time.sleep(2)

def calc_quad(number):
    while True:
        print('quad:',number*number*number*number)
        number += number
        time.sleep(1)

if __name__ == '__main__':
    number = 1

thread1 = threading.Thread(target=calc_square, args=(number,))
thread2 = threading.Thread(target=calc_quad, args=(number,))

# execute both in parallel

thread1.start()
thread2.start()

# join threads back to the parent process

thread1.join()
thread2.join()

