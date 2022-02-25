## Spelling Checker
Given an array of words A (dictionary) and another array B (which contain some words). You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present. Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if it is not.
Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

NOTE: Try to do this in O(n) time complexity.

### Constraints
```
1 <= |A| <= 1000
1 <= sum of all strings in A <= 50000
1 <= |B| <= 1000
```

### Examples
###### Input
```
A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
```
###### Output
```
[1, 0]
```
###### Explanation
```
Only "cat" is present in the dictionary.
```