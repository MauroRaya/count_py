#!/usr/bin/env python3
import sys

if sys.argv != 2:
    print('incorrect syntax: python3 path/count.py path/file/to/read')


try:
    file_path  = sys.argv[1].lower()
    
    with open(file_path) as file:
        line_count = 0
        word_count = 0
        char_count = 0
        
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)
        
        print('Line count:', line_count)
        print('Word count:', word_count)
        print('Character count:', char_count)

except FileNotFoundError:
    print('File not found')