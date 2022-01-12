import bcrypt

password = b"Getlostcovid19" # `b` here is used to convert str to bytes since `bytes format` is used to hash the password
hashedpwd = bcrypt.hashpw(password, bcrypt.gensalt())
#print("Your hashed password is : ", hashedpwd)

entered_pwd = input('Please enter your password : ')
entered_pwd = bytes(entered_pwd, encoding= 'utf-8') # here your encoding password to convert str to bytes , to check the password

if bcrypt.checkpw(entered_pwd, hashedpwd):
    print("Loging is successfull!! ")
else:
    print("Login failure")