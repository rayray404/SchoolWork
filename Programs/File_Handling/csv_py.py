import csv

fil = open("CSV.csv", "a")
csv_w = csv.writer(fil)

csv_w.writerow([1,2,3])
fil.close()