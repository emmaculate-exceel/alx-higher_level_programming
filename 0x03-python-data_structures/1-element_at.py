def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return ("None")  # Return None if the index is out of range

    element = my_list[idx]  # Get the element at the specified index
    return element  # Return the element foundi
