import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    output_length = 0

    if num_arguments > 0:
        print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:", end='\n')
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")
            output_length += len(f"{i}: {arg}\n")
    else:
          print(f"{num_arguments} arguments.")

if __name__ == "__main__":
    print_arguments()