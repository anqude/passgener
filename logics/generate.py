from secrets import choice # Для безопасной генерации пароля
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lettersB=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
lettersS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]
special=[ "!", "@", "№", "#", "$", "%", "^", "|", "&", "*", "_", "-", "=", "+", "-", "/", "(", ")", "?", "{", "}", "[", "]", "~", ">", "<", "." ]

def alph_generate(number,letterB,letterS,spec):
    password_lst=[] # Создаём алфавит пароля
    if number==True:
        password_lst+=numbers
    if letterB==True:
        password_lst+=lettersB
    if letterS==True:
        password_lst+=lettersS
    if spec==True:
        password_lst+=special
    return password_lst   
              
def pass_generate(password_lst,lineal):
    password=[] # Создаём непосредственно пароль
    for i in range(lineal):
        password.append(choice(password_lst))
    password=''.join(password)
    return password