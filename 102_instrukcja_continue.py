print('Lesson\n')

print('Prosty przykład wykorzystania continue\n') 

for i in range (1, 6):
    if i % 2 == 0:
        continue
    print(i)

print('\nPrzykład z lekcji\n')

persons = ['Elizabeth',  'Steven@sales.mycompany.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']

domain = 'mycompany.com'

emails = []

for person in persons:

    if '@' in person:
        emails.append(person)
        continue

    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)