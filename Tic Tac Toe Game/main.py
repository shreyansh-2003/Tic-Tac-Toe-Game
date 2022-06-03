"""
Developed By Shreyansh Padarha

"""

# importing required libraries

"""
have to import modules selectively, cant import whole library as two similar libraries have been imported
"""
import random
from tkmacosx import *  # This library was specifically created by an Indian for removing bugs faced on mac os, it works on windows, linux as well
from tkinter import messagebox
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import font
from tkinter import Label
from tkinter import Canvas
from tkinter import Toplevel
from tkinter import StringVar
from tkinter.font import *
from tkmacosx.widgets import button
from PIL import Image, ImageTk

"""
Tic-tac-toe Game
Developed by Shreyansh Padarha
"""

# storing the hexadecimal for the turquoise theme in bg_theme, recurring through each window created
bg_theme = "#42F9F9"


# function for having a watermark ("developed by") in the program
def salutation(master, col, row):
    cLabel = Label(master, text="Developed By Shreyansh Padarha", fg='black', bg=bg_theme)
    cLabel['font'] = font.Font(size=16, weight='bold')
    cLabel.grid(column=col, row=row, sticky="e", pady=(10, 0))
    Label()


""" Initial class will hold all the attributes within the initial pop-up box which is meant to ask the player to play 
single-player or multi-player 
"""


class Initial:
    def __init__(self):
        # initialising Tkinter as Tk
        self.choice = Tk()

        # Creating a Marquee for the "Welcome to the tic-tac-toe game"
        greet_text = """Welcome to the Tic-tac-toe game ! \
        """ * 1000
        greet = Marquee(self.choice, bg='orange', fg='#101820',
                        text=greet_text,
                        initial_delay=0,
                        end_delay=0,
                        left_margin=55,
                        bd=3,
                        font=font.Font(family="Helvetica", size=20, weight='bold'))
        greet.grid(row=0, column=1, ipadx=38, pady=10)

        self.choice.title("Tic-tac-toe Game")  # changing title of the window
        self.choice.geometry("365x235")  # changing geometry of the window
        self.choice.resizable(width=False,
                              height=False)  # setting attribute resizable to false for width and height, to prevent manual resizing by user
        self.choice.configure(bg=bg_theme)  # onfiguring the background colour

        # self.icon = PhotoImage(file="iconChange.ico")
        # self.choice.iconphoto(True,icon)

        # calling the functions that place labels and buttons on the window
        self.createButtons()
        salutation(self.choice, 1, 3)

        self.choice.mainloop()

    # function that creates buttons onn choice window
    def createButtons(self):
        global My_Font
        # setting font that can be reused in a standardized manner
        My_Font = font.Font(family="Helvetica", size=25, weight='bold')

        # button for playing multiplayer
        PP = Button(self.choice,
                    text="Play VS Player",
                    command=lambda: self.clicked(True),
                    bd=5,
                    relief='raised',
                    font=My_Font)
        PP.grid(column=1, row=1, pady=10, padx=20)  # placing button

        # button for playing vs computer
        CP = Button(self.choice,
                    text="Play VS Computer",
                    command=lambda: self.clicked(False),
                    bd=5,
                    relief='raised',
                    font=My_Font)

        CP.grid(column=1, row=2, pady=10, padx=20)  # placing button

    # function that holds instructions for when the buttons are clicked
    def clicked(self, player):

        global entry  # creating a global variable for the window variable

        # destroying the initial choice selection window --> without destroying the font style of the TopLevel window
        # cant be modified
        self.choice.destroy()

        # creating a new tkinter window to get player names
        entry = Tk()

        # Creating a Marquee for the "Enter Player Names" overlay
        greet_text_entry = """ Enter Player Names  \
               """ * 1000
        greet_entry = Marquee(entry, bg='orange', fg='#101820',
                              text=greet_text_entry,
                              initial_delay=0,
                              end_delay=0,
                              font=font.Font(size=25, weight='bold'),
                              left_margin=55)

        greet_entry.grid(row=0, column=0, columnspan=2, ipadx=78, pady=10)

        # changing title of the window
        entry.title("Tic-tac-toe Game")
        entry.geometry("438x255")  # changing geometry of the window
        entry.resizable(width=False,
                        height=False)  # setting attribute resizable to false for width and height to prevent resizing
        entry.configure(bg=bg_theme)  # configuring the background colour of the window

        # labels to show what the entry box signifies
        P1 = Label(entry, text="Player 1 ", bg=bg_theme, fg="black")
        P1['font'] = font.Font(family="Helvetica", size=22, weight='bold')
        P1.grid(column=0, row=1)

        P2 = Label(entry, text="Player 2 ", bg=bg_theme, fg="black")
        P2['font'] = font.Font(size=22, weight='bold')
        P2.grid(column=0, row=2, padx=20, pady=5)

        # entries for player names
        Player1 = Entry(entry, bg="#212124", fg="white")
        Player1['font'] = font.Font(family="Helvetica", size=20, weight='bold')
        Player1.grid(column=1, row=1, padx=20, pady=5)

        Player2 = Entry(entry, bg="#212124", fg="white")
        Player2['font'] = font.Font(family="Helvetica", size=20, weight='bold')
        Player2.grid(column=1, row=2, padx=20, pady=5)

        if len(Player1.get()) > 20 or len(Player2.get()) > 20:
            pass

        # if the play vs computer button was clicked, then player boolean value will be false
        # so if player is false then insert player 2 by default as "COMPUTER", adn disable entry
        if not player:
            Player2.insert(0, "COMPUTER")
            Player2.config(state="disabled", justify="center", fg="black", bg="orange")

        # button for submitting player names, it will call a function that initializes the UI class
        Button(entry,
               text="PLAY",
               command=lambda: self.submit(Player1.get(), Player2.get()),
               focuscolor="orange",
               bd=3.5,
               relief='raised',
               font=font.Font(family="Helvetica", size=28
                              , weight='bold')).grid(row=3, columnspan=2, pady=10, padx=50, ipadx=30)

        # developer tag
        salutation(entry, 1, 4)

        entry.mainloop()

    # function for when "PLAY" button is clicked
    def submit(self, p_1, p_2):
        global newGame
        print("Player 1 : ", p_1)
        print("Player 2 : ", p_2)

        if p_2 != "COMPUTER":
            entry.destroy()
            # initializing the UI class
            newGame = UI(p_1, p_2)

        else:
            global msg
            msg = Toplevel(entry)
            msg.geometry("630x130")  # changing geometry of the window
            msg.title("Tic-tac-toe Game")  # title of the main window
            msg.resizable(width=False, height=False)  # setting attribute resizable to false for width and height
            msg.configure(bg=bg_theme)

            Label(msg, text="Sorry ! This section is under development !", font=font.Font(family="Helvetica", size=30
                                                                                          , weight='bold'), bg=bg_theme,
                  fg="black").grid(row=0, column=0,
                                   padx=5,
                                   pady=10)

            Button(msg, text="OK", font=font.Font(family="Helvetica", size=25
                                                  , weight='bold'),
                   relief="raised", command=self.destroy).grid(row=1, column=0, padx=10, pady=10)

    def destroy(self):
        msg.destroy()
        entry.destroy()
        test = Initial()


