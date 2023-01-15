import re


def solve_p1(s) -> str:
    i = 0
    decompressed = ""
    while i < len(s):
        if s[i] == "(":
            num_to_repeat, repeat_times, repeater_declaration_length = extract_repeater(s, i)
            i += repeater_declaration_length
            decompressed += s[i + 1:i + num_to_repeat + 1] * repeat_times
            i += num_to_repeat
        else:
            decompressed += s[i]
        i += 1

    return decompressed


def solve_p2(s) -> int:
    decompressed_length = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            i, decompressed_length_substr = process_repeater_rec(s, i, 1)
            decompressed_length += decompressed_length_substr
        else:
            decompressed_length += 1
            i += 1
    return decompressed_length


def process_repeater_rec(s, i, existing_mult_factor):
    decompressed_length = 0
    num_to_repeat, duplication_factor, repeater_declaration_length = extract_repeater(s, i)
    i += repeater_declaration_length + 1
    end_idx = i + num_to_repeat
    while i < end_idx:
        if s[i] == "(":
            i, decompressed_length_substr = process_repeater_rec(s, i, duplication_factor * existing_mult_factor)
            decompressed_length += decompressed_length_substr
        else:
            decompressed_length += existing_mult_factor * duplication_factor
            i += 1
    return i, decompressed_length


def extract_repeater(s, i):
    starting_i = i
    repeater = "("
    while s[i] != ")":
        i += 1
        repeater += s[i]
    repeater_regex = re.findall(r"\d+", repeater)
    return int(repeater_regex[0]), int(repeater_regex[1]), i - starting_i
