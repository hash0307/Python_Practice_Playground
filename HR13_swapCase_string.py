def swap_case(s):
    swap_string=""
    for letter in s:
        if letter.isupper():
            swap_string += letter.lower()
        elif letter.islower():
            swap_string += letter.upper()
        else:
            swap_string += letter
    return swap_string
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)