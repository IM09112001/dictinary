#Дан два словаря:
# dictinary_1={'a': 300, 'b': 400}
# dictinary_2={'c': 500, 'd': 600}
# Объединить их в один словарь

dictinary_1={
    'a': 300,
    'b': 400
}
dictinary_2={
    'c': 500,
    'd': 600
}


dictinary_1.update(dictinary_2)

print(dictinary_1)



