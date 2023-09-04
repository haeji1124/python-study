import tkinter
import random

def click_btn():
    f=open('./교육생 리스트.txt','r', encoding='utf-8')
    students=f.readlines()
    label["text"] = random.choice(students).strip()
    label.update()

root = tkinter.Tk()
root.title("발표자는 누구?!")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=900, height=800)
canvas.pack()

gazou = tkinter.PhotoImage(file="random.png")
canvas.create_image(300, 200, image=gazou)

label = tkinter.Label(root, text="??????", font=("Times New Roman", 90), bg="gold")
label.place(x=270, y=200)

button = tkinter.Button(root, text="누가 발표할까요?", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=250, y=400)


root.mainloop()
