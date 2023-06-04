from baseclass import Base
from options import Results

base = Base()
result = Results(base.driver)

base.item_search(result.item)
base.buy_it_now()

print(result.titles())

print(result.prices())
print(result.links())
base.close_window()
