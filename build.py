import subprocess
import sys
import unittest
from pathlib import Path
import shutil
from args import args_for_cal as args

def compile_and_test():
    print("Compiling and testing...")
    test_failed = False
    try:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromName("test_calc"))
        if not result.wasSuccessful():
            test_failed = True
    except Exception as e:
        print(f"An error occurred during testing: {e}")
        test_failed = True

    if test_failed:
        print("Unit tests failed, but continuing....")

def build_executable():
    print("Building executable.......")
    # Path to calc.py
    calc_file = Path('calc.py').resolve()

    # Using pyinstaller to create an executable
    cmd = [
        'pyinstaller',
        '--onefile',            
        '--name', 'calculator', 
        str(calc_file)          
    ]

    try:
        subprocess.run(cmd, check=True)
        print("Executable created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating executable: {e}")
        sys.exit(1)

def clean():
    # Cleaning up temporary build files and directories
    print("Cleaning up...")
    try:
        shutil.rmtree('build', ignore_errors=True)  # Remove build directory
        shutil.rmtree('dist', ignore_errors=True)   # Remove dist directory
        shutil.rmtree('__pycache__', ignore_errors=True)  # Remove __pycache__ directory
        for file in Path('.').glob('*.spec'):  # Remove any .spec files
            file.unlink()
        print("Cleanup complete!")
    except Exception as e:
        print(f"Error cleaning up: {e}")

def run_executable():
    # Running the executable
    exe_path = Path('dist').joinpath('calculator.exe')
    if exe_path.exists():
        print("Running the executable...")
        try:
            subprocess.run(str(exe_path), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the executable: {e}")
    else:
        print("Executable not found. Please build the executable first.")

if __name__ == '__main__':
    if args.jenkins == False:
        while True:
            print('''
            1. Clean-up only
            2. compile and test only.
            3. build executable only.
            4. clean up, compile and test, build executable
            5. exit
            
            ''')
        
            choice = input("Enter your choice: ")

            if choice == "1":
                clean()
                sys.exit("Cleaned your directory tree!!!")
            if choice == "2":
                compile_and_test()
            if choice == "3":
                build_executable()
            if choice == "4":
                clean()
                compile_and_test()
                build_executable()
            if choice == "5":
                sys.exit("ByeBye!!")
            
            if choice not in ["1", "2", "3", "4", "5"]:
                sys.exit("Invalid Choice!! Goodday!")

            answer = input("Installation complete, Do you wish to run the program?(yes/No || y/n) ")

            if answer.lower() == "y":
                print(answer.lower())
                run_executable()
                sys.exit("Goodday!!!")
            if answer.lower() == "yes":
                run_executable()
                sys.exit("Goodday!")
            else:
                sys.exit("Have a good day, you can run your program at dist/.")
    else:
        if args.compile_test and args.build_executable:
            clean()
            compile_and_test()
            build_executable()
        elif args.clean and args.compile_test:
            clean()
            compile_and_test()
        elif args.clean and args.build_executable:
            clean()
            build_executable()
        elif args.compile_test:
            compile_and_test()
        elif args.clean:
            clean()
        elif args.build_executable:
    
            build_executable()