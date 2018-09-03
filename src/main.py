def get_files_paths(directory: str, filter_function: callable=None) -> list:
    '''
    Return all directories and files paths from current directory
    :param directory: current_directory.
    :param filter_function: function to filter results. Example: os.path.isfile. Default None
    :return: list of paths to filtered files and directories from current directory
    '''
    import os
    directory = os.path.abspath(directory)
    pathc = os.listdir(directory)
    result = []
    counter = 0
    while len(pathc) > 0:
        current_item = pathc.pop()
        current_path = os.path.join(directory, current_item)
        if os.path.islink(current_path):
            continue
        if filter_function and filter_function(current_path) or not filter_function:
            result.append(current_path)
        if os.path.isdir(current_path):
            pathc += [os.path.join(current_path, sub_item) for sub_item in os.listdir(current_path)]
        counter += 1

    return result


def python_count(directory: str) -> int:
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
    import os

    def try_file_contains(file_path: str) -> bool:
        '''
        Checks if filename matches pattern PYTHON_<number>.txt and if count of occurrences is equal to number
        :param file_path: path to try files
        :return: boolean
        '''
        import re
        result = re.match(r'.*PYTHON_(?P<file_number>\d+)\.txt$', file_path, re.UNICODE | re.IGNORECASE)
        if not result:
            return False
        file_number = int(result.group('file_number'), base=10)
        try:
            with open(file_path, 'r') as current_file:
                content = current_file.read()
            return content.count('PYTHON') == file_number
        except FileExistsError:
            return False


    def try_path(filepath):
        return os.path.isfile(filepath) and try_file_contains(filepath)

    matching_files = get_files_paths(directory, try_path)
    return len(matching_files)


def main():
    directories = ['../resources/0', '../resources/1', '../resources/2', '../resources/3', '../resources/4']

    for directory in directories:
        print(python_count(directory))


if __name__ == '__main__':
    main()
