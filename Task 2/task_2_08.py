#8.Print Today's date. in the format 'dd.mm.yyyy'.

from datetime import datetime

print(datetime.today().strftime('%d-%m-%Y'))