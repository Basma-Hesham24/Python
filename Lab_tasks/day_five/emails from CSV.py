import csv
from email_validation import validation
from domain_extraction import domain 

file = open("B:/python docs/emails from csv/users_emails.csv", "r")
reader = csv.reader(file)
data = list(reader)
file.close()

emails = []
for i in range(1, len(data)):
    if len(data[i]) >= 2 and data[i][1].strip() != "":
        emails.append(data[i][1])

valid_emails = []
for email in emails:
    if validation(email):
        valid_emails.append(email)

domains = []
for email in valid_emails:
    domain_name = domain(email)
    if domain_name not in domains:
        domains.append(domain_name)

#print(emails)
#print(valid_emails)
print (domains)