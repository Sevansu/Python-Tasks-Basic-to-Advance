'''8.Compare whether the entered email is correct or not using the regular expression. An email should be in the format xyz@abc.dom or xyz@abc.dom.subdom'''

import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):
    if(re.search(regex,email)):  
        print("Valid Email")  
    else:  
        print("Invalid Email")  
 
if __name__ == '__main__' :   
    email = "sevansupatel2122@gmail.com"  
    check(email) 
    email = "mynamesomenumber@go.minnstate.edu"
    check(email)
    email = "sevansu.com"
    check(email) 