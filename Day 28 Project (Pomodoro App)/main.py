from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#FF8080"
ORANGE = "#FFCF96"
GREEN = "#557C55"
YELLOW = "#F6FDC3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    lbl_timer.config(text="TIMER")
    canvas.itemconfig(canvas_timer, text="00:00")
    lbl_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown_timer(long_break_sec)
        lbl_timer.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(short_break_sec)
        lbl_timer.config(text="SHORT BREAK", fg=ORANGE)
    else:
        countdown_timer(work_sec)
        lbl_timer.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_reps = math.floor(reps/2)
        for i in range(work_reps):
            lbl_check.config(text=checkmarks)
            checkmarks += txt_checkmark
        lbl_check.config(text=checkmarks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
txt_checkmark = " ✔ "
lbl_timer = Label(text="TIMER", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
lbl_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
canvas_timer = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

btn_start = Button(text="START", font=(FONT_NAME, 16, "bold"), fg=YELLOW, bg=GREEN, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="RESET", font=(FONT_NAME, 16, "bold"), fg=YELLOW, bg=GREEN, command=reset_timer)
btn_reset.grid(column=2, row=2)

lbl_check = Label(font=(FONT_NAME, 12, "bold"), fg=RED, bg=YELLOW)
lbl_check.grid(column=1, row=3)

window.mainloop()
