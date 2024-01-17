import os
from dotenv import load_dotenv
from colorama import Fore

def main():
    
    print(Fore.YELLOW + 'I\'am main')

    print(os.getenv('DB__USER'))


if __name__ == '__main__':
    load_dotenv()
    main()
