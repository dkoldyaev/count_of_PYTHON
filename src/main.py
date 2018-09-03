def get_files_paths(directory):
    import os
    pathc = os.listdir(directory)
    result = []
    while (len(pathc) > 0) :
        current_path = os.path.join(directory, pathc.pop())
        if os.path.isfile(current_path) :
            result.append(current_path)
            print('is_file: %s\n' % current_path)
        else :
            pathc.append(current_path)
            print('is_directory: %s\n' % current_path)


def python_count(directory):
    """Count how many files in the provided directory contain equal number of PYTHON occurrences as its corresponding
    number in the file name. Do not use bash/shell functions.

    Each file name is of the following format PYTHON_[3 digit number].txt

    Examples:
        file PYTHON_002.txt is counted iff contains exactly 2 PYTHON occurrences, otherwise it is not counted.

    Args:
        directory (str): path to the directory whose files need to be counted.

    Returns:
        int: number of files
    """
    get_files_paths(directory)
    return 1



def main():
    directories = ['../resources/0', '../resources/1', '../resources/2', '../resources/3', '../resources/4']

    for directory in directories:
        print(python_count(directory))


if __name__ == '__main__':
    main()
