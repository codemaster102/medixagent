from tkinter import *
from chat import get_response, bot_name

BG_GREY = "#ABB2B9"
BG_COLOUR = "#17202A"
TEXT_COLOUR = "#EAECEE"

FONT = "Arial 14"
FONT_BOLD = "Arial 13 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

        photo = PhotoImage(file = "icon.png")
        self.window.iconphoto(False, photo)

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Medix Help")
        self.window.resizable(width=True, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOUR)

        head_label = Label(self.window, bg=BG_COLOUR, fg=TEXT_COLOUR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        #Divider
        line = Label(self.window, width=450, bg=BG_GREY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #Text
        self.text_widget = Text(self.window, width=20, height=2, bg="#108742", fg=TEXT_COLOUR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #Scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        #Bottom label
        bottom_label = Label(self.window, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #Input box
        self.msg_entry = Entry(bottom_label, bg="#777a78", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #Send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#0998ab", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()