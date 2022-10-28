
def open_and_format(file_name):
    data_file = open(file_name, 'r')
    file_line = data_file.readline()
    items = []
    while file_line !='':
        item, price = file_line.rstrip().split(',')
        items.append((item, int(price)))
        file_line = data_file.readline()

    return items


