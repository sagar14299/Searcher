import pyperclip, re

def phone(text) :
    phone_re = re.compile(r'''
            ((\(\+\d{3}\)-)|(\+\d{3}-)|(\+\d{3}\s))?  
            # (+977-).....OR...+977...OR..+977 .......OR...none
            
            (((\d{4}-\d{3}-\d{3})|(\d{10}))|(\d{1,3}-\d{5,6}))     
            #10-digit phone number........OR..6-7 digit landline number
            ''',re.VERBOSE)
    
    #iterating through each match and appending it to ph_list
    ph_list = []
    for ans in re.finditer(phone_re, text) :
        ph_list.append(str(ans.group(0)))
    
    if len(ph_list) == 0 :
        return 'No numbers found!'
    else :
        ph_nums = '\n'.join(ph_list)        #converting list into string
        return ph_nums


def mail(text) :
    mail_re = re.compile(r'''
            [0-9a-zA-Z-_%+.]+       #name
            @               
            [0-9a-zA-Z-]+           #domain name
            \.[0-9a-zA-Z-]+         #.com or sth
            (\.[a-zA-Z]{2,4})?      #.np or sth
            ''',re.VERBOSE)
    
    #iterating through each match and appending it to ph_list
    mail_list = []
    for ans in re.finditer(mail_re, text) :
        mail_list.append(str(ans.group(0)))

    
    if len(mail_list) == 0 :
        return 'No emails found!'
    else :
        emails = '\n'.join(mail_list)       #converting list into string
        return emails


text = pyperclip.paste()
ans = mail(text)+'\n'+phone(text)
pyperclip.copy(ans)
print('Following were successfully copied to clipboard :\n\n'+ans)
