## Shortest Unique Prefix
Given a list of N words. Find shortest unique prefix to represent each word in the list.
NOTE: Assume that no word is prefix of another. In other words, the representation is always possible

### Constraints
```
1 <= Sum of length of all words <= 1e6
```

### Examples
###### Input
```
 A = ["zebra", "dog", "duck", "dove"]
```
###### Output
```
 ["z", "dog", "du", "dov"]
```
###### Explanation
```
 Shortest unique prefix of each word is:
 For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
 For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
 For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
 For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog". 
```