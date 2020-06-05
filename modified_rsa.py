import time 
import sys

#Checking whether the user input is prime number or composite number. 
def check_prime(number):
    counter = 0
    for divider in range(1,number+1):
        remainder = number % divider
        if remainder == 0:
            counter += 1
    return counter


#Selecting First prime Number(p)
def first_prime():
    print('**********    FIRST PRIME NUMBER SELECTION *********\n')
    while True:
        try:
            p = int(input("\nSelect first large random prime number: "))
            no_of_divider = check_prime(p)
            if no_of_divider == 2:
                print(f"Congratulation, {p} is a prime number.\n")
                return p
                break
            else:
                print(f"Sorry, {p} is composite Number.\nTry Again...\n")
        except:
            print('Invalid Input. Try Again !!!')

#Selecting Second Prime Number(q)
def second_prime():
    print('*************    SECOND PRIME NUMBER SELECTION    ****************\n')
    while True:
        try:
            q = int(input("Select second large random prime number: "))
            no_of_divider = check_prime(q)
            if no_of_divider == 2:
                print(f'Congratulation Again, {q} is a prime Number.\n')
                time.sleep(1)
                return q
                break
            else:
                print(f'Sorry, {q} is a composite Number.\nTry Again...\n')
        except:
            print("Invalid Input. Try Again !!!")

    
#Selecting third Prime Number(q)
def third_prime():
    print('*************    THIRD PRIME NUMBER SELECTION    ****************\n')
    while True:
        try:
            r = int(input("Select third large random prime number: "))
            no_of_divider = check_prime(r)
            if no_of_divider == 2:
                print(f'Congratulation Again, {r} is a prime Number.\n')
                time.sleep(1)
                return r
                break
            else:
                print(f'Sorry, {r} is a composite Number.\nTry Again...\n')
        except:
            print("Invaid Input. Try Again !!!")



#Selecting public key(e) For Data Encryption
def select_public_key():

    print("*********    PUBLIC KEY SELECTION    ************")
    print("Conditions : ")
    print(f'     [1] : 1 < e < phi_n i.e. 1 < e < {phi_n}')
    print(f'     [2] : gcd(e , phi_n) = 1.\n') #gcd = greatest common divisor
    while True:
        try:
            e = int(input('Select value of \"e\" in the given range:'))
            if e > 1 and e < phi_n:
                no_of_divider = check_prime(e)

                if no_of_divider == 2:
                    print(f'public key (f) : {(e * 2) + 1}\n')
                    return e
                    break
                else:
                    print(f'gcd({e} , {phi_n}) != 1.\nTry Again...')
                    continue

            else:
                print(f'Please, Select Pubic Key in Range 1 < e < {phi_n}')
                continue
        except:
            print('Please, Use Integer as Public key.')
            continue



#Calculating Private Key For Data Encryption.
def private_key_selection():
    for k in range(0,200):
        d = (1 + k * phi_n) / e
        if d.is_integer():
            time.sleep(1)
            print('Please Wait !!! Generating private key.')
            time.sleep(1)
            print('\n')
            print(f'Private Key (d) : {int(d)}\n')
            return int(d)
            break



#Encrypting / Decrypting Data According to user Choice
def encrypt_decrypt():
    while True:
        try:
            time.sleep(1)
            print('**********     WELCOME TO ENCRYPTION / DECRYPTION PHASE     ************\n')
            time.sleep(0.6)
            print('Press 1 for Encryption.\nPress 2 for Decryption.\nPress 3 to exit program\n')
            time.sleep(0.6)
            user_choice = input('Enter Your Choice : ')
            print(f"User Choice : {user_choice}\n")

            if user_choice == '1':
                plain_text = int(input('Enter Plain text For Encryption: '))
                print('\n')
                time.sleep(1)
                print('Please Wait !!! Generating Cipher Text...\n')
                time.sleep(1)
                cipher_text = (plain_text ** int((f-1)/2)) % (z+10)
                # print(int(cipher_text))
                # cipher_text = int(cipher_text)
                print (f"Cipher Text : {int(cipher_text)}\n")


            if user_choice == '2':
                cipher_text = int(input("Enter Cipher Text for Decryption : "))
                print('\n')
                plain_text = (cipher_text ** d) % (z+10)
                print(f"Plain Text : {plain_text}\n")

            if user_choice == '3':
                print('Please Wait...')
                time.sleep(1.4)
                print('Program Ended Successfully.')
                break

        except:
            print('Invalid Input..\n')
            continue





#Main Method for executing all the created functions.
def final():
    print('************     KEEP YOUR SYSTEM SECURE. ENCRYPT YOUR DATA WITH RSA     *************\n')
    global p, q, r, n, z, phi_n, e, f, d 
    p = first_prime()
    q = second_prime()
    r = third_prime()
    n = p * q * r
    print (f"The value of n is : [n = {n}]\n")
    z = n - 10
    print(f"The value of \"z\" is [z = {z}] \n")
    phi_n  = (p-1) * (q-1) * (r-1)
    print(f"The value of phi_n is : [phi_n = {phi_n}]\n")
    e = select_public_key()
    print (f"The value of e is [e = {e}]\n")
    f = (e * 2) + 1
    print(f"The value of f is : [f = {f}]\n")
    d = private_key_selection()
    print(f"The value of d is [d = {d}]\n")
    encrypt_decrypt()

final()




