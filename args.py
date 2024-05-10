import argparse

parser = argparse.ArgumentParser(description='Build script for Calculator project')
parser.add_argument('--jenkins', action='store_true')
parser.add_argument('--operation', '-op', help='add, sub, div, mul; Requires when running through Jenkins')
parser.add_argument('--num1', '-n1', type=float, help="Enter num1")
parser.add_argument('--num2', '-n2', type=float, help="Enter num2")

parser.add_argument('--build_executable', action='store_true', help='build the executable only')
parser.add_argument('--clean', action='store_true', help='Clean up previous build artifacts')
parser.add_argument('--compile_test', action='store_true', help='Compile and test the code')
args_for_cal = parser.parse_args()