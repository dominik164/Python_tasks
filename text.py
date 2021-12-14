import os

def delate():
    f = open('Greek.txt', "r").read()
    file = f.split(' ')
    print(file)
    words = ["Greek","Greek:" "and", "or", "never", "why"]
    for word in range (len(file),0,-1):
        if file[word-1] in words:
            file.remove(file[word-1])
    print(file)

def replacment():
    f = open('Africa.txt', "r").read()
    file = f.split(' ')
    print(file)
    words_dictonary = {'Africa': 'Europe', 'and': '&','never': 'always',
                       'why': 'WHY' ,'African' : 'European'}
    for word in range(len(file)):
        if file[word - 1] in words_dictonary.keys():
            file[word - 1] = words_dictonary.get(file[word - 1], word)
    print(file)
if __name__ == '__main__':
    delate()
    #replacment()