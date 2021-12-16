'''
Create a python application to secure 
our existing password by swapping numbers and letters
to your transformed password.

Example:
    SECURE_dict= {'i': 'l', 'o':'u', 'v': 'y', 'c': 'k', '1': '0', '2':'9', '3':'8',
            'l': 'i','u':'o', 'y': 'v', 'k': 'c', '0': '1', '9':'2', '8':'3' }

    Input:
    password ='Ilovecoding123'
    password2 ='LIUKEKudlng098'


    Output:
    Your secure password is: liuyekudlng098
    Your secure password is:  ilocecoding123
    

'''
SECURE_dict= {'i': 'l', 'o':'u', 'v': 'y', 'c': 'k', '1': '0', '2':'9', '3':'8',
            'l': 'i','u':'o', 'y': 'v', 'k': 'c', '0': '1', '9':'2', '8':'3' }

def securePassword(password):
    transTable = password.maketrans(SECURE_dict)
    password = password.translate(transTable)
    return password
  





if __name__ == "__main__":
    password = input('Enter your password: ')
    password = password.lower()
    password = securePassword(password)
    
    print(f'*******Your safer password is: {password}********')


