#создайте словарь, в котором ключами бутуд числа от 1 до 10, а значениями эти же числа, возведенный в куб

mainDict={}
mainList=[]
n=int(input("Ввдеите количество чисел массива: "))
def to_dict(list=[]):
    for elem in list:
        mainDict[elem]=elem**3
    return mainDict


for i in range(1, n+1):
    mainList.append(i)

print(to_dict(mainList))