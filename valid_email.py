# email_count = int(input())

import re

def valid_email(n,email_strings):
    # print(email_strings)
    for e in email_strings:
        name,email = re.split('\s',e,maxsplit=1)
        email = email.strip("<>")
        # print(name,email)
        regex = r'^[^\.\-\_]([0-9\w\-\.])+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
        email_address = re.search(regex,email)
        # print(email, email_address)
        if email_address:
            print(name,"<" + email_address.group() + ">")  
        else: 
            continue

emails = ["dheeraj <dheeraj-234@gmail.com>", "crap <itsallcrap>", "harsh <harsh_1234@rediff.in>", "kumal <kunal_shin@iop.az>", "mattp <matt23@@india.in>", "harsh <.harsh_1234@rediff.in>", "harsh <-harsh_1234@rediff.in>"]

emails2 = ["this <is@valid.com>","this <is_som@radom.stuff>","this <is_it@valid.com>","this <_is@notvalid.com>"]

valid_email(7,emails)


