from string import ascii_lowercase

def create_cell(i, j):
    first_char = ascii_lowercase[i]
    middle_char = ascii_lowercase[i+j]
    return f"{first_char}{middle_char}{first_char}"

print(create_cell(4, 6))