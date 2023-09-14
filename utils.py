# def register(email: str, password: str):


def login() -> str:
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
    email = login()
    pasword = password()
    

    










    



