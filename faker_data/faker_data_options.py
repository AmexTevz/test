from faker import Faker
import random

fake = Faker()


class Options:
    def faker_header(self):
        age = random.randint(18, 66)

        header_dict = {'Fname': fake.first_name(), 'Lname': fake.last_name(), 'Age': age,
                       'Job': ' '.join(fake.job().split(',')).replace("'s",""),
                       'Company': ' '.join(fake.company().split(',')).replace("'s","")}
        return header_dict

    def faker_dict(self):
        database = {'Fname': 'Fname varchar(500)', 'Lname': 'Lname varchar(500)', 'Age': 'Age int',
                    'Job': 'Job varchar(500)', 'Company': 'Company varchar (500)'}
        return database



