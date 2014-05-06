import csv

def main():
	reader = csv.DictReader(open("record.csv", "rb"))
	for row in reader:
		if row['FirstName'] == ' ':
			print 'First Name is empty. Unsuccessful'
		elif row['Age'] == ' ':
			print 'Age is empty. Unsuccessful'
		else:
			print 'Successful', row

if __name__ == "__main__":
	main()
