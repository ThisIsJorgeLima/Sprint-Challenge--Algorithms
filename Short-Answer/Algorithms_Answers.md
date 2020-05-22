#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

## Answer:

Our runtime for our third analysis is a runtime of O(n): This uses recursion, which calculates the number of ears for n bunnies. If the number of bunnies were to increase, our recursive calls would increase as well.
+--------------------------------------------------------+      
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

        Answer:

Our runtime for our second analysis is a runtime ofO(n^2): Because we have two loops, and one is nested. Our inputs are being iterated n*n times.
+--------------------------------------------------------+      
c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

## Answer:

Our runtime for our third analysis is a runtime of O(n): This uses recursion, which calculates the number of ears for n bunnies. If the number of bunnies were to increase, our recursive calls would increase as well.

+--------------------------------------------------------+

## Exercise II

Question:
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

+--------------------------------------------------------+
## Answer:

n-story would be our max number of floors—the base case we cannot cover the f with zero eggs regardless of an infinite amount to be thrown. We will need to find a minimum value using binary search. That way, we can divide a large array into two smaller sub-arrays.

We would circumscribe the middle floor within the highest possible. The probability of an egg breaking is greater since one can break simply falling off my kitchen counter.

However, let's say our egg didn't break from the middle floor. We could use this as our benchmark as our lowest possible and retest our thesis.

Before retesting, one would need to consider the lowest of possibilities. Maybe the shortest was one floor below the highest level. If it were, we would stop there and record that as our faintest possibility of tossing an egg from such height without having it break.

In conclusion, this is truly a binary search solution. One would conclude that our runtime would be O(log n).
