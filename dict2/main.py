#создайте словарь с количеством элементов не менее 5-ти.
# поменяйте местами первый и последний элемент.
# добавте в конец ключ "new_key" со значением "new_value".
# вывудите на печать итоговый словарь. важно, чтобы словарь остался тем же

mainDict={
    'first':'first elem',
    'a': 'qwer',
    'b':'book',
    'c':'colour',
    'd': 'dark',
    'e':'elephant',
    'f':'fruit',
    'last':12345
}
#changing first and last
changeElem=mainDict['first']
mainDict['first']=mainDict['last']
mainDict['last']=changeElem
#

#deliting second elem
del mainDict['a']
#

#add new_key:value
mainDict['new_key']='new_value'
#
print(mainDict)
