Data Structure Justification:

The questions in this quiz were stored in a .json file for readability and ease of manipulation. It was structured to imitate the quiz, where for every question, the question is at the top and the answers listed one by one at the bottom. This way, it's obvious which answers belong to which questions, and which individual question is. This also makes it easy for me or others to add questions and answers, simply by following the format in the .json file. If I were to create another file for another quiz, this .json file would be available for use if I ever needed it.

Function Design:

The way retry() is structured is pretty simple. It takes user input and expects either yes or no, while also accepting those inputs in all lowercase or all uppercase. Answering yes restarts the quiz, answering no quits the quiz, and answering anything else creates an invalid message. This function allows the quiz to keep track of high scores and solves the problem of invalid inputs.

Control Flow:

The way this quiz handles invalid inputs for answers is to check answers in an if-statement. The condition is that the answer must be within the available/valid answers. If the answer is, then it skips the rest of the if-statement. If the answer does not meet the condition, it continues through the if-statement, which just prints a message saying the answer is invalid. This also allows the user to try again.

Use of AI:

In this quiz, I used the AI agent in VSCode to help me fix the issue of invalid answers (lines 34 - 38). It also helped me randomize the answers in each question so that they appeared in a different order after the quiz restarted (lines 27 - 29). Lastly, it helped me created a defined function that asked the user if they wanted to restart the quiz or not, only allowing yes or no inputs (lines 12 - 19, 53 - 54). I accepted these lines of code from the AI agent only after confirming they were within the bounds of what we've been learning so far. I also tested them to see if they worked.