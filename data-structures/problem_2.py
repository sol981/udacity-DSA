import os
from typing import List

def find_files(suffix: str, path: str) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    
    lst = []
    # Current working directory
    current_dir = os.getcwd()

    folder = os.path.join(current_dir, path)
    if os.path.isdir(folder):
        files_in_dir = os.listdir(folder)

        for file_name in files_in_dir:
            f = os.path.join(current_dir,path, file_name)
            next = os.path.join(path, file_name)
            if os.path.isdir(f):
                lst += find_files(suffix, next)

            if os.path.isfile(f) and file_name[-1] == suffix[-1] and file_name[-2] == suffix[-2]:
                lst.append(path + "/" +file_name)
    return lst

if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    print("testcase 1")
    print(find_files(".c", './testdir'))

    # Test case 2: find a file with suffix .c in wrong path
    print("testcase 2")
    print(find_files(".c", 'wrong_dir'))

    # Test case 3: find a file with suffix .c in subsubdir
    print("testcase 3")
    print(find_files(".c", './testdir/subdir3/subsubdir1'))