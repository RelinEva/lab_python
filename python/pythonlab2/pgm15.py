#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
'''
def generate_password(level):
    import string
    import random
    level_dict={'low':8,'middle':12,'high':16}
    segment=[0,0,0,0]
    for x in range (level_dict[level]):
        r=random.randint(0,3)
        segment[r]+=1
        lower_letter=random.choices(string.ascii_lowercase,k=segment[0])
        upper_letter=random.choices(string.ascii_uppercase,k=segment[1])
        digits=random.choices(string.digits,k=segment[2])
        symbols = random.choices('!@#$%^&*()_+', k=segment[3])
        password=lower_letter+upper_letter+digits+symbols
        random.shuffle(password)
        return "".join(password)
    def check_level_input(string,level):
        if string.lower()==level or string.lower()==level.lower()[0]:
            return True
        else:
            return False
        def main():
            while True:
                level=input('choose your password security level:[low|middle|high]')
                if level.lower()=='exit':
                    break
                elif check_level_input(level,'low'):
                    print(generate_password('low'))
                elif check_level_input(level,'middle'):
                    print(generate_password('middle'))
                elif check_level_input(level,'high'):
                    print(generate_password('high'))
                else:
                    print('Input Error')
                    if __name__ == "__main__":
                     main() '''



def generate_passwords(level):
    """
    Generate password of specific level.
    
    Arguments:
    level -- password security level. 8 characters for low, 12 for
    middle, and 16 for high. In each pattern, the password is a
    mix of lowercase letters, uppercase letters, numbers, and symbols.
    
    Returns:
    password -- a password string.
    """
    import string
    import random
    
    level_dict = {'low':8, 'middle':12, 'high':16}
    
    segment = [0, 0, 0, 0]
    for x in range(level_dict[level]):
        r = random.randint(0,3)
        segment[r] += 1
    
    lower_letter = random.choices(string.ascii_lowercase, k=segment[0])
    upper_letter = random.choices(string.ascii_uppercase, k=segment[1])
    digits = random.choices(string.digits, k=segment[2])
    symbols = random.choices('!@#$%^&*()_+', k=segment[3])
    
    password = lower_letter + upper_letter + digits + symbols
    random.shuffle(password)
    
    return ''.join(password)

def check_level_input(string, level):
    """
    Check the input string is a level or not.
    
    Arguments:
    string -- input string.
    level -- correct level string.
    
    Returns:
    True/False -- if the input is correct level, return True, else return false.
    """
    if string.lower() == level or string.lower() == level.lower()[0]:
        return True
    else:
        return False
    
def main():
    while True:
        level = input('Choose your password security level: [low/middle/high]')
        if level.lower() == 'exit':
            break
        elif check_level_input(level, 'low'):
            print(generate_passwords('low'))
        elif check_level_input(level, 'middle'):
            print(generate_passwords('middle'))
        elif check_level_input(level, 'high'):
            print(generate_passwords('high'))
        else:
            print('Input error.')
        
if __name__ == "__main__":
    main()


                

                               