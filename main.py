from text_to_speech import speak
from speech_to_text import *
from basic import *
import os


if __name__ == '__main__':
    #flashcards = create_dict()
    flashcards = {}
    flashcards["What is the powerhouse of the cell?"] = "Mitochondria"
    flashcards["What are you doing?"] = "Coding"
    flashcards["Best part of Hackathons?"] = "Free Stuff"
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    score, asked = 0, 0
    speak("Starting Test, say 'Quit' to end or 'Give up' to skip question")
    print("Starting Test, say 'Quit' to end or 'Give up' to skip question")
    for question in flashcards:
        speak(question)
        print(question)
        asked += 1
        words = run_mic(flashcards[question].lower())
        if words == "Correct":
            speak("Correct")
            score += 1
        elif words == 'Quit':
            break
        elif words == "Give up":
            print("Incorrect, the answer is " + flashcards[question])
    print("You scored " + str((100*score)//len(flashcards)) + "%!")
    print("Congratulations")
