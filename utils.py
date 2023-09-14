# def register(email: str, password: str):


def emil() -> str:
    while True:
        email = input("Введите логин: ")
        if "@" not in email:
            print("Email должен содержать '@'!")
            continue     
        

        dog = email.index("@") + 1
        services = ['gmail.com', 'mail.ru', 'yahoo.com']
        check = False
    
        for i in services:
            if i == email[dog:]:
                check = True
                break
        
        if check == False:
            continue
        else:
            break

    return email


def password():
    while True:
        pasword = input("Введите пароль: ")

        if len(pasword) < 8:
            print("Пароль должен содержать минимум 8 символов!")
            continue
        if pasword.islower() == True:
            print("Пароль должен содержать хотя одну заглавную букву")  
            continue
        if pasword.isupper() == True:
            print("Пароль должен содержать хотя одну строчную букву")    
            continue
        break
    return pasword



def register():
    email = emil()
    pasword = password()

    with open("data.txt", "a") as f:
        f.write(f"{email}: {pasword}" + '\n')
        

def login():

    with open("data.txt", "r+") as f:
        users = f.readlines()
        users = [user.replace("\n", "") for user in users]
    
    email = input("Введите ваш логин: ")
    pasword = input("Введите ваш пароль: ")

    user = f"{email}: {pasword}"

    if user in users:
        print("Вы вошли в свой аккаунт")
    else:
        print('Такого аккаунта не существует')




        













    



