import csv
import sys

def parse_csv(direction):
    cat = []
    with open(direction, 'rU') as csvfile:
        # read in title of the file . 
        t = csvfile.readline()
        title = t.replace(",", "")
        # read in category of CSV file
        t = csvfile.readline()
        cat = t.strip().split(',')
        print cat
        # parsing data and store in cat. ...
        reader = csv.reader(csvfile)
        #for line in reader:
        #   print line
        numline = len(csvfile.readline()) 
    csvfile.close() 
    print numline

# parse line and store in cat .... or .... 

if __name__ == '__main__':
    upload_link = sys.argv[1]
    parse_csv(upload_link)


