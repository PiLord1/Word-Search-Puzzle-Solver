# Word Search Puzzle Solver
_Project idea by Sir Darvy Ong_

In this project, a program was developed that would automatically solve a word search puzzle. The puzzle itself and the list of words to search will be provided by the user. The program then searches for each word in the puzzle until all the words have been found. It then displays the solution to the puzzle.

The puzzle is laid-out as a 2D grid with the origin (0,0) at the top-most left part, as shown on the figure. The solution to each word is indicated by (row,col) - direction where row,col are the row,col indices of the first character in the word in the puzzle, and then the direction to traverse the rest of the word . For example, in the board above, the solution to the word BATMAN is indicated as (12,1) - up, SUPERMAN is (4,1) - right-down, STORM is (12,11) - left and SPIDERMAN is (11,3) - right-up.

![image](https://github.com/PiLord1/Word-Search-Puzzle-Solver/assets/51207250/d486ad0b-13d4-4c18-88d6-43b9917fb96d)

Here is a **video demo**: https://youtu.be/-rlgEueerH8

The program can be divided into two distinct parts, namely puzzle input and puzzle solving.


## PART 1: Data Inputs
### Fetching, Sorting, and Printing Words
Ask the user for a number, **n**, that will determine the number of words that will be given to you. Store these words in a list named ‘words’. Use the _get_words()_ function to ask and store the words given by the user. The words will have a length no longer than 15 characters.

After the words have been saved, call the _sort_words()_ function. This function sorted the words alphabetically, starting from a to z. The sorted words should still be in the ‘words’ array.

The sorted words array should then be printed on the terminal using the _print_words()_ function. Only one word per line should be printed.

#### Functions created:
* _get_words(n, words)_ - asks the user to input the words and stores them into the list, words.
* _sort_words(n, words)_ - sorts the words array alphabetically using pythons inbuilt sort function
* _print_words(n, words)_ - prints the contents of the words list

![image](https://github.com/PiLord1/Word-Search-Puzzle-Solver/assets/51207250/0258bc34-321e-4d25-99f3-8c840f6641d3)

### Fetching and Printing the Board
Ask the user for another integer, **m**, that will be used to create the mxm _board_ list. The board should be populated by calling the _populate_board()_ function, where the user will be prompted values for the board row by row. The input may be a mixture of large or small letters, and I converted them all into capital letters. Assume that inputs will only include alphabetic characters. After populating the board, the _print_board()_ function showed the board on the screen. An example is shown below.

#### Functions created:
* _populate_board(m, board)_ - asks the user for inputs and saves them onto the board row by row.
* _print_board(m, board)_ - prints the contents of the board onto the terminal.

![image](https://github.com/PiLord1/Word-Search-Puzzle-Solver/assets/51207250/6e512c58-18e3-4fd2-ba3e-be65f8fa271e)


## PART 2: Word Search Solver

Now, since I’ve already created a means for initializing the board and entering the words to search, it is time to create the algorithm for searching the words. My algorithm followed the following conventions:
* Origin (row 0, col 0) should be located at the top most left cell of your board.
* It is assumed that the word search can be completed by looking for the words in the following directions: left, right, up, down, and the four diagonals. There will be no instances where the word cannot be found in a straight line on the board.

_Search_words()_ function was used to find the starting position and direction of the words in the words array. Indexes for direction followed the following format:
* dir_x - directions for x (-1 for left, 0 for neither, and 1 for right)
* dir_y - directions for y (1 for up, 0 for neither, and -1 for down)

#### Functions created:
* _search_words(m, board, n, words, solutions)_ - searches the board for the words, and saves each words position and direction in the solutions dictionary.
* _print_solutions(solutions)_ - prints the solutions following the format given above.

_Note:_ No word will be a subset of another word. e.g. hell and hello, snow and snowman, etc.

![image](https://github.com/PiLord1/Word-Search-Puzzle-Solver/assets/51207250/1fe1dc9a-315a-4abc-817a-abb7ccc7b4ce)


