import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'managers'))

from fileManager import FileManager

def generate_input_and_output():
    fm = FileManager(True)
    fm.create_random_input_and_output()
    return None

def test2():
    return None

if __name__ == "__main__":
    print("Using file manager")
    generate_input_and_output()
