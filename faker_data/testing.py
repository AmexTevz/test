import csv
import psycopg2
from faker_data_options import Options

# Current headers are - Fname, Lname, Age, Job, Company

options_data = Options()

try:
    quantity = int(input('How many ROWS? : ')) # The number of rows needed.
except ValueError:
    print('Only intigers are allowed\nPlease Try Again')
else:
    # Type headers from the headers list above. Use space in between.
    headers = list(input('What are the COLUMNS? :  ').replace(',',' ').split(' '))
    filename = input('CSV File Name? :')  # Choose the CSV file name or leave it blank.
    csv_file_path = f'PATH TO YOU DIRECTORY/{filename}.csv'

    num = 1

    def key_generator():
        key_list = ['Id']
        value_list = [num]
        for i in headers:
            if i.title() in options_data.faker_header().keys():
                key_list.append(i.title())
                values = options_data.faker_header()[i.title()]
                value_list.append(values)
        return key_list, value_list


    def value_generator():
        transfer_to_strings = ','.join(str(i) for i in key_generator()[1])
        surround_with_quotes = ','.join(f"'{i}'" for i in transfer_to_strings.split(',')[1:])
        result = f'({surround_with_quotes})'
        return result


    if filename != '':  # Will skip the csv creation if left blank.

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
        if data.title() in options_data.faker_dict().keys():
            d_headers.append(options_data.faker_dict()[data.title()])
            d_inserts.append(data.title())
    database_headers = f"({','.join(d_headers)})"
    database_inserts = f"({','.join(d_inserts)})"

    table_name = input('\n\nTable Name For The SQL?: ')  # Will skip the table creation if left blank.

    if table_name != '':

        con = psycopg2.connect(
            database="Database Name",
            user="postgres",
            password="Password",
            host="127.0.0.1",
            port='5432'
        )

        cursor = con.cursor()
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
