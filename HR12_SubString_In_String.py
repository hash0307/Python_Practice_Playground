def count_substring(string, sub_string):
    sub_string_len = len(sub_string)
    sub_count = 0
    for i in range(0, len(string)):
        if string[i:i+sub_string_len] == sub_string:
            sub_count += 1
    return sub_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)