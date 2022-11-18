def fib(num):
    if 0 <= num <= 1:
        return num
    return fib(num - 2) + fib(num - 1)

def main():
    while (True):
        print('Результат фибоначи: ' + str(fib(int(input('Напишите число: ')))))

if __name__ == '__main__':
    main()