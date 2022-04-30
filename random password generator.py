import random 

# asking the user for the maximum length of the password
max_len = int(input("Enter the maximum length of the password: "))

# all the characters we will use in our password
digs = ["0","1","2","3","4","5","6","7","8","9",]
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
chars_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
syms = ["!","@","#","$","%","^","&","*",";",":","`","~","-","+","/","?","=","(",")"]

# combined list of all the characters based on the password level 
comb_list_easy = chars + chars_upper
comb_list_medium = digs + chars + chars_upper
comb_list_strong = digs + chars + chars_upper + syms

# selecting a character from each of the lists
rand_digs = random.choice(digs)
rand_chars = random.choice(chars)
rand_chars_upper = random.choice(chars_upper)
rand_syms = random.choice(syms)

# asking the user the level of password
print("1.)Easy\n2.)Medium\n3.)Strong")
pass_level = input("Enter the level of the password: ")

# password generator if the password level selected by the user is easy
if pass_level in ["1","easy","EASY","Easy"]:
    # making a password of 2 character to ensure we have atleast 1 character from the two lists, i.e. the characters list and the upper characters list 
    temp_pass = rand_chars + rand_chars_upper 
    counter = 2
    while counter < max_len:
        temp_pass = temp_pass + random.choice(comb_list_easy)
        counter += 1
    print(temp_pass)

# password generator if the password level selected by the user is medium
elif pass_level in ["2","medium","MEDIUM","Medium"]:
    # making a password of 3 character to ensure we have atleast 1 character from the three lists, i.e. the characters list, the upper characters list 
    # and the digits list
    temp_pass = rand_chars + rand_chars_upper + rand_digs
    counter = 3
    while counter < max_len:
        temp_pass = temp_pass + random.choice(comb_list_medium)
        counter += 1
    print(temp_pass)

# password generator if the password level selected by the user is strong
elif pass_level in ["3","strong","STRONG","Strong"]:
    # making a password of 4 character to ensure we have atleast 1 character from the four lists, i.e. the characters list, the upper characters list and the digits list
    # and the symbols list
    temp_pass = rand_chars + rand_chars_upper + rand_digs + rand_syms
    counter = 4
    while counter < max_len:
        temp_pass = temp_pass + random.choice(comb_list_strong)
        counter += 1
    print(temp_pass)