from tkinter import *
import random
import time


# ---------- COLOR PALETE ----------- #
BG = "#DDDDDD" #rgb(234, 223, 180)
FG = "#222831" #rgb(155, 176, 193)
FG2 = "#30475E" #rgb(81, 130, 155)
FG3 = "#F05454" #rgb(246, 153, 92)



# ---------- FUNCTIONS / CLASS ----------- #
class TypingSpeedTest:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("800x800")
        self.window.configure(bg=BG)
        self.start_time = None
        self.sentence = self.generate_sentence()
        self.set_ui()
        self.window.mainloop()
        
    def start_timer(self):
        self.start_time = time.time()
            
        
    def set_ui(self):
        self.subtitle_label = Label(self.window, text="How fast can you TYPE?", font=("Helvetica", 36), fg=FG, bg=BG, highlightthickness=0)
        self.subtitle_label.pack(pady=20)
        
        self.sentence_label = Label(self.window, text=self.sentence, font=("Helvetica", 18), wraplength=700, fg=FG, bg=BG, highlightthickness=0)
        self.sentence_label.pack()

        self.input_text = Text(self.window, font=("Helvetica", 16), wrap=WORD, width=60, height=10)
        self.input_text.pack(pady=40)
        self.input_text.bind('<Key>', func=self.check_typing)

        self.result_label = Label(self.window, text="", font=("Helvetica", 14), fg=FG, bg=BG, highlightthickness=0)
        self.result_label.pack()

    def check_typing(self, event):
        if self.start_time is None:
            self.start_timer()
        self.user_input = self.input_text.get("1.0", "end-1c")
        self.correct_words = self.sentence.split()
        self.user_words = self.user_input.split()

        for i in range(len(self.user_words)):
            if i < len(self.correct_words):
                if self.user_words[i] == self.correct_words[i]:
                    self.input_text.tag_add("correct", f"1.{len(' '.join(self.correct_words[:i]))}", f"1.{len(' '.join(self.correct_words[:i+1]))}")
                    self.input_text.tag_config("correct", foreground=FG2)
                else:
                    self.input_text.tag_add("incorrect", f"1.{len(' '.join(self.correct_words[:i]))}", f"1.{len(' '.join(self.correct_words[:i+1]))}")
                    self.input_text.tag_config("incorrect", foreground=FG3)
                    break
            else:
                self.result_label.config(text="Typing test done")
                self.input_text.config(state=DISABLED)
                end_time = time.time()
                elapsed_time = end_time - self.start_time
                total_words = len(self.sentence.split())
                wpm = int((total_words / elapsed_time) * 60)
                self.result_label.config(text=f"Typing test done\nYour WPM (Words per Minute): {wpm}")
                
    
    def generate_sentence(self):
        try: 
            with open('./paragraphs.txt', 'r') as file:
                paragraphs = file.read()
            paragraph_list = paragraphs.split('\n')
        except FileNotFoundError:
            print("File not found.")
            paragraph_list = ["The rapid advancements in technology have revolutionized the way we live and work. From artificial intelligence to virtual reality, innovations continue to shape our daily experiences. As we embrace these changes, the potential for further transformation in various sectors becomes increasingly evident.",
                            "The urgent need for environmental conservation is evident as we grapple with the effects of climate change. Sustainable practices and eco-friendly initiatives are becoming crucial for preserving our planet. It is imperative for individuals, communities, and governments to collaborate in adopting responsible measures to ensure a healthier and greener future.",
                            "Education remains a cornerstone for personal and societal development. In an ever-evolving world, the emphasis on lifelong learning has become more pronounced. As technology and globalization reshape the job market, a commitment to continuous education becomes essential for staying competitive and adaptable."
                            ]
        finally:
            random_paragraph = random.choice(paragraph_list)
            random_paragraph = random_paragraph.strip("\\n")
            return random_paragraph



app = TypingSpeedTest()
