import multiprocessing

def calc_square(number):
    print('square:',number*number)

def calc_quad(number):
    print('quad:',number*number*number*number)

if __name__ == '__main__':
    number = 7

p1 = multiprocessing.Process(target=calc_square, args=(number,))
p2 = multiprocessing.Process(target=calc_quad, args=(number,))

# execute both in parallel

p1.start()
p2.start()

# join threads back to the parent process

p1.join()
p2.join()

