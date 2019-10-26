#%%
from pyautogui import press, typewrite, hotkey


#%%

def create_dict():
    isRunning = True
    #dict for questions and answers
    dict = {}
    while isRunning:
        question = input("Please enter your question(type 'Q' to quit)")
        if question == 'Q':
            isRunning = False
            break
        if question in dict.keys():
            print("You already submitted this question")
        else:
            answer = input("Please enter the answer to the question")
            dict[question] = answer
    return dict

dict = create_dict()


#%%
def quiz_user(dict):
    isRunning = True
    print("Quizzing you! Type 'Q' to quit")
    while isRunning:
        for question, answer in dict.items():
            userAnswer = input(question)
            if userAnswer == 'Q':
                return
            if userAnswer == dict[question]:
                print("Correct!")
            else:
                print("Incorrect, the answer is %s", dict[question])

quiz_user(dict)


#%%



