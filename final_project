
import tkinter as tk
from PIL import Image, ImageTk 
import pandas as pd
import os

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800
image_dir= "/Users/emersonfatzinger/Desktop/bcog200/Final_Project_folder/"
instructions = image_dir+ "instructions.csv"
question_dir = "/Users/emersonfatzinger/Desktop/bcog200/Final_Project_folder/questions_file/"

#quiz_questions="/Users/emersonfatzinger/Desktop/bcog200/Final_Project_folder/project_questions.csv"
# learn how to make this available for everyone who takes the quiz'''

class Questions:
    def __init__(self, folder_path):
        self.questions = self.load_questions_from_folder(folder_path)
        self.current_q = 0

    def load_questions_from_folder(self, folder_path): #Emerson
        #get the code from CSV files located within our folder 
        #AI Attribute CHAT GBT I asked for assistance on how to load of csv files into printatble questions that we present for our quiz
        # It suggested we strip the files and put them into a dictonary
        questions = []
        files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])
        for filename in files:
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
                if len(lines) >= 2:
                    question_text = lines[0]
                    options = {}
                    for line in lines[1:]:
                        if line[1] == '.':
                            key = line[0].upper()
                            value = line[3:].strip()
                            options[key] = value
                    questions.append({
                        'question': question_text,
                        'options': options
                    })
        return questions

    def get_current_question(self): 
        #show which question is next and checks to see when the quiz is over
        if self.current_q < len(self.questions):
            return self.questions[self.current_q]
        else:
            return None

    def next_question(self):
        #counter
        self.current_q += 1

    def is_finished(self):
        return self.current_q >= len(self.questions)


class Display:
 
    def __init__(self,root, questions_obj):
        self.root=root #tkinter root window
        self.root.title("Illini Archetype Quiz")
        self.root.geometry("1000x800")

        self.archetype_scores = {
            'class': 0, 'social': 0, 'grainger': 0, 'crush': 0}
        #self.questions = pd.read_csv(quiz_questions)
        self.questions_obj = questions_obj
        

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True) 

        self.show_instructions()


    def clear_container(self): #haley
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_instructions(self): #haley
        self.clear_container()
        #we are choosing to make our intructions just a print statement so anyone can use the quiz and they dont have to have the file already saved on their device 
        instructions_text = "Welcome to the Illini Archetype Quiz! You will be given a set of questions and you should choose your answer based on your personal preference. When you are ready to start, click next. Enjoy! \n\nClick Go to start."
        label = tk.Label(self.container, text=instructions_text, font=("Trebuchet MS", 25, "bold"), bg="dark orange", fg="blue", wraplength=900, justify="center")
        label.pack(pady=100, fill="both", expand=True)
        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)
        #create quit button
        quit_button = tk.Button(button_frame, text="Quit", command=self.root.destroy, padx=25, pady=15, bg='green', fg='black')
        quit_button.pack(side="left", padx=20)
        #create go button
        go_button = tk.Button(button_frame, text="Go", command=self.show_question, padx=25, pady=15)
        go_button.pack(side="right", padx=20)

    def show_quiz_page(self):
        self.clear_container()
        label = tk.Label(self.container, text=quiz_text, font=("Arial", 24), wraplength=900, justify="center")
        label.pack(pady=100, fill="both", expand=True)
        back_button = tk.Button(self.container, text="Back to Instructions", command=self.show_instructions, padx=20, pady=10)
        back_button.pack(pady=20)
    
    def show_question(self):  #Emerson
        self.clear_container()
        if not self.questions_obj.is_finished(): #if the quiz is not finished yet...
            q = self.questions_obj.get_current_question()
            question_text = q['question']
            options = q['options']

            label = tk.Label(
                self.container,
                text=question_text,
                font=("Arial", 18), 
                wraplength=400, 
                justify="left"
            )
            label.pack(pady=40)

            # Create a frame to hold the buttons
            # AI Assitance, make the buttons equal size but all fit the text correctly. 
            btn_frame = tk.Frame(self.container) 
            btn_frame.pack()

            keys = sorted(options.keys())
            for index, key in enumerate(keys):
                row = index // 2
                col = index % 2
                btn = tk.Button(
                    btn_frame,
                    text=f"{key}. {options[key]}",
                    font=("Arial", 16),
                    wraplength=350,
                    justify="left",
                    width=40,
                    height=8,
                    command=lambda k=key: self.handle_answer(k))
                btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # make the columns fit 
            for i in range(2):
                btn_frame.grid_columnconfigure(i, weight=1)

            back_button = tk.Button(
                self.container, 
                text="Back to Instructions", 
                command=self.show_instructions, 
                padx=20, pady=10
            )
            back_button.pack(pady=20)
        else:
            self.show_results()

    
    
    def handle_answer(self, selected_key): #haley 
        archetype_map = {'A': 'class', 'B': 'social', 'C': 'grainger', 'D': 'crush'}
        archetype = archetype_map.get(selected_key)
        if archetype:
            self.archetype_scores[archetype] += 1
        self.questions_obj.next_question()
        self.show_question()
    
    def show_results(self): #Emerson
        self.clear_container()
        winner_archetype = max(self.archetype_scores, key=self.archetype_scores.get)
        archetype_names = {
            'class': 'Class President',
            'social': 'Social Chair',
            'grainger': 'Grainger Addict',
            'crush': 'Orange Crush'}
        # Add descriptions 
        archetype_descriptions = {
        'class': "Congrats on being class president! This title means that you are a natural leader with the motivation to be the most accomplished. This archetype is active in various RSOs and can be found leading on the executive board. You'll use your time at UIUC to do great things in the future!",
        'social': "You are the life of the party! Your extroverted and fun loving personality will grant you countless memorable moments from your time at the University of Illinois. Your easy-going and welcoming demenor always invites new friends. The biggest lesson college taught you is how to have a good time...",
        'grainger': "Hey smarty pants! Your time at the University of Illinois may have been challanging, but all those all nighters are sure to be worth it. Your hard work will drive you to a successful carrer. We will be looking for your name on the next list of Nobel Prize winners.",
        'crush': "ILL-INI! You are no stranger to the jumbotron at State Farm Center. We know you are used to the spotlight, and will take this spirit and energy with you through the rest of your life. We know that will be found repping the Illini for generations to come "}
        result_text = f"You are most like: {archetype_names[winner_archetype]}!\n\n{archetype_descriptions[winner_archetype]}"

        label = tk.Label(self.container, text=result_text, font=("Ariel", 25), fg="#ff69b4", wraplength=900, justify="center")
        label.pack(pady=100)
        quit_button = tk.Button(self.container, text="Quit", command=self.root.destroy, padx=25, pady=15, bg='green', fg='black')
        quit_button.pack(pady=20)


                
def main():
    question_dir = "/Users/emersonfatzinger/Desktop/bcog200/Final_Project_folder/questions_file/"
    root = tk.Tk()
    questions = Questions(question_dir)
    app = Display(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
