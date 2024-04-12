import pytest

from lib.diary_entry import *
from lib.diary import *
from lib.phone_number_extractor import *
from lib.readable_entry_finder import *
from lib.todo_list import *
from lib.todo import *

"""
When i add multiple diary entries
#all lists them out in the order created
"""
def test_adds_and_lists_entries():
    diary = Diary()
    entry_1 = DiaryEntry('First Entry', 'Hello diary, what a way to start')
    entry_2 = DiaryEntry('Second Entry', 'This is going well')
    entry_3 = DiaryEntry('Third Entry', 'My number is 07000000000')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]

"""
When i add multiple tasks
And i dont mark any complete
#all_incomplete lists them in the order added
"""
def test_incomplete_returns_incomplete_todo_list_with_two_incomplete():
    todo_list = TodoList()
    todo_1 = Todo('Walk the dog')
    todo_2 = Todo('Feed the cat')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]

"""
Given 2 instances of todo
If 1 instance is complete
#incomplete returns only incomplete todo
""" 

def test_mixed_incomplete_complete_todos_incomplete_returns_incomplete_only():
    todo_list = TodoList()
    todo_1 = Todo('Walk the dog')
    todo_2 = Todo('Feed the cat')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()
    assert todo_list.incomplete() == [todo_1]

"""
Given 2 instances of todo
If 1 instance is complete
#complete returns only complete todo
"""

def test_mixed_incomplete_complete_todos_complete_returns_compelte_only():
    todo_list = TodoList()
    todo_1 = Todo('Walk the dog')
    todo_2 = Todo('Feed the cat')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_2.mark_complete()
    assert todo_list.complete() == [todo_2]

"""
Given 3 instances of todo
If all instances are incomplete
#give_up marks both complete
"""    

def test_give_up_marks_all_incompelte_todos_complete():
    todo_list = TodoList()
    todo_1 = Todo('Walk the dog')
    todo_2 = Todo('Feed the cat')
    todo_3 = Todo('Clean the house')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_list.give_up()
    assert todo_list.complete() == [todo_1,  todo_2, todo_3]

"""
When i have multiple diary entries
and i call #phonenumhberextractor
i get a list of all of the phone numbers from all diary entries
"""
def test_phone_number_extractor_extracts_correct_number():
    diary = Diary()
    entry_1 = DiaryEntry('First Entry', 'Hello diary, what a way to start')
    entry_2 = DiaryEntry('Second Entry', 'This is going well')
    entry_3 = DiaryEntry('Third Entry', 'My number is 07000000000')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract_numbers() == ['07000000000']

"""
When i have multiple diary entries
and i call #phonenumhberextractor
it ignores non valid numbers
"""
def test_phone_number_extractor_ignores_invalid_numbers():
    diary = Diary()
    entry_1 = DiaryEntry('First Entry', 'Hello diary, what a way to start 7893847')
    entry_2 = DiaryEntry('Second Entry', 'This is going well 07834')
    entry_3 = DiaryEntry('Third Entry', 'My number is 07000000000')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract_numbers() == ['07000000000']

"""
When i have multiple diary entries
and i call #phonenumhberextractor
it ignores duplicates
"""
def test_phone_number_extractor_ignores_duplicates():
    diary = Diary()
    entry_1 = DiaryEntry('First Entry', 'Hello diary, what a way to start 07000000000')
    entry_2 = DiaryEntry('Second Entry', 'This is going well 07000000000')
    entry_3 = DiaryEntry('Third Entry', 'My number is 07000000000')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract_numbers() == ['07000000000']

"""
When i add one diary entry that fits in the time
and i call #readableentryfinder
with a wpm of 2 and minutes of 2
it gets the diary entry
"""
def test_readable_entry_finder_works_single_readable_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Title', 'One two three four')
    diary.add(entry_1)
    readable_entry = ReadableEntryFinder(diary)
    assert readable_entry.extract(2, 2) == entry_1

"""
When i add one diary entry that does not fit in the time
and i call #readableentryfinder
with a wpm of 2 and minutes of 2
it returns none
"""
def test_readable_finder_works_for_entry_does_not_fit():
    diary = Diary()
    entry_1 = DiaryEntry('Title', 'One two three four five')
    diary.add(entry_1)
    readable_entry = ReadableEntryFinder(diary)
    assert readable_entry.extract(2, 2) == None

"""
When i add multiple diary entries, one readable
and i call #readableentryfinder
with a wpm of 2 and minutes of 2
it returns the readable entry
"""
def test_readble_works_for_2_entries_if_1_readable():
    diary = Diary()
    entry_1 = DiaryEntry('Title', 'One two three four five')
    entry_2 = DiaryEntry('Title', 'One two three four')
    diary.add(entry_1)
    diary.add(entry_2)
    readable_entry = ReadableEntryFinder(diary)
    assert readable_entry.extract(2, 2) == entry_2

"""
When i add multiple diary entries, multiple readable
and i call #readableentryfinder
with a wpm of 2 and minutes of 2
it returns the longest readable entry
"""
def test_readable_finds_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry('Title', 'One two three four five six')
    entry_2 = DiaryEntry('Title', 'One two three four')
    entry_3 = DiaryEntry('Title', 'One two three')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    readable_entry = ReadableEntryFinder(diary)
    assert readable_entry.extract(2, 2) == entry_2

