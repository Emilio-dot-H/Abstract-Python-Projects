## Anagrams

Use Python and a dictionary file to find all the single-word anagrams for a given English
word or single name.

The problem is that the operator (==) considers two lists equivalent only if they have the same number of the same list items and those items occur in the same order. You can easily solve this problem with the builtin function `sorted()`, which can take a list as an argument and reorder its contents alphabetically.

## Phrase Anagrams

A Python program that lets a user interactively build an anagram phrase from the letters in their name.

A simple interface that prompts the user to input the initial
name, displays potential word choices, and displays any remaining letters. The program will also need to keep track of the growing anagram phrase and let the user know when every letter has been used. There will likely be lots of failed attempts, so the interface should allow the user to restart the process at any time.

### Using Counter()

Python ships with a module named collections that includes several container data types. One of these types, Counter, counts the occurrences of an item. Python stores the items as dictionary keys and the counts as dictionary values.

You can use Counter, instead of the `sorted()` method, to find single-word anagrams. Rather than two sorted lists, the output will be two dictionaries, which can also be directly compared with ==.

### Finding Voldemort: The British Brute-Force

Reduce the number of anagrams of tmvoordle to a manageable number that will still contain Voldemort.

- Filtering with Consonant-Vowel Mapping
- Filtering with Trigrams
- Filtering with Digrams