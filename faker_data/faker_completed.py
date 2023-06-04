from faker import Faker
from faker.providers import internet
import random
import csv
import psycopg2


fake = Faker()
fake.add_provider(internet)

database = {'Fname': 'Fname varchar(500)', 'Lname': 'Lname varchar(500)', 'Age': 'Age int',
            'Gender': 'Gender varchar(500)', 'Job': 'Job varchar(500)', 'Company': 'Company varchar (500)'}
quantity = int(input('How many ROWS? : '))
headers = list(input('What are the COLUMNS? :  ').split(' '))
filename = input('CSV File Name? :')
csv_file_path = f'/Users/amirantevzadze/Desktop/{filename}.csv'


def key_generator():
    key_list = ['Id']
    value_list = [num]
    age = random.randint(18, 66)
    gender = random.choice(['Male', 'Female'])
    header_dict = {'Fname': fake.first_name(), 'Lname': fake.last_name(), 'Age': age, 'Gender': gender,
                   'Job': ' '.join(fake.job().split(',')).replace("'s",""),
                   'Company': ' '.join(fake.company().split(',')).replace("'s","")}
    for i in headers:
        if i.title() in header_dict.keys():
            key_list.append(i.title())
            values = header_dict[i.title()]
            value_list.append(values)
    return key_list, value_list


def value_generator():
    transfer_to_strings = ','.join(str(i) for i in key_generator()[1])
    surround_with_quotes = ','.join(f"'{i}'" for i in transfer_to_strings.split(',')[1:])
    result = f'({surround_with_quotes})'
    return result,transfer_to_strings,surround_with_quotes
print(value_generator())

if filename != '':
    num = 1
    with open(csv_file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(key_generator()[0])
        for _ in range(quantity):
            row_result = key_generator()[1]
            writer.writerow(row_result)
            num += 1
        print('CSV File Created')
else:
    print('CSV FILE SKIPPED')
    pass


d_headers = ['Id serial PRIMARY KEY']
d_inserts = []
for data in headers:
    if data.title() in database.keys():
        d_headers.append(database[data.title()])
        d_inserts.append(data.title())
database_headers = f"({','.join(d_headers)})"
database_inserts = f"({','.join(d_inserts)})"


table_name = input('\n\nTable Name For The SQL?: ')


if table_name != '':

    con = psycopg2.connect(
        database="faker",
        user="postgres",
        password="Teklunia1",
        host="127.0.0.1",
        port='5432'
    )

    cursor = con.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    cursor.execute(f"CREATE TABLE {table_name} {database_headers};")
    for _ in range(quantity):
        cursor.execute(f"INSERT INTO {table_name} {database_inserts}\nVALUES {value_generator()}")

    con.commit()
    con.close()
    cursor.close()
    print('Database Table Created')

else:
    print('DATABASE TABLE SKIPPED')
    pass

