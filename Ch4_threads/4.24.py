import threading

input_num = int(input("Enter a number: "))


def prime_numbers():
    for current_num in range(input_num + 1):
        if current_num > 1:
            for i in range(2, current_num):
                if (current_num % i) == 0:
                    break
            else:
                print(current_num)


t = threading.Thread(target=prime_numbers())
t.start()
