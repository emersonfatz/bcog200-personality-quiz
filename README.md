**Our project is going to be a persoanlity quiz based on the arcetype of UofI students. The user will be prompted certain questions where they will answer based on their personality. Each question will measure a different quality of their personality, that will be included in the overall result. The answers they give will determine which archetype the user gets. 
a. Mainloop function. This function will loop through the entirety of the questions and calculate the final score, based on the collection of answers.        b. Input() Function. This function will be used to gather information throughout the course of the quiz. It will allow us to format a string that will put the user's input directly into the output.                                                                                                                          c. Dictionaries. This function will store questions, options, and scores. This will make the data more organized and allow easy retrieval of the information during the quiz.
Haley Trojan: haleytrojan1 , Emerson Fatzinger: emersonfatz
This project will be split up in portions of the project. To start, the first portion will cover all of the introductory input. This includes the instructions, purpose, and cover desgin of the project. The second portion will include the questions and answers. We will create a seperate csv file containing the quesitons and answers, that we could potentially input into load functions. The final portion will contain the results of the quiz. The results will be calculated from point logic behind each answer to all the questions. Emerson and I plan to work on each section together. 

Outline of Functions: 

Def load questions(questions_file):
This function would take in the parameter of the file with our list of questions and would load them into a tuple

Def print instructions(instructions_file):
This function would read and print the instructions to the user 

Def administer_quiz(question_tuple):
This function would take in the tuple of questions that we made earlier, then one by one ask the questions and allow the user to input their answer. It would the store the answers to a list. 

Def calculate_score(questions_tuple, answer_list):
This function would take in the parameters of the data already taken and use it to calculate a persons score and result. 

Def print result(final_score):
This page would be similar to print instructions in the way that it displays the users final score

main()



