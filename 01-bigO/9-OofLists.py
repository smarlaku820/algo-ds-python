# Adding or removing items to the end of the list is O(1)
# as no re-indexing happens.
# Adding or removing items to the start of the list is O(n)
# as re-indexing occurs.
# Adding items in the middle of the list, still counts
# as O(n) although only n/2 operations occur. Remember,
# we drop the constants.