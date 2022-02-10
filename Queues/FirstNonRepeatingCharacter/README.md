## First non-repeating Character
Given a string A denoting a stream of lowercase alphabets.
You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. if no non-repeating character is found then append '#' at the end of B.

### Constraints
```
1 <= |A| <= 1e5
```

### Examples
###### Input 
```
A = "abadbc"
```
###### Output
```
"aabbdd"
```
###### Explanation
```
"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
```