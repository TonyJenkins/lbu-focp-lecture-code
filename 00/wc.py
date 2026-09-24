#!/usr/bin/env python3

import sys


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def get_line_count(list_of_lines):
    return len(list_of_lines)


def get_character_count(list_of_lines):
    return sum(len(line.strip()) for line in list_of_lines)


def get_word_count(list_of_lines):
    word_count = 0
    for line in list_of_lines:
        word_count += len(line.split())

    return word_count


if __name__ == '__main__':

    try:
        content = read_file(sys.argv[1])

        lines = get_line_count(content)
        characters = get_character_count(content)
        words = get_word_count(content)

        print(f'{sys.argv[1]}:{lines}:{characters}:{words}')
    except IndexError:
        print(f'Usage: {sys.argv[0]} <file>')
    except FileNotFoundError:
        print(f'Usage: {sys.argv[0]} <file>')
