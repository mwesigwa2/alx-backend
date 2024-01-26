#!/usr/bin/env python3
'''
    Write a function named index_range that
    takes two integer arguments page and page_size.

    The function should return a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination
    parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
'''


def index_range(page, page_size):
    '''
        takes 2 parameters and returns a tuple
    '''
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
