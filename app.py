import threading
import tkinter as tk
from io import BytesIO
from tkinter import ttk

from PIL import Image, ImageTk


class App():
    # TODO: Import data, Moveable tabs, Timer integration, Refresh
    def __init__(self):
        width = 400
        height = 550
        title = 'Shiva\'s Summoner Spell Tracker'
        self._images = []
        # Create the main window
        self.root = tk.Tk()
        # Set the window size (widthxheight)
        self.root.geometry(f'{width}x{height}')
        # Change the title of the window
        self.root.title(f'{title}')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=2)
        self.mainframe.rowconfigure(2, weight=2)
        self.mainframe.rowconfigure(3, weight=2)
        self.mainframe.rowconfigure(4, weight=2)
        self.mainframe.rowconfigure(5, weight=2)

        self.row0 = tk.Frame(self.mainframe, background='red', name='row0')
        self.row0.grid(row=0, column=0, sticky='NSEW')

        self.row1 = tk.Frame(self.mainframe, background='blue', name='row1')
        self.row1.grid(row=1, column=0, sticky='NSEW')

        self.row2 = tk.Frame(self.mainframe, background='green', name='row2')
        self.row2.grid(row=2, column=0, sticky='NSEW')

        self.row3 = tk.Frame(self.mainframe, background='yellow', name='row3')
        self.row3.grid(row=3, column=0, sticky='NSEW')

        self.row4 = tk.Frame(self.mainframe, background='purple', name='row4')
        self.row4.grid(row=4, column=0, sticky='NSEW')

        self.row5 = tk.Frame(self.mainframe, background='orange', name='row5')
        self.row5.grid(row=5, column=0, sticky='NSEW')

        ttk.Button(self.row0, text='Refresh').pack(
            fill='both', expand=True, padx=5, pady=5)

        self.champions = {}
        self.champions['champ1'] = self.create_champ_row_layout(self.row1)
        self.champions['champ2'] = self.create_champ_row_layout(self.row2)
        self.champions['champ3'] = self.create_champ_row_layout(self.row3)
        self.champions['champ4'] = self.create_champ_row_layout(self.row4)
        self.champions['champ5'] = self.create_champ_row_layout(self.row5)

        # print(self.champions)

        # self.header_text = ttk.Label(self.mainframe, text="Spell Tracker",
        #                              background='white', font=('Brass Mono', 30))
        # self.header_text.grid(row=0, column=0)

        # self.set_text_field = ttk.Entry(self.mainframe)
        # self.set_text_field.grid(row=1, column=0, pady=10, sticky='NSEW')
        # set_text_button = ttk.Button(
        #     self.mainframe, text="Set Text", command=self.set_text)
        # set_text_button.grid(row=1, column=1, pady=10)

        # color_options = ['red', 'green', 'blue', 'black']
        # self.set_color_field = ttk.Combobox(
        #     self.mainframe, values=color_options)
        # self.set_color_field.grid(row=2, column=0, pady=10, sticky='NSEW')
        # set_color_button = ttk.Button(
        #     self.mainframe, text="Set Color", command=self.set_color)
        # set_color_button.grid(row=2, column=1, pady=10)

        # self.reverse_text = ttk.Button(
        #     self.mainframe, text="Reverse Text", command=self.reverse)
        # self.reverse_text.grid(row=3, column=0, sticky='NSWE', pady=10)

        # Show the main window
        # self.root.mainloop()
        return

    def refresh(self):
        print('refresh')

    def create_champ_row_layout(self, row):
        champion = {}
        row.columnconfigure(0, weight=4)
        row.columnconfigure(1, weight=6)
        row.rowconfigure(0, weight=1)

        col0 = tk.Frame(row, background='white')
        col0.grid(row=0, column=0, sticky='NSEW', padx=5, pady=5)

        col1 = tk.Frame(row, background='white')
        col1.grid(row=0, column=1, sticky='NSEW', padx=5, pady=5)

        col0.rowconfigure(0, weight=4)
        col0.rowconfigure(1, weight=1)
        col0.columnconfigure(0, weight=1)

        champ_image = ttk.Label(col0, text='ChampImage')
        champ_image.grid(row=0, column=0, sticky='NSEW', padx=5, pady=5)
        champion['championImage'] = champ_image

        champ_name = ttk.Label(col0, text='ChampName')
        champ_name.grid(row=1, column=0, sticky='NSEW', padx=5, pady=5)
        champion['championName'] = champ_name

        col1.rowconfigure(0, weight=1)
        col1.rowconfigure(1, weight=1)
        col1.columnconfigure(0, weight=4)
        col1.columnconfigure(1, weight=4)
        col1.columnconfigure(2, weight=1)

        summ_1_image = ttk.Button(col1, text='Summ1Image')
        summ_1_image.grid(row=0, column=0, sticky='NSEW', padx=5, pady=5)
        champion['summonerSpell1Image'] = summ_1_image

        summoner_1_cooldown = ttk.Label(col1, text='Summ1CD', foreground='red')
        summoner_1_cooldown.grid(
            row=0, column=1, sticky='NSEW', padx=5, pady=5)
        champion['summonerSpell1Cooldown'] = summoner_1_cooldown

        summ_2_image = ttk.Button(col1, text='Summ2Image')
        summ_2_image.grid(row=1, column=0, sticky='NSEW', padx=5, pady=5)
        champion['summonerSpell2Image'] = summ_2_image

        summ_2_cooldown = ttk.Label(col1, text='Summ2CD', foreground='red')
        summ_2_cooldown.grid(
            row=1, column=1, sticky='NSEW', padx=5, pady=5)
        champion['summonerSpell2Cooldown'] = summ_2_cooldown

        ttk.Button(col1, text='MoveUpArrow').grid(
            row=0, column=2, sticky='NSEW', padx=5, pady=5)

        ttk.Button(col1, text='MoveUpArrow').grid(
            row=1, column=2, sticky='NSEW', padx=5, pady=5)

        return champion

    def configure_image(self, widget, image):
        tk_champ_image = ImageTk.PhotoImage(
            Image.open(BytesIO(image)))  # type: ignore
        self._images.append(tk_champ_image)
        widget.configure(image=tk_champ_image)  # type: ignore
        return

    def configure_text(self, widget, text):
        return

    def configure_button(self, widget, command):
        return

    def start_cooldown(self, champion_name, summoner_spell_name):
        # TODO: call cooldown_timer's start_cooldown() function
        return

    # def set_text(self):
    #     newtext = self.set_text_field.get()
    #     self.text.config(text=newtext)

    # def set_color(self):
    #     newcolor = self.set_color_field.get()
    #     self.text.config(foreground=newcolor)

    # def reverse(self):
    #     newtext = self.text.cget('text')
    #     reversed = newtext[::-1]
    #     self.text.config(text=reversed)


def main():
    """
    main()
    """
    app = App()
    # pf = Pulsefire()
    # champ_image = pf.fetch_champ_image('Zoe')
    # app.configure_image(app.champions['champ1']['championImage'], champ_image)
    app.root.mainloop()


if __name__ == '__main__':
    main()