"""
Main Tic-tac-toe board work
"""

"""
Rough Layout 
-> Row 0 : Column 1 - Label ("Turn : "), Column 2 Label(getting player name from current variable)
-> Row 1 : three buttons (lines cutting across and above) 
-> Row 2 : three buttons (lines cutting across and above)
-> Row 3 : three buttons (lines cutting across and above)
-> Row 4 : Salutation (and equal gap from board like row 0 and row 1 gap)

"""


# created outside the class, and method not required for it
def closeAll():
    res.destroy()


class UI:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.players = [p1, p2]  # this will help in randomizing who gets the first move
        self.current = random.choice(self.players)
        # creating a matrix (nested list)(3X3), where 0 signifies empty space
        self.board_matrix = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]

        # initialising the main window
        self.main = Tk()

        # creating a Canvas for the board to be on --> for aesthetic purposes
        self.board = Canvas(self.main, bg="brown", height=400, width=550,
                            highlightbackground="#BA8C63", highlightthickness=5)

        self.board.grid(row=1, column=0, columnspan=3)  # placing the board canvas

        self.main.geometry("384x450")  # changing geometry of the window
        self.main.title("Tic-tac-toe Game")  # title of the main window
        self.main.resizable(width=False, height=False)  # setting attribute resizable to false for width and height
        self.main.configure(bg=bg_theme)  # changing bg colour

        # Creating labels that will display the current turn player name
        self.turn_label = Label(self.main, text="Turn : ",
                                font=font.Font(family="Helvetica", size=25, weight='bold'),
                                fg="black",
                                bg=bg_theme)
        self.turn_label.grid(row=0, column=0, padx=(0, 0), pady=20)

        self.playerName = Label(self.main, text=self.current,
                                font=font.Font(family="Helvetica", size=25, weight='bold'),
                                fg="black",
                                bg=bg_theme)
        self.playerName.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="w")

        # calling the function that will create the main game board
        self.createBoard(self.board)

        # calling the salutation function for developer's watermark in the end
        salutation(self.main, 1, 4)

        self.main.mainloop()

    # function that creates the board with widgets
    def createBoard(self, master):
        if self.p2 != "COMPUTER":
            for r in range(1, 4):  # 3 rows
                for c in range(0, 3):  # 3 columns
                    lab = Button(master, text=None, bg="#BA8C63",
                                 relief="flat",
                                 font=font.Font(family="Helvetica", size=40
                                                , weight='bold'),
                                 borderless=True, width=123, height=100)
                    lab.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")  # sticky parameter used to avoid gaps
                    lab.bind('<Button-1>', lambda event, object=[r - 1, c]: self.clickKey(event, object))

        # under development sectionn
        else:
            pass

    def clickKey(self, event, position):
        # playing multiplayer
        if self.p2 != "COMPUTER":

            if self.board_matrix[position[0]][position[1]] == 0:
                if self.current == self.p1:
                    event.widget.config(activebackground='#AE0E36')
                    event.widget.config(text="X", font=font.Font(family="Helvetica", size=60
                                                                 , weight='bold'), fg="blue",
                                        activebackground='green')

                    self.current = self.p2
                    self.playerName.config(text=self.current)
                    self.board_matrix[position[0]][position[1]] = self.p1


                else:
                    event.widget.config(text="O", font=font.Font(family="Helvetica", size=60
                                                                 , weight='bold'), fg="red",
                                        activebackground='green')

                    self.current = self.p1
                    self.playerName.config(text=self.current)
                    self.board_matrix[position[0]][position[1]] = self.p2

            else:
                event.widget.config(activebackground='#AE0E36')
                # print("!!!!! button already clicked !!!! ")
                # print(self.board_matrix)

        # playing vs computer
        else:
            pass

        # print(self.board_matrix)
        result = self.checkState(self.board_matrix)

        # if the returned value / result is not 0, it means its a player name
        if type(result) != int:
            msg = str(result) + " won !"
            self.resBox(msg)
        else:
            if result == 0:
                pass
                # print("empty boxes left !/n")
            else:
                self.resBox("ITS A TIE !")

    # This will check whether p1 or p2 has won
    def checkState(self, arr):
        # checking if diagonals are equal
        if arr[0][0] == arr[1][1] == arr[2][2] or \
                arr[0][2] == arr[1][1] == arr[2][0]:
            return arr[1][1]
        # checking if verticals or horizontals are equal
        for x in range(0, 3):
            if arr[0][x] == arr[1][x] == arr[2][x] == self.p1 or \
                    arr[0][x] == arr[1][x] == arr[2][x] == self.p2:
                return arr[0][x]
            if arr[x][0] == arr[x][1] == arr[x][2] == self.p1 or \
                    arr[x][0] == arr[x][1] == arr[x][2] == self.p2:
                return arr[x][0]
            else:
                continue

        check_value = self.checkFull()
        return check_value

    # function to check whether there is any empty space in the board
    def checkFull(self):
        arr = self.board_matrix
        for row in range(0, 3):
            for column in range(0, 3):
                if arr[row][column] == 0:
                    return 0
        return -1

    # function for displaying result box
    def resBox(self, message):
        global res
        self.main.withdraw()  # shifts the focus to the Toplevel window
        res = Toplevel(self.main)
        res.geometry("400x130")  # changing geometry of the window
        res.title("Tic-tac-toe Game")  # title of the main window
        res.resizable(width=False, height=False)  # setting attribute resizable to false for width and height
        res.configure(bg=bg_theme)

        Label(res, text=message, font=font.Font(family="Helvetica", size=30
                                                , weight='bold'), bg=bg_theme, fg="black").grid(row=0, column=0,
                                                                                                columnspan=2, padx=5,
                                                                                                pady=10)

        Button(res, text="Exit Game", font=font.Font(family="Helvetica", size=25
                                                     , weight='bold'),
               relief="raised", command=self.closeAll).grid(row=1, column=0, padx=10, pady=10)

        Button(res, text="Play Again", font=font.Font(family="Helvetica", size=25
                                                      , weight='bold'),
               relief="raised", command=self.playAgain).grid(row=1, column=1, padx=10, pady=10)

    # closing all applications
    def closeAll(self):
        res.destroy()
        self.main.destroy()

    # resetting the board for same players
    def playAgain(self):
        res.destroy()
        self.main.destroy()
        UI(self.p1, self.p2)


"""
DRIVER CODE
"""

if __name__=="__main__":
    test = Initial()
