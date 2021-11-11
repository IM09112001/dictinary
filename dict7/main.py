#Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки, а значениями
# пусть будут числа, соответствующие количеству вхождений данной буквы в строку

mainDict={}
checkList=[]
str1='pythonist'



for elem in str1:
    checkList.append(elem)
    mainDict[elem]=1
    for i in range(len(checkList)):
        if checkList[i]==elem:
            mainDict[elem]+=1
    mainDict[elem]-=1


print(mainDict)







