'''9.Check a mobile number for india whehter it is a valid one or not using the regular expression. The format should be +91-1234567890'''

import re
regex = r'(?<!\w)(?:(?:\+91-)\s?)?\d{10}\b'
def check(phone):
    if(re.search(regex,phone)):  
        print("Valid phone")  
    else:  
        print("Invalid phone")  
 
if __name__ == '__main__' :   
    phone = "+91-1234567890"  
    check(phone) 
    phone1 = "09542315612"
    check(phone1) 