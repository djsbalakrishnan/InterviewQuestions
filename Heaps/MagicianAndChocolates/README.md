## Magician and Chocolates
Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that kid can eat in A units of time.

NOTE:
- floor() function returns the largest integer less than or equal to a given number.
- Return your answer modulo 1e9+7


#### Constraints
```
1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 1e5
```

#### Example Input
```
 A = 5
 B = [2, 4, 6, 8, 10]
```

#### Example Output
```
 Maximum number of chocolates that can be eaten is 33.
```
