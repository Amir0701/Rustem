import socket as sock
import math

socket = sock.socket()
socket.connect(('localhost', 9090))
while True:
    print('Чтобы выйти введите - exit\n'
          'Введите число для проверки на простоту:')
    x = input()
    if x == "exit":
        print("Клиент вышел")
        break
    x = int(x)
    print("Хотите ли ввести количество раундов?(Да/Нет)")
    answer = input()
    _round = 0
    if answer == "Да":
        _round = int(input())
    else:
        _round = int(math.log(x))
    socket.send(x.to_bytes(1024, byteorder="big"))
    socket.send(_round.to_bytes(1024, byteorder='big'))
    res = socket.recv(1024).decode("utf-8")
    if(res == "True"):
         print(f'{x} - вероятно простое')
    else:
        print(f' {x} - составное')
    print()
socket.close()