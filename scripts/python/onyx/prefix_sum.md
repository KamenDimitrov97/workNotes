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


kubectl patch cronjob fat-mnt-manual-recalculate-permissions-table -n fat-mnt-dev -p '{"spec" : {"suspend" : true }}'

kubectl get pods -n <namespace> | grep <cronjob - fat-mnt-manual-recalculate-permissions-table> | awk '{print $1}' | xargs kubectl delete pod -n <namespace>


aplication designed for custom office to track coming and going of packages and things like that through customs 

aub got 2 of the main areas prototyped they will finish the actual application 
offering support, passing on any knowledge, training and giving support to these guys 
how to deploy docker
CI/CD 
they don't use the same repo on gitlab 
azure devops repo setup there not anything functionaly has changed 
some of the layouts have changed 

Requirements:
- need an asm account 
- warp-cli - one.one.one.one.com
- cloudfare zero- instead use warp-clie connect and disconnect won't be able to work with other internet 


warp-cli teams-enroll asm aeos-platform
one of the themes - aubegine 
other of the themes - aeos

3 parts:
aeos-platform/website - that's the frontend - vue application 
winform-component-library - wintext field, wintable, different components base component library - generics
aeos-component-library - extends winform-component library and calls it a new name inherits almost all of the winform components -specific to this application 
work across all 3 repos - if something needs to be used alot then try implementing 

sequioa - was the original app before aubergine current application by the clients they're actually using it 
we did a replica of 2 3 forms as ASM are taking over this project 

aeos.component-libary
winform-component-librar
wintextfield.vue

wintextfield.ts - defines props interface, props for the input, 

scss variables are stored src/default.ts

NPM run storybook - documentation on components that we have I can test out some changes here 

to see how the component behaves in the platform - you'll have to build the platform
setup aubergine version while waiting for access rights

ask phil for credentials to ASM
a declaration is just a form - everything is a declaration

headers and other tabs (items)
ncts/departures
ncts/arrivals you can right click and open the declaration 
playwright handles opening new tabs

arrival bugged that at first isn't recognizing the data field initially 
I'll be using latest version of component libararies 
if you want to do dev changes to winform or library

1. setup npm link -make this winform component libarary available to my local package manager 
2. then npm run build
3. take the name from the build and say 
4. npm link build name 
5. npm ls - verify locations of node packages 
6. change version 
7. do the same for aubergine-lib
8. npm link winform-build-version aubergine-winform-build-version in the platform
9. verify npm ls


how to unlink 
npm install will change your packagelock
npm unlink winform-build-version aubergine-winform-build-version 


vue official 
pretty typescript errors
git lens
eslint
yaml
peacock
probably not gonna be able to access the platform due to no access rights 

talk to Phil about aubergine
