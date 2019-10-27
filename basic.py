from pyautogui import press, typewrite, hotkey


def create_dict():
    isRunning = True
    #dict for questions and answers
    dict = {}
    while isRunning:
        question = input("Please enter your question(type 'Finished!' to finish)")
        if question == 'Finished!':
            break
        if question in dict.keys():
            print("You already submitted this question")
        else:
            answer = input("Please enter your word")
            dict[question] = answer
    return dict





