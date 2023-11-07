- Student Name: [Muhammad Zayan Khan]
- Student CIS ID: [001061023]

For this coursework we want to create a very simple C program that takes a number as an input and returns the perimeter of a sequence of squares.

The rectangle is aranged as follows:

![rectangles](https://upload.wikimedia.org/wikipedia/commons/d/db/34%2A21-FibonacciBlocks.png)

The image shows 8 squares with a side length of of 1, 1, 2, 3, 5, 8, 13 and 21 respectively. If we sum up the perimeters of these squares we get : 4 * (1 + 1 + 2 + 3 + 5 + 8 + 13 + 21) = 216

In perimeter.c write a function that gives the sum of the perimeters of n+1 such squares.

Hint: You may want to have a look at the Fibonacci sequence.

1. Add your name and CIS ID to this file.
2. Write the function perimeter(int n) in perimeter.c (20 marks)
3. Ensure that all tests in the tests folder run successfully. (5 marks)
4. Write a Makefile for the project in Makefile (10 marks). For full marks the makefile should automate finding and linking files so that the addition of new files does not "break" the makefile. It should have the following options 
      - all: create an executable called perimeter that takes a number n as an input and returns the sum of the perimeters of n+1 squares
      - clean: remove all executables
      - test: manually run the tests in test
5. Currently the tests could be passed by simply assigning the correct value to each of the 4 inputs. Add a test to tests/test.c that resolves this issue. (5 marks)
6. Code is clean and easy to read and does not contain unneeded variables, etc., README has been edited (10 marks)



edited perimeter.c:

A  integer array F3 with a size of 1000000000 is initialised. .First, the code initialises variables p and sum to 0 within the perimeter function.The printf and scanf routines are used by the programme to ask the user to enter a number through the terminal.If the input {n} is smaller than zero, the function checks for it. The method returns 0 if it is. The function returns 4 in case {n} is smaller than 2.The code then uses a Fibonacci sequence calculation to fill the array {F3}, where each element is the sum of the two earlier elements. The code first determines how many elements are in the array {F3}, then adds them all up.In the end, the perimeter is determined by multiplying the total of the array items by four and allocated to the variable {p}. The perimeter function then returns this value.








Total marks: 50
