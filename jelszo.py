import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

while 1:
    password_len = int(input("Milyen hosszú jelszót kérsz : "))
    password_count = int(input("Hány darab jelszót szeretnél : "))
    for x in range(0,password_count):
        password  = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Itt az általad kért jelszó(k) : ", password)