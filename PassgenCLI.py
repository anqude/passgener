from pyperclip import copy# Для копирования в буфер обмена
from logics.entropy import get_entopy
from logics.qr import generate_qr_text
from logics.generate import alph_generate,pass_generate

soglasie=["yes","y","д","да"]
while True:
    try:
        lineal=int(input("Длина пароля: "))
        break
    except ValueError:
        print("Это должно быть число!")
while True:
    number=input("Использовать числа? [Д/н] ")
    letterB=input("Использовать большие буквы? [Д/н] ")
    letterS=input("Использовать маленькие буквы? [Д/н] ")  
    spec=input("Использовать спец символы? [Д/н] ")
    variables=[number.lower(),letterB.lower(),letterS.lower(),spec.lower()]

    for i in range(len(variables)):
        if variables[i] in soglasie:
            variables[i]=True
        else:  
            variables[i]=False 
    number,letterB,letterS,spec=variables[0],variables[1],variables[2],variables[3]
    if True in variables:
        break
    else:
        print("Пустой пароль!")  
password_lst=alph_generate(number,letterB,letterS,spec)
password=pass_generate(password_lst,lineal)
print(password)
entropy,state=get_entopy(password)
entropy_data=str(entropy)+" bits, "+state
print(entropy_data)
if(input("Скопировать в буфер обмена? [Д/н] ").lower() in soglasie) :
        copy(password)
else:
   pass
if(input("Создать QR код? [Д/н] ").lower() in soglasie) :
    generate_qr_text(password)
else:
   pass
    