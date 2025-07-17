emails = ["gmail.ahmed@com","islam@gmail.com","omargmail.com","karim@yahoo.com","mahmoud@outlook.com"]
valid_emails = list(filter(lambda emails: "@" in emails and "." in emails, emails))
print (valid_emails)