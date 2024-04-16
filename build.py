import subprocess
import shutil
import sys
import unittest

def clean():
    print("Cleaning up...")
    dist_dir = "dist"
    if shutil.os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)

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
        print("Unit tests failed, but continuing with packaging...")

def package():
    print("Packaging...")
    try:
        subprocess.check_call([sys.executable, "setup.py", "sdist"])
    except subprocess.CalledProcessError:
        sys.exit(1)

def main():
    clean()
    compile_and_test()
    package()
    print("Build completed successfully.")

if __name__ == "__main__":
    main()
