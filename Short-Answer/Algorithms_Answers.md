#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This uses a O(n) runtime, being that there is an n amount of times for n * n to run to reach n^3


b) This uses a O(nlogn) runtime, with the inner loop increasing at a much faster rate than the loop itself.


c) Bunnies uses a O(n) runtime, using a recursive call to move 1 down each call will run through the list once and end the program

## Exercise II



I would first find the middle of the list and if it does not break, I would make that the beginning of the new array. If it does break I would make it the end of the array. I would then recursively call the function again using the new array as the argument. I would repeat this until I find the only item left in the array, which would be the first floor that the egg would be broken, or f floor. Continually splitting the array would make this an O(logn) runtime.