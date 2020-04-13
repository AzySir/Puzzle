import csv

# Without considering escape strings and creating an array
def getRows():
    with open('csv-sample.csv', 'r') as file: # Open 'read-only' csv-sample.csv
        reader = csv.reader(file) # Read the text inside of the file
        data = list(reader) # Convert the data read into a list and accomodate for the escape characters
        print("Total Rows: {}".format(len(data)))


# A shortened version of above code
def getRowsShortened():
    with open('csv-sample.csv', 'r') as file:
        print("Total Rows: {}".format(len(list(csv.reader(file)))))


getRows()


