def common_elements(set_1, set_2):
    # Use set intersection to find common elements
    common_set = set_1.intersection(set_2)
    return common_set

# Example usage:
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
