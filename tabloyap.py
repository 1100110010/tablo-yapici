from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['isim', 'yaş', 'şehir']
table.add_row(["falcon excalibur", 13, "ağrı"])
table.add_row(["aeburuwole", 14, "ağrı"])
table.add_row(["veteran7", 000000, "bilinmiyor"])
table.add_row(["null", 123, "null"])
table.add_row(["null", 123, "null"])

print(table)
print('made by falcon excalibur(can cayar)')
