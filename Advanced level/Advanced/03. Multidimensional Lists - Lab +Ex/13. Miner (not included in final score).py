def count_substring(string, sub_string):
    len_of_sub_string = len(sub_string)
    count = 0
    for s in range(len(string)):
        stop = len_of_sub_string
        search_match = string[s:len_of_sub_string]
        len_of_sub_string += 1
        if search_match == sub_string:
            count += 1
        if len_of_sub_string > len(string):
            break
    return count


print(count_substring('ABCDCDC', 'CDC'))