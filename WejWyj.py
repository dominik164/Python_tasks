# ! /usr/bin/env python         shebang
#print ("Hello World!")


def hello():
    print("Hello")


def input_data():
    imie, nazwisko, data = input("Insert your name").split()
    print(data)


def lock():
    print("Insert password: ")
    passwd = int(input())
    print("Insert password: ")
    temp = int(input())
    if (temp == passwd):
        print("OK")
    else:
        print("Eror")


if __name__ == "__main__":
    # hello()
    # input_data()
    lock()
