import csv

# Parse data as csv file
def load_csv(name, delimiter=','):
    data = []
    with open(name, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        line_count = 0
        for row in csv_reader:
            sample = {}
            if line_count==0:
                keys = row
            else:
                for i in range(len(keys)):
                    sample[keys[i]] = row[i]
                data.append(sample)
            line_count += 1
    return data