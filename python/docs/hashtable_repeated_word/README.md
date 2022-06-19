# Challenge Summary
Write a function called first_repeated_word that finds the first word to appear more than once in a string.

## Whiteboard Process
![whiteboard](White Board.png)

## Approach & Efficiency
[Code](/code_challenges/hashtable_repeated_word.py)
* BigO for Time is O(1) due to the rapid lookup nature of a dictionary.
* BigO for Space is O(1) since the call stack is being used minimally.
* Create a function that takes in text as a string and returns the first repeated word or None if one is not found.
* Create a dictionary for holding the words
* Create a regex pattern and use it to transform a string sans punctuation except for in word joins. Lower that
  string to all lowercase and split it into separate words.
* Loop through the string word by word
  * Check if each word is already in the dictionary
  * If a word is not found to be in the dictionary, add that word to the dictionary.
  * If the word already exists in the dictionary, return the word
