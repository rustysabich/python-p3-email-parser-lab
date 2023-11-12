# create EmailAddressParser class

# import the re module
import re
class EmailAddressParser:
    
    # initialize an instance with a string of emails
    def __init__(self, email_string):
        self.email_string = email_string
        
    # create a parse()
    def parse(self):
        emails = re.split(r"[\s,]+", self.email_string)
        # sort the emails
        emails.sort()
        return [email for email in emails if re.match(r"^[A-z][\w\.]+@[\w]+\.[\w]+$", email)]
        