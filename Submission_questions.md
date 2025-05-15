# Project Submission Questions 
### Which three functions or methods that you wrote are you proudest of/happiest with? For each of those three functions/methods, describe (briefly) why you like them.
Haley Trojan:
1. The first function I am proudest of is the 'def handle_answer(self, selected_key)' method. Overall, this function includes the code to process the participant's
answer, updates the archetype output, and continously evolves the quiz. The function starts by setting up a dictionary to locate each answer choice and proceeds to
update the final output, based on chosen answer to each question. It also advances the quiz by collecting the score and moving onto the next question.
I am very happy with how this function ran because the logic is unique and the code is simple, yet straight-forward.
2. The second function I am proudest of is the 'def show_instructions(self)' method, specifically the lines that include the "go" and "quit" buttons. It does not only
place these buttons on the display screen, but it also correctly calls "show_question" to start the quiz and creates a 'quit' button to close the application.
Even though these are quite simple commands, we experienced errors and challenges when trying to run the program. Asking many questions and getting various outside
opinions, helped us solve the problem to make the code run efficiently. I am happiest with this function because it was an example of overcoming challenges.
3. The third function I am proudest of is the 'def clear_container(self)' method. Even though this function is pretty short, it is immensely impactful.
When we started this project, each screen would remain displayed until the 'quit' button was pressed. This served as an imposition because as you moved onto the next
section of the quiz, the previous page would still be visible. This function removed all widgets (like buttons, questions, and answers, etc.) and ensured the
container is emptied before new content is added. I am happiest with this function because it adds a sense of cleanliness and simplicity to our project.

Emerson Fatzinger:
1. 
2. 
3. 

### Describe if you went above and beyond on the minimal project requirements and challenged yourself to approach a project that is more complex than the basic requirements, required you to learn something beyond what was taught in the course, or used code concepts not taught in class. 

One of the most challenging and distinctive aspects of this quiz application's logic is its ability to dynamically load and parse questions from multiple CSV 
files, standardize them, and present them interactively within a single Tkinter window. This requires reliable file handling and flexible parsing to ensure only 
valid questions are used, regardless of how many CSVs are added or how they're structured. The scoring system is straightforward yet adaptable, mapping each answer 
to an archetype and quickly determining the user's dominant type at the end. By separating data management from the user interface and allowing quiz content to be 
updated simply by adding new files, the logic is both impactful and flexible.
