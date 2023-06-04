from baseclass import Base
from options import Results
import csv

base = Base()
result = Results(base.driver)

base.item_search(result.item)
base.buy_it_now()

filename = input('CSV File Name? :')
csv_file_path = f'/Users/amirantevzadze/Desktop/{filename}.csv'

if filename != '':  # Will skip the csv creation if left blank.
    num = 1
    with open(csv_file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Price', 'Link'])
        for name, price, link in zip(result.titles(), result.prices(), result.links()):
            if 'to' not in result.prices():
                row_result = [num, name, price, link]
                writer.writerow(row_result)
                num += 1
        print('CSV File Created')
else:
    print('CSV FILE SKIPPED')

base.close_window()
