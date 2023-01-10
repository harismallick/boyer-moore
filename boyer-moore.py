from typing import Tuple

def bad_char_rule(partial_str: str, search_str: str) -> int:

    mismatch_index = find_mismatch(partial_str, search_str)
    if mismatch_index == -1:
        return 0
    bad_char = partial_str[mismatch_index]

    for i in reversed(range(mismatch_index)):
        if search_str[i] == bad_char:
            return mismatch_index - i

    return mismatch_index + 1


def good_suff_rule(partial_str: str, search_str: str) -> int:
    
    mismatch_index: int = find_mismatch(partial_str, search_str)
    if mismatch_index == len(search_str):
        return 1

    good_suffix: str = partial_str[mismatch_index+1:]
    good_suffix_len: int = len(good_suffix)
    #size_diff = abs(mismatch_index-good_suffix_len)

    for i in reversed(range(mismatch_index+1)):
        x = search_str[i]
        y = good_suffix[-1]

        if search_str[i] == good_suffix[-1]:
            spliced_str = search_str[max((i-good_suffix_len+1),0):i+1]
            shift = find_mismatch(spliced_str, good_suffix[good_suffix_len-len(spliced_str):])

            if shift == -1:
                return (len(search_str)-i-1)

            #we paused here. Trying to figure out best solution for how to splice the search string.
            #this is a test.



    pass

def find_mismatch(partial_str: str, search_str: str) -> int:
    print('hello')
    for i in reversed(range(len(search_str))):
        if partial_str[i] != search_str[i]:
            return i
    
    return -1

def boyer_moore(full_str: str, search_str: str) -> Tuple[bool, int, int]:

    i = 0
    stop_index = len(full_str)-len(search_str)
    search_str_len = len(search_str)
    while i <= stop_index:

        partial_str = full_str[i:i+search_str_len]

        #bad_char_shift = bad_char_rule(partial_str, search_str)
        good_suffix_shift = good_suff_rule(partial_str, search_str)
        # if bad_char_shift > 0:
        #     i = i + bad_char_shift
        if good_suffix_shift > 0:
            i = i + good_suffix_shift

        else:
            return (True, i, i+search_str_len)
    
    return "didn't work"

def main():
    # full_str = "GCAATGCCTATGTG"
    # search_str = "TATGTG"
    full_str = "CCTGATCGCG"
    search_str = "CGTAACGGCG"
    test = boyer_moore(full_str, search_str)
    print(test)

if __name__ == '__main__':
    main()
