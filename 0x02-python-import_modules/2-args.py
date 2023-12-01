#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import argparse

    parser = argparse.ArgumentParser(description='Print the number of and list of arguments.')

    args = parser.parse_args()

    number_of_arguments = len(args)
    list_of_arguments = args

    print("Number of arguments:", number_of_arguments)
    print("List of arguments:", list_of_arguments)

