import math
import random
import socket

def isPrime(n, k):
  if n == 2 or n == 3:
      return True
  s, t = f(n - 1)
  flag = False
  for i in range(k):
      a = random.randint(2, n - 2)
      res = pow(a, t, n)
      if res == 1 or res == n - 1:
          break
      else:
        for j in range(s - 1):
          res = res * res % n
          if res == n - 1:
              flag = True
              break
        if flag == False:
            return False #Составное
  return True#вероятно простое

def f(n):
    s = 0
    while n % 2 == 0:
        s = s + 1
        n //= 2
    return s, n



def write_to_file(l, r, fileNameResult):
    with open(fileNameResult, "w+") as file:
        i = 0
        while i < len(l):
            s = r[i].split()
            if(l[i] == True):
                if len(s) > 1:
                    file.write(s[0] + "  " + s[1] + "  вероятно простое\n")
                else:
                    file.write(s[0] + "  вероятно простое\n")
            else:
                if len(s) > 1:
                    file.write(s[0] + "  " + s[1] + "  составное\n")
                else:
                    file.write(s[0] + "  составное\n")
            i += 1

def read_from_file(fileName):
    with open(fileName, "r+") as file:
        l = []
        res = []
        for text in file:
            l.append(text)
            s = text.split()
            if len(s) > 1:
                res.append(isPrime(int(s[0]), int(s[1])))
            else:
                res.append(isPrime(int(s[0]), int(math.log(int(s[0])))))
    return res,l

def pow(x1, y1, n):
    r = 1

    while y1 != 0:
        if y1 % 2 == 1:
            r = (r * x1) % n
        x1 = x1 * x1 % n
        y1 = y1 // 2
    return r


def start_server():
    sock = socket.socket()
    sock.bind(('localhost', 9090))
    sock.listen(1)
    connect, address = sock.accept()
    print("connected")
    while True:
        n = 0
        n = int.from_bytes(connect.recv(1024), byteorder='big')
        if not n:
            print("Выход из сервера")
            print()
            break
        _round = 0
        _round = int.from_bytes(connect.recv(1024), byteorder='big')

        res = isPrime(n, _round)
        res = str(res)
        connect.send(res.encode("utf-8"))
    connect.close()

while True:
    print("1 - ввод с консоли")
    print("2 - чтения из файла")
    print("3 - через сокет")
    print("0 - выход")
    print("Введите число от 0 до 4")
    case = int(input())
    if case == 1:
        print("Введите число для проверки на простоту")
        n = int(input())
        print("Хотите ли ввести количество раундов?(Да/Нет)")
        vibor = input()
        k = 0
        if vibor == "Да":
            print("Введите количество раундов")
            k = int(input())
        else:
            k = int(math.log(n))
        result = isPrime(n, k)
        if result == True:
            print(str(n) + " - вероятно простое")
        else:
            print(str(n) + " - составное")
        print()
    elif case == 2:
        print("Введите название файла")
        fileName = input()
        res, l = read_from_file(fileName)
        print("Введите название файла куда хотите записать результат")
        fileNameResult = input()
        write_to_file(res, l, fileNameResult)
        print("Результаты записаны в файл")
        print()
    elif case == 3:
        start_server()
    elif case == 0:
        print("Работа закончена")
        break;
    else:
        print("Неправильно введено число")
