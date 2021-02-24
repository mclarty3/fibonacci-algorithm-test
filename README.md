# fibonacci-algorithm-test
Tests the efficiencies of a few different algorithms for calculating numbers in the Fibonacci sequence

# Description
I used recursion to find the nth number of the Fibonacci sequence for a HW problem and my professor said it was inefficient, so I thought it'd be fun 
to have a closer look at how efficienct it and other algorithms were.

I implemented the following algorithms:
* Recursive algorithm: Just your run of the mill recursive algorithm to find F(n). If n > 2, return F(n - 2) + F(n - 1), otherwise return 1
* Simple while loop: Sums up the numbers in a loop to find F(n); no recursion needed!
* Closed form equation: The basic closed form equation to find F(n), derived using the golden ratio (Binet's formula)
* Matrix exponentiation: I tried a few ways of doing this and settled on shamelessly stealing the code from [StackOverflow](https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series/23462371#23462371)

# Results
So it turns out my professor was right and recursion is a _horrendously_ inefficient way of calculating numbers in the Fibonacci sequence. Surprise surprise.

![Results from the test](Results.png?raw=True "Test")

I won't get into the technical time complexity, but just looking at the graph it seems that the time for the recursive algorithm increases at about 2<sup>n</sup>,
while for the basic loop it increases linearly, and matrix multiplication and Binet's formula take constant time. I ended up completely omitting any results from the recursive algorithm after n = 20, as it skewed the graph pretty substantially. For n > 40, using recursion becomes more or less infeasible.

I'm not totally sure how to interpret the random spikes; I'm guessing that's just my computer taking a little extra time to do something else while the algorithms
are running. I keep my poor CPU pretty busy.

I probably won't do anything else with this, but I had fun staying up late to make it.
