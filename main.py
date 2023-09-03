import sys
from modules.transaction_calc.main import process_file
from modules.extensions import config

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
    else:
        file_path = sys.argv[1]
        process_file(file_path, config)
