# 2018_10_02_1538493733 - Lattice Paths

I won't try to top the explanation provided [here](https://gist.github.com/mizhi/d89387031af1b59c10a4134a9eaf0628).
```text
This problem has the properties of having optimal substructure
and overlapping sub problems. Meaning, if we have the optimal
solution for smaller parts of the problem, we can compute
the optimal solution for the containing problem.

We compute the path count using a dynamic programming algorithm.

We recognize that the number of ways to get to each position
is the sum of the number of ways to get to the position to
the left of the current position and the number of ways to
get to the the top of the current position.

Because we restrict movement to right and down, we know
that the left column and the top row are all 1s. There is
only one path to get to any of these positions.

Therefore, we simply need to fill in the rest of the matrix and
retrieve the count in the bottom right cell.

In this setup, can make a matrix that represents the
number of paths it takes to get to each position on the
grid. In a 2x2 graph, traversing along the edges, this means
there are (2+1) x (2+1) positions to account for.

The first part of this code initializes a matrix.
The second part builds the counts.

Runtime: O(2n) = O(n) where n is width * height or the number
of positions.
```