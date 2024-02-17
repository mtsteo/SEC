from urllib.request import urlopen
import hashlib


sha256hash = input("[+] Enter sha256 Hash value: ")

try:
     with open('10-million-password-list-top-1000000.txt', 'r', encoding='utf-8') as file:
         
        password_list = file.read().splitlines()
        for password in password_list:
            guess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
            if guess == sha256hash:
                print("[+] The password is: " + str(password))
                break
            elif guess != sha256hash:
                print(f"{guess}")
                continue
            else:
                print("The password does not matched in the list…")
except Exception as exc:
    print('There was a problem: %s' % (exc))
