# checksum-tools
This Python module contains several functions for generating and comparing checksums of files in a specified directory.
# Functionality
The checksum(file_path) function generates a SHA-256 checksum of a specified file.
The checksum_directory(directory) function generates SHA-256 checksums for all files in a specified directory, and writes them to a log file (log.txt).
The write_list_to_file(my_list, filename) function writes a list to a specified file.
The read_file_to_list(filename) function reads a specified file and returns the contents as a list.
The verify_checksum(checksum, checksum_array) function verifies if a specified checksum is present in an array of checksums.
The compare_lists(list1, list2) function compares two lists of checksums and returns true if any matches are found.
# Usage
- To use this module, import it in your Python script
- To generate checksums for all files in a directory, call the checksum_directory(directory) function and pass in the path to the directory as an argument.
- The verify_checksum(checksum, checksum_array) function can be used to verify a single checksum, and the compare_lists(list1, list2) function can be used to compare two   lists of checksums.
- The read_file_to_list(filename) function can be used to read the log file and get the list of checksums.
# Notes
- This module uses the hashlib library for generating SHA-256 checksums, and the os library for traversing directories.
- The checksum_directory(directory) function will write all generated checksums to a file named 'log.txt' in the current directory.
- The verify_checksum(checksum, checksum_array) and compare_lists(list1, list2) functions are for example purpose only, you can use them as per your requirement.
