from baseclass import Base
from options import Results
import csv

base = Base()
result = Results(base.driver)

base.item_search(result.item)
base.buy_it_now()
combined_info = []
while True:
    for i in zip(result.titles(), result.prices(), result.links()):
        if 'to' not in i[1] and result.number_of_entries != len(combined_info):
            combined_info.append(i)
    if result.number_of_entries > len(combined_info):
        try:
            base.next_page()
            continue
        except:
            break
    else:
        break

filename = input('CSV File Name? :')
csv_file_path = f'/Users/amirantevzadze/Desktop/{filename}.csv'

if filename != '':  # Will skip the csv creation if left blank.
    num = 1
    with open(csv_file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Price', 'Link'])
        for i in combined_info:
            listed = list(i)
            row_result = [num, listed[0],listed[1],listed[2]]
            writer.writerow(row_result)
            num += 1
        print('CSV File Created')
else:
    print('CSV FILE SKIPPED')

base.close_window()