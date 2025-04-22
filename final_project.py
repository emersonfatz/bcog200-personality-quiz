import project_questions.csv as project_questions

def load_questions(project_questions): #haley
    question_list = []
    
def print_instructions(project_questions): #emerson
    with open(project_questions, 'r', encoding='utf-8') as file:
        instructions = file.read()
        print(instructions)

def administer_survey(question_list): #both
    answer_list = []
    for question, _ in question_list:
        valid_response = ask_question(question)
        answer_list.append(valid_response)
    return answer_list

def ask_question(question): #both
     #code here

def calculate_score(question_list, answer_list): #both
   #include a counter

def display_result(final_score): #both
     #displpay results


def main(): #emerson
    

if __name__ == "__main__":
    main()
