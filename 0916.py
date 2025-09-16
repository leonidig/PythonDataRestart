users = {
            "neo": [42, 'foo'],
            "trinity": [99, 'bar'],
            "morpheus": [7, 'baz']
        } 

login = input('Enter login: ')

attempts = 3

if login in users:
    code, word = users[login]

    while attempts > 0:
        secret_code = int(input('Enter code: '))
        
        if code == secret_code:
            secret_word = input('Enter word: ')
            if secret_word == word:
                print(f'Done!\nYou`r all set, {login}')
                break
            else:
                print('Access Denied')

        else:
            difference = abs(secret_code - code)
            if difference <= 10:
                print('Hot')
            else:
                print('Cold')

            attempts -= 1
            print(f'Attempts left: {attempts}')
    else:
        print('CODE 403')
    
else:
    print('User 404')