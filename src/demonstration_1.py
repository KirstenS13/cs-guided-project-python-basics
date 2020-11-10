"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""


def split_in_parts(s, part_length):
    # Your code here
    # create a variable for the new string
    return_list = []  # empty list
    # print("return_list: ", return_list)
    substring = ""  # empty string

    #  alternate syntax for someone who understands python much better than I do
    # for i in range(0, len(s) + 1, 3):
    #     print(s[i: (i + 3)])

    for letter in s:
        print(letter)
        # if the length of the substring is less than part_length:
        if len(substring) < part_length:
            # then we add the letter to it
            substring = substring + letter  # or substring += letter
        # otherwise, we add the substring to the return list
        else:
            return_list.append(substring)
        # reset the substring to be an empty string
            substring = ""
        # add the letter
            substring = substring + letter  # or substring += letter

    if len(substring) > 0:
        return_list.append(substring)

    # makes it a string with spaces separating every 3 letters
    return_string = " ".join(return_list)

    return return_string
    # for letter in s:
    # for i in range(len(s)):
    # string_slice = s[start_index:end_index]


    # Your code here
print(split_in_parts("supercalifragilisticexpialidocious", 3))
