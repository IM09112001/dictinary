#Даны 2 списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка
#были ключами, а элементы второго-соответсвено значениями нашего словаря


mainDict={}
mainList=[]
keyList=[]
n=int(input("Ввдеите количество чисел массива: "))

def to_dict(listKey=[], listValue=[]):
    for i in range(n):
        elemKey=listKey[i]
        mainDict[elemKey]=listValue[i]
    print(mainDict)


for i in range(n):
    elem=input("Введите элементы словаря: ")
    mainList.append(elem)


for i in range(n):
    elem=input("Введите ключи словаря: ")
    keyList.append(elem)



to_dict(keyList, mainList)
