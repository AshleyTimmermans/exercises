# Write your code here
import re
def scrape_email_addresses(string):
    return re.findall(r'[a-zA-Z1-9\.]*@{1}[a-zA-Z1-9\.]*', string)