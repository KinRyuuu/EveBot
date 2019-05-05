# Take a file and read it into an array splitting on a given delimiter
def parse_file_as_array(file, delimiter=None):

    # Open the file and get all lines that are not comments or blank
    with open(file, 'r') as fileHandler:
        read_data = [(line) for line in fileHandler.readlines() if is_blank_or_comment(line) == False]

    # If no delimiter is given, split on newlines, else we need to split on the delimiter
    if delimiter is None:
        file_array = read_data
    else:
        file_array = "".join(read_data).split(delimiter)

    return file_array


# Determines whether a line is either blank or a comment
def is_blank_or_comment(line):
    return line.strip() == '' or line[0:2] == "//"
