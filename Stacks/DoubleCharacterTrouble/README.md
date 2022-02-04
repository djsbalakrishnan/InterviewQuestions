## Double Character Trouble 

### Problem Description 
```
You are given a string A.
An operation on the string is defined as follows:
Remove the first occurrence of same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".
Therefore the string after this operation will be "acd".
Keep performing this operation on the string until there are no more occurrences of same consecutive characters and return the final string.
```

### Problem Constraints 
`1 <= |A| <= 100000`

### Example Input 
```
Input 1:
A = abccbc

Input 2:
A = ab
```

### Example Output 
```
Output 1:
"ac"

Output 2:
"ab"
```