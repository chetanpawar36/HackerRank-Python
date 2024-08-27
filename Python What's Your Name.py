# """____Question: What's Your Name?____"""


#-->Complete the print_full_name function


def print_full_name(first_name, last_name):
    
    print(f"Hello {first_name} {last_name}! You just delved into Python.")
    
if __name__ == '__main__':
    
    first_name = input("enter the first name to be entered: ")
    
    last_name = input("enter the last name to be entered: ")
    
    print_full_name(first_name, last_name)
