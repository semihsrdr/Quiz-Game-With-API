from tkinter import *
from quiz_model import create_questions,check_answer

BACKGROUND_COLOR="#008DDA"
FONT_COLOR="#F7EEDD"

question_number=0
correct_answer=0
my_questions=create_questions()
question=my_questions[question_number].question
answer=my_questions[question_number].answer

user_answer=None

def true_choice():
    global question_number,correct_answer
    if question_number<10:
        user_answer="True"
        if check_answer(user_answer,question_number,my_questions):
            correct_answer+=1

        question_number+=1
        question = my_questions[question_number].question

        canvas.itemconfig(question_text,text=question)
        counter.config(text=f"{correct_answer}/{question_number}")
    else:
        counter.config(text="")
        canvas.itemconfig(question_text,text=f"Game Over {correct_answer}/{question_number}")

def wrong_choice():
    global question_number,correct_answer
    if question_number < 10:
        user_answer = "False"
        if check_answer(user_answer,question_number,my_questions):
            correct_answer+=1
        question_number+=1
        question = my_questions[question_number].question

        canvas.itemconfig(question_text, text=question)
        counter.config(text=f"{correct_answer}/{question_number}")
    else:
        counter.config(text="")
        canvas.itemconfig(question_text,text=f"Game Over {correct_answer}/{question_number}")

window=Tk()
window.minsize(400,650)
window.title("Quiz Game")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=35)

true_image=PhotoImage(file="images/right.png")
wrong_image=PhotoImage(file="images/wrong.png")

counter=Label(text=f"{correct_answer}/{question_number}",bg=BACKGROUND_COLOR,font=("Arial",25,"bold"))
counter.grid(row=0,column=0)

canvas=Canvas(width=300,height=400,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=1,column=1)

question_text=canvas.create_text(150,175,width=300,text=my_questions[0].question,
                                 font=("Arial",20,"bold"),fill=FONT_COLOR)

true_button=Button(image=true_image,bg=BACKGROUND_COLOR,command=true_choice)
true_button.grid(column=2,row=2)

wrong_button=Button(image=wrong_image,bg=BACKGROUND_COLOR,command=wrong_choice)
wrong_button.grid(column=0,row=2)

window.mainloop()



