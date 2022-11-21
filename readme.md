# Programming Task 2

## _ReviewMe_

![](https://i.ibb.co/ZByNPgZ/Review-Me.png)

Using the previous software as a foundation, ReviewMe is now looking for a program that will give customers a restaurant's score and/or rank the top n restaurants based on their average ratings, which ReviewMe independently determined as the sum of the average scores for food, wine, and atmosphere.

The data is stored in a file named scores.txt, which must be given into the program. Furthermore, only one entry should be entered in the file for each restaurant. Multiple lines corresponding to the same restaurant should likewise be considered an error.

## Features

1. Gives the score of a restaurant
2. Gives the Top restaurants dependant on user input
3. Extracts data from a read me file called scores.txt
4. Sorts the data
5. Dynamic solutions for incorrect input
6. If there are errors, program raises exception
7. User is able to exit the program

## Tech

ReviewMe rlies on a number of open source prerequisites to function:

- [Python](https://www.python.org/) - Python is a high-level, interpreted, general-purpose programming language.
- [Linux Bash](https://www.linux.org/) - Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.

## Installation

ReviewMe requires [Python](https://www.python.org/) v3.10.5 to run.

```sh
tar -zxf pt2.tgz
```

Check Python version & Installation

```sh
Check version
python --version

For windows - Download latest version from the official website:
https://www.python.org/downloads/

For Centos - use yum:
sudo yum install python3

For Ubuntu - use apt-get:
sudo apt install python3
```

## Running the Program

1. After initialisation of the program, the user is prompted to pick a selection from the menu to determine what they would like the program would do for them.
   ![](https://i.ibb.co/SmvHsWL/carbon.png)

2. If the user selects "1" the program will prompt the user to input the name of the restaurant, once the user does this, the program will print the restaurant name rating.
   ![](https://i.ibb.co/ryQnYxT/carbon-1.png)

3. If the user selects 2, the program will prompt the user to input the number of restaurants so it can print the top restaurants in descending order.
   ![](https://i.ibb.co/18ybX9R/carbon-2.png)

4. If the user selects 3, the program will exit.
   ![](https://i.ibb.co/HrGHQd5/carbon-3.png)

## Improvements to be made

I realised after completing the assignment that the rubric requests to use tuples instead of dictionaries. The end result is exactly the same. Other than that, I would really like to learn to use shorter and more efficient code, it seems as though I am repeating myself a lot in the functions, although this also makes them more tangible and modular if specific and individual changes were to be made.

Setting variables for numbers is also always a brilliant idea, which I implemented a few times but not throughout the assignment, this would allow for future improvements/modifications to be faster as you would only have to change the number of the variable instead of wading through the code to change individual values.

I would also like to undestand my code better, I am still in my early days and I find that I'm correcting and fiddling with the code a lot, trying many different things, by the end of what I have completed sometimes I look at a section and I don't fully comprehend it instantly, I have to work through it, relying heavily on comments.

## License

UNE
