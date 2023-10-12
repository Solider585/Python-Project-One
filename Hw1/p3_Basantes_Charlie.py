#Q.3

string_input = input("Input a string: ")
s = str(string_input)

number_input = input("Enter a number: ")
n = int(number_input)


def find_dup_str(s, n):

    for i in range(len(s)):
        substring_slice = s[i:i+n]
        slice_remaining_string = s[i+n+1:]

        if slice_remaining_string.find(substring_slice) >= 0:
            #print("duplicate found :", do_something)
            return substring_slice
    return ""


def find_max_dup(s):

    for i in reversed(range(int(len(s)/2))):
        max_duplicate = find_dup_str(s,i)


        if max_duplicate:
            return max_duplicate
    return ""

print(find_dup_str(s,n))
print(find_max_dup(s))
