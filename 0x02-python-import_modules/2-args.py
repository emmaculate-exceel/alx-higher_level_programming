#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import argparse

    parser = argparse.ArgumentParser(description='Print the number of and list of arguments.')

    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='List of arguments')

    args = parser.parse_args()

    list_of_arguments = args.arguments
    number_of_arguments = len(list_of_arguments)
    list_of_arguments = args
    ,
    print("Number of arguments:", number_of_arguments)
    print("List of arguments:", list_of_arguments)

