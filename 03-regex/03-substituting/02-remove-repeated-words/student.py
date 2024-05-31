# Write your code here
import re
def remove_repeated_words(string):
    return re.sub(r'(\b[a-zA-Z]+\b)( \1)+', r'\1', string)

#\b staat voor een woordgrens -> volledige woorden matchen en niet delen van woorden
#(\b[a-zA-Z]+\b)   === één volledig woord