# Explanation 

To make things faster, we can use a technique called prefix sum optimization. The idea behind prefix sum optimization is to precompute and store the prefix sum of the array in a separate array. The prefix sum of an array is simply the sum of all the elements from the start of the array up to the current index. For example, if you have an array [1, 2, 3, 4, 5], the prefix sum array would be [1, 3, 6, 10, 15].

# Usage

https://www.hackerrank.com/challenges/crush/problem?h_r=next-challenge&h_v=legacy&isFullScreen=true  <--- try it out here

the example below is:
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example

Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of
between the indices and

inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]

The largest value is

after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below.

arrayManipulation has the following parameters:

    int n - the number of elements in the array
    int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

Returns

    int - the maximum value in the resultant array

Input Format

The first line contains two space-separated integers
and , the size of the array and the number of operations.
Each of the next lines contains three space-separated integers , and , the left index, right index and summand. 

# code snippet 

```go
func arrayManipulation(n int32, queries [][]int32) int64 {
    arr := make([]int64, n)
    var max int64

    for _, query := range queries {
        a := query[0] - 1 // Adjust indices to be 0-based
        b := query[1] - 1
        k := int64(query[2])
        arr[a] += k
        if b < n-1 {
            arr[b+1] -= k
        }
    }

    var sum int64
    for _, val := range arr {
        sum += val
        if sum > max {
            max = sum
        }
    }

    return max
}
```