
def read_file_to_list(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines

# Example usage
sum_log = 'log.txt'
log_list = read_file_to_list(sum_log)
print(log_list)


def verify_checksum(checksum, checksum_array):
    if checksum in checksum_array:
        print(f"Checksum: {checksum} \tMatch Found:\t{checksum}")
        return True
    else:
        print(f"Checksum: {checksum} \tMatch Found:\tFalse")
        return False

# stored_checksums = ["a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16", "a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p17","a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p18"]

# verify_checksum("a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16", stored_checksums)
# verify_checksum("a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p19", stored_checksums)
def compare_lists(list1, list2):
    for checksum in list1:
        if checksum in list2:
            print("Match found!")
            return True
    print("No match found.")
    return False

# Example usage
#list1 = ['a1b2c3', 'd4e5f6', 'g7h8i9']
#list2 = ['j0k1l2', 'a1b2c3', 'm3n4o5']

# if compare_lists(list1, list2):
    # print("Match found!")
# else:
    # print("No match found.")