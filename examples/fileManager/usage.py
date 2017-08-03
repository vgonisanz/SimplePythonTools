import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))

from fileManager import FileManager

def generate_input_and_output(input_path = "./input", output_path = "./output"):
    fm = FileManager(True)
    fm.create_random_input_and_output(5, input_path, output_path)
    return None

def rename_files_with_hash_in_extension_folder(input_path, output_path):
    fm = FileManager(True)
    fm.set_input_path(input_path)
    fm.set_output_path(output_path)
    file_list = fm.get_list_files_input_path()
    fm.rename_files_with_hash_in_extension_folder(file_list)
    return None

if __name__ == "__main__":
    print("Using file manager")
    input_path = "./input"
    output_path = "./output"
    generate_input_and_output(input_path, output_path)
    rename_files_with_hash_in_extension_folder(input_path, output_path)
    #fm.purge_input_and_output()
