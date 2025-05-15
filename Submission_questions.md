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
1. One of the functions I am proudest of is the show_questions function. As we started the project one of our most major roadblocks was actaully figuring out how to
get each questions to display one after another. This was a concept that I had to put in a lot of research and time in tutoring to figure out but once it worked, it was very exciting. Understanding how to get the questions from the csv files into a dictonary and getting them to present in the form of clickable answers was quite daunting but a fun task to get through. Getting the answer options to show up on the buttons was something that went through so many trial phases but I had a vision for what i wanted it to look like and im really glad I was able to achieve it by constantly tweaking the size and framining of our buttons. 
2. The other function I am really proud of is the show_results function. While this function wasnt necessarily the hardest one to complete out of the entire project, I had some of the most fun figuring this one out because it felt like one of the final creative stepping stones that I had to finish. For this section, msot of the calculating had been done in earlier functions, so it was really enjoyable to get to come up with creative descriptions for each of the archetypes. Im really happy with how the descriptions came out and whenever I make a friend take the quiz I love when they finally get to this screen and get to read the result, not only of their answering, but of our hard work. 
3. The function I would say I am overall the proudest of is the load_questions_from_folder function. As I mentioned previosuly it seemed like an impossible task to get our questions from the csv file to the exact order we wanted in our project. There was a lot of different ideas thrown around to how we would do this. An inital idea was to have a function for each questions and manually put the questions and answer choices in, although this would have been quite simple, I knew I wanted to figure out how to load all the CSV files into one. I used a lot of ideas from our final unit when it came to stripping the files. But after a lot of researching, failing, and being overall very confused this function got done. It was a major roadblock that we had to tackle pretty early on in our project and im very proud of how it turned out. 
### Describe if you went above and beyond on the minimal project requirements and challenged yourself to approach a project that is more complex than the basic requirements, required you to learn something beyond what was taught in the course, or used code concepts not taught in class. 

One of the most challenging and distinctive aspects of this quiz application's logic is its ability to dynamically load and parse questions from multiple CSV 
files, standardize them, and present them interactively within a single Tkinter window. This requires reliable file handling and flexible parsing to ensure only 
valid questions are used, regardless of how many CSVs are added or how they're structured. The scoring system is straightforward yet adaptable, mapping each answer 
to an archetype and quickly determining the user's dominant type at the end. By separating data management from the user interface and allowing quiz content to be 
updated simply by adding new files, the logic is both impactful and flexible.
