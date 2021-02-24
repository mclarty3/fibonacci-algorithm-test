# fibonacci-algorithm-test
Tests the efficiencies of a few different algorithms for calculating numbers in the Fibonacci sequence

# Description
I used recursion to find the nth number of the Fibonacci sequence for a HW problem and my professor said it was inefficient, so I thought it'd be fun 
to have a closer look at how efficienct it and other algorithms were.

I implemented the following algorithms:
* Recursive algorithm: Just your run of the mill recursive algorithm to find F(n). If n > 2, return F(n - 2) + F(n - 1), otherwise return 1
* Simple while loop: Sums up the numbers in a loop to find F(n); no recursion needed!
* Closed form equation: The basic closed form equation to find F(n), derived using the golden ratio
* Matrix exponentiation: I tried a few ways of doing this and settled on shamelessly stealing the code from StackOverflow

# Results
So it turns out my professor was right and recursion is a _horrendously_ inefficient way of calculating numbers in the Fibonacci sequence.
![results](https://github.com/mclarty3/fibonacci-algorithm-test/blob/master/results.png?raw=true)
