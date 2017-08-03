import os
import io
import sys
import string
import random
import hashlib
import shutil

"""
This python 3 class to easy manage files and folders

To generate HTML documentation for this module issue the command:

    pydoc -w fileManager
"""

class FileManager(object):
    _verbose = False
    _input_path = None
    _output_path = None
    """
    Initialize JsonManager with a name to identify eash instance
    """
    @classmethod
    def __init__(self, verbose = False):
        """
        Construct a new 'FileManager' object.
        By default input and output path is execution path

        :return: returns nothing
        """
        self._verbose = verbose
        self._input_path = os.path.join(self.pwd(), "input")
        self._output_path = os.path.join(self.pwd(), "output")
        return None

    """
    Test function
    """
    @classmethod
    def test(self):
        print("Test")
        return None

    """
    Generate random string
    """
    @classmethod
    def generate_random_string(self, size = 16, chars=string.ascii_uppercase + string.digits):
        data = str(''.join(random.choice(chars) for _ in range(size)))
        return data

    """
    Test function
    """
    @classmethod
    def create_random_file(self, path_name):
        file_content = self.generate_random_string()
        with io.FileIO(path_name, "w") as file:
            file.write(bytes(file_content, 'UTF-8'))
            file.close()
        return None

    """
    Create random input values and output folder
    """
    @classmethod
    def create_random_input_and_output(self, input_random_files = 3, relative_input_path = "input", relative_output_path = "output"):
        # Variables
        current_path = self.pwd()
        input_file_path = os.path.join(current_path, relative_input_path)
        output_file_path = os.path.join(current_path, relative_output_path)
        # Create folders if no exist
        self.mkdir(input_file_path)
        self.mkdir(output_file_path)
        # Initialize class
        self.set_input_path(input_file_path)
        self.set_output_path(output_file_path)
        # Create files
        for i in range(input_random_files):
            file_name = self.generate_random_string()
            file_path = os.path.join(input_file_path, file_name + ".txt")
            self.create_random_file(file_path)
        return None

    """
    Delete input and output folder
    """
    @classmethod
    def purge_input_and_output(self):
        self.rmdir(self._input_path)
        self.rmdir(self._output_path)
        return None

    """
    Create random input values and output folder
    """
    @classmethod
    def rmdir(self, path):
        shutil.rmtree(path, ignore_errors=True)
        return None

    """
    Get current working path
    """
    @classmethod
    def pwd(self):
        current_path = os.getcwd()
        return current_path

    """
    Create a folder recursively from a path
    """
    @classmethod
    def mkdir(self, path):
        if not os.path.exists(path):
            if self._verbose:
                print("Creating folder at: %s" % path)
            os.makedirs(path)
        return None

    """
    Get file size
    """
    @classmethod
    def file_size(self, file_path):
        file_size = None
        isfile = os.path.isfile(file_path)
        if isfile:
            file_size = os.path.getsize(file)
        else:
            print("File: %s doesn't exist" % file_path)
        return file_size

    """
    set_input_path
    """
    @classmethod
    def set_input_path(self, input_path, force_create = False):
        result = None
        isdif = os.path.isdir(input_path)
        if not isdif:
            if not force_create:
                print("Cannot set: %s as input path. It is not a directory" % input_path)
                return result
            else:
                self.mkdir(input_path)
        if self._verbose:
            print("Setting input path: %s" % input_path)
        self._input_path = input_path
        return result

    """
    set_output_path
    """
    @classmethod
    def set_output_path(self, output_path, force_create = False):
        result = None
        isdif = os.path.isdir(output_path)
        if not isdif:
            if not force_create:
                print("Cannot set: %s as output path. It is not a directory" % output_path)
                return result
            else:
                os.makedirs(output_path)
        if self._verbose:
            print("Setting output path: %s" % output_path)
        self._output_path = output_path
        return result

    """
    get_list_files_input_path
    """
    @classmethod
    def get_list_files_input_path(self):
        file_list = []
        for folder, subfolders, files in os.walk(self._input_path):
            for file in files:
                file_path = os.path.join(folder, file)
                file_list.append(file_path)
        return file_list

    """
    Calculate_hash

    Calculate Hash from a file, need absolute path
    """
    def calculate_hash(self, file_name, blocksize = 256):
        result = None
        md5 = hashlib.md5()
        isfile = os.path.isfile(file_name)
        if isfile:
            with open(file_name, 'rb') as rawfile:
                while True:
                    buf = rawfile.read(blocksize)
                    md5.update(buf)
                    if not buf:
                        break
                    md5.update(buf)
            result = md5.hexdigest()
        else:
            if self._verbose:
                print("File no exist")
        return result

    """
    Copy all files in output folder in a folder with its extension
    return: number of files moved
    """
    @classmethod
    def rename_files_with_hash_in_extension_folder(self, file_list, delete_input = False):
        if delete_input:
            print("Moving file list...")
        else:
            print("Copying file list...")
        counter = 0
        for file in file_list:
            file_exist = False
            file_extension = os.path.splitext(file)[1][1:]
            hash_name = self.calculate_hash(self, file)
            final_file_path = os.path.join(self._output_path, file_extension)
            isoutputdif = os.path.isdir(final_file_path)
            if not isoutputdif:
                os.makedirs(final_file_path)
            final_file_name = os.path.join(final_file_path, hash_name + "." + file_extension)
            file_exist = os.path.isfile(final_file_name)
            if not file_exist:
                counter = counter + 1
                if delete_input:
                    shutil.move(file, final_file_name)
                else:
                    shutil.copyfile(file, final_file_name)
            print("Processed: %s" % hash_name)
        print("Renamed %d files." % counter)
        return counter
