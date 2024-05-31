# Write your code here
import re
def is_valid_email_address(string):
    return re.fullmatch(r'[a-z1-9\.]*@{1}(ucll\.be|student\.ucll\.be)', string)