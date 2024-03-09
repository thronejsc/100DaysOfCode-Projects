from tkinter import *

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window)
        self.window.geometry("250x260")
        self.window.title("Tic-Tac-Toe")
        self.buttonList = []
        self.currentPlayer = 0
        
        
        index = 0
        for y in range(3):
            for x in range(3):
                tile = Button(self.frame, text=" ", width=10, height=5, command= lambda index=index:self.click(index))
                tile.grid(row=y, column=x, sticky="NSEW")
                index += 1
                self.buttonList.append(tile)
                
        self.frame.pack()
        
    def click(self, index):        
        if self.currentPlayer == 0:
            self.buttonList[index].config(text="X")
            self.currentPlayer = 1
        else:
            self.buttonList[index].config(text="O")
            self.currentPlayer = 0
            
        
        
def main():
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()


main()