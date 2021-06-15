from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['isim', 'yaş', 'şehir']
table.add_row(["djdjfj", 13, "dısjsksmsn"])
table.add_row(["djdjwjejej", 14, "fjfjdjsn"])
table.add_row(["dkwkwksjs", 000000, "bilinmiyor"])
table.add_row(["null", 123, "null"])
table.add_row(["null", 123, "null"])

print(table)

