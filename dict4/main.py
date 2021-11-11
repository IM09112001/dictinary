#дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран

mainDict={
    'a':375,
    'b':567,
    'c':-37,
    'd':21
}
asd=1
for elem in mainDict.keys():
    asd*=mainDict[elem]
print(asd)
