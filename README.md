# Outline for Final Project 
1. Our project is going to be a persoanlity quiz based on the arcetype of UofI students. The user will be prompted certain questions where they will answer based on their personality. Each question will measure a different quality of their personality, that will be included in the overall result. The answers they give will determine which archetype the user gets. 
2. 
- Mainloop function. This function will loop through the entirety of the questions and calculate the final score, based on the collection of answers. 
- Input() Function. This function will be used to gather information throughout the course of the quiz. It will allow us to format a string that will put the user's input directly into the output.
- Dictionaries. This function will store questions, options, and scores. This will make the data more organized and allow easy retrieval of the information during the quiz.
3. Haley Trojan: haleytrojan1 , Emerson Fatzinger: emersonfatz
4. 
- This project will be split up in portions of the project. To start, the first portion will cover all of the introductory input. This includes the instructions, purpose, and cover desgin of the project. The second portion will include the questions and answers. 
- We will create a seperate csv file containing the quesitons and answers, that we could potentially input into load functions. The final portion will contain the results of the quiz. The results will be calculated from point logic behind each answer to all the questions. Emerson and I plan to work on each section together. 

## Outline of Functions: 

Def load questions(questions_file):
This function would take in the parameter of the file with our list of questions and would load them into a tuple

### Quesitons that will be in csv file:
1. **Its syllabus week, how do you choose to spend your time**
- A. You can find me at my RSOs table on quad day (class president)
- B. It's not a real week… let's  have fun! (social chair)
- C. It's the perfect time to get ahead on work before things get busy (grainger addict)
- D. Grabbing a pair of striped overalls from the bookstore.. Football season is coming up! (orange crush)

2. **What dorm did you live in freshman year** 
- A. Bromley (the social chair)
- B. ISR (grainger addict)
- C. Six pack (orange crush) 
- D. LLC (class president) 

3. **How do you like to spend a thursday night** 
- A. I never miss a thursday night Joes duh (social chair)
- B. Karaoke at the union (class president) 
- C. In bed of course…it’s a school night (grainer addict)
- D. Playing on my intramural team (orange crush)

4. **It's halloweekend at u of i which costume are you picking?**
- A. The mascot (orange crush) 
- B. "C-" the scariest thing i can think of (class president) 
- C. Party animal (social chair) 
- D. Harry potter (grainger)

5. **How do you like to get your work done?**
- A. Why wait around? Get it done right away (grainger)
- B. I’ll get around to it at some point… (orange crush)
- C. Probably turned in late, but at least it's done (social chair)
- D. I fit it in between my extracurricular events (class president)

6. **Dr. Uddenberg is hosting a Kahoot in class. What avatar are you choosing?**
- A. The unicorn (social chair)
- B. The brain (grainger)
- C. The pumpkin (orange crush) 
- D. The dog (class president)

### Coding Outline 
- Def print instructions(instructions_file):
This function would read and print the instructions to the user 

**Instructions draft:**

- "Hello! Welcome to the University of Illinois Archetype Quiz! This quiz will measure your personality based on a series of questions. Go through each question and click the answer that best applies to you. At the end of the quiz, you will receive a UIUC student archetype. Have fun!"

- Def administer_quiz(question_tuple):
This function would take in the tuple of questions that we made earlier, then one by one ask the questions and allow the user to input their answer. It would the store the answers to a list. 

- Def calculate_score(questions_tuple, answer_list):
This function would take in the parameters of the data already taken and use it to calculate a persons score and result. 

- Def print result(final_score):
This page would be similar to print instructions in the way that it displays the users final score

- main()

### 📥 Download All CSV Files (Recommended Method)

All required csv files will be located in data/questions_file/

To get all the `.csv` files needed to run the project, clone the entire repository using:

```bash
git clone https://github.com/your-username/your-repo.git





