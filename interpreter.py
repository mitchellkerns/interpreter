import os
import argparse
from main import interpret

def run_interpreter():
    parser = argparse.ArgumentParser(description="Interpret Nessus data.")
    parser.add_argument('-c', '--csv', type=str, help='Path to the CSV file generated by Nessus.')
    parser.add_argument('-d', '--dir', type=str, help='Directory where the output will be saved.')

    args = parser.parse_args()

    if not args.csv:
        args.csv = input("Please enter the path to the CSV file: ").strip()

    if not args.dir:
        args.dir = input("Please enter the client directory path: ").strip()

    # Ensure the client directory exists
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    # Initialize and run the Interpreter
    interpreter = interpret(args.csv, args.dir)
    print(f"Interpreter has successfully generated the report at: {interpreter.output_path}")

if __name__ == "__main__":
    run_interpreter()