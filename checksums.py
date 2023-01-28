import hashlib
import os


# stored_checksums = []

def write_list_to_file(my_list, filename):
    with open(filename, 'a') as f:
        for item in my_list:
            f.write(item + '\n')

def read_file_to_list(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines



def checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def checksum_directory(directory):
    stored_checksums = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_checksum = checksum(file_path)
            stored_checksums.append(file_checksum)
            print(f'{file_path}: {file_checksum}')
            write_list_to_file(stored_checksums, 'log.txt')



def verify_checksum(checksum, checksum_array):
    if checksum in checksum_array:
        print(f"Checksum: {checksum} \tMatch Found:\t{checksum}")
        return True
    else:
        print(f"Checksum: {checksum} \tMatch Found:\tFalse")
        return False


def compare_lists(list1, list2):
    for checksum in list1:
        if checksum in list2:
            print("Match found!")
            return True
    print("No match found.")
    return False

def validate_directory_path(path):
    if not os.path.isdir(path):
        raise ValueError(f"{path} is not a valid directory.")
    else:
        return True

def manual():
    path = input("Enter the path to the directory: ")
    if validate_directory_path(path):
        checksum_directory(path)
