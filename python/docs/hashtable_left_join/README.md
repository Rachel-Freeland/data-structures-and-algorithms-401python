# Hashmap LEFT JOIN
Using the hashtable implementation that I made, I will write a function that performs a LEFT JOIN on 2 hash tables.

## Challenge
Write a function called left_join that takes in 2 hashmaps. The first hashmap has word strings as keys, and a
synonym of the key as values. The second hashmap also has word strings as keys, and antonyms of the key as values.
Return a data structure that holds the result.
* Combine the key and corresponding values(if they exist) into a new data structure according to LEFT JOIN logic.
* If no values exist in the right hashmap, then some flavor of "NULL" should be used and appended to the result row.

## Approach & Efficiency
* [Code](/code_challenges/hashtable_left_join.py)
* BigO is O(n) for both Time and Space Complexity

![left join](Screen%20Shot%202022-06-20%20at%2010.52.31.png)
