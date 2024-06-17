import threading
import tkinter as tk
from io import BytesIO
from tkinter import ttk

from PIL import Image, ImageTk


class App():
    # TODO: Moveable tabs, Optimization of startup, Refactor game time tracking
    def __init__(self):
        width = 250
        height = 550
        title = 'Shiva\'s Summoner Spell Tracker'
        self._images = {}
        # Create the main window
        self.root = tk.Tk()
        # Set the window size (widthxheight)
        self.root.geometry(f'{width}x{height}')
        # Change the title of the window
        self.root.title(f'{title}')
        self.root.resizable(False, False)
        self.mainframe = tk.Frame(self.root, background='grey')
        self.mainframe.propagate(False)
        self.mainframe.pack(fill='both', expand=True)

        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure([1, 2, 3, 4, 5], weight=3)

        self.row0 = tk.Frame(self.mainframe, background='red', name='row0')
        self.row0.grid(row=0, column=0, sticky='NSEW', pady=2, padx=2)
        self.row0.propagate(False)

        self.row1 = tk.Frame(self.mainframe, background='blue', name='row1')
        self.row1.grid(row=1, column=0, sticky='NSEW', pady=2, padx=2)

        self.row2 = tk.Frame(self.mainframe, background='green', name='row2')
        self.row2.grid(row=2, column=0, sticky='NSEW', pady=2, padx=2)

        self.row3 = tk.Frame(self.mainframe, background='yellow', name='row3')
        self.row3.grid(row=3, column=0, sticky='NSEW', pady=2, padx=2)

        self.row4 = tk.Frame(self.mainframe, background='purple', name='row4')
        self.row4.grid(row=4, column=0, sticky='NSEW', pady=2, padx=2)

        self.row5 = tk.Frame(self.mainframe, background='orange', name='row5')
        self.row5.grid(row=5, column=0, sticky='NSEW', pady=2, padx=2)

        self.refresh_button = ttk.Button(self.row0, text='Refresh')
        self.refresh_button.pack(fill='both', expand=True)

        self.row_widgets = []
        self.row_widgets.append(self.create_champ_row_layout(self.row1))
        self.row_widgets.append(self.create_champ_row_layout(self.row2))
        self.row_widgets.append(self.create_champ_row_layout(self.row3))
        self.row_widgets.append(self.create_champ_row_layout(self.row4))
        self.row_widgets.append(self.create_champ_row_layout(self.row5))

        return

    def refresh(self):
        print('refresh')

    def create_champ_row_layout(self, row: tk.Frame):
        widgets = {}

        champ_image = ttk.Label(row, text='ChampImage')
        champ_image.place(relx=0, rely=0, relwidth=0.4,
                          relheight=1, anchor='nw')
        widgets['championImage'] = champ_image

        summ_1_image = tk.Button(row, text='Summ1Image')
        summ_1_image.place(relx=0.4, y=0, relwidth=0.2,
                           relheight=0.5, anchor='nw')
        widgets['summonerSpell1Image'] = summ_1_image

        summoner_1_cooldown = ttk.Label(row, text='Ready', foreground='green')
        summoner_1_cooldown.place(
            relx=0.6, rely=0, relwidth=0.3, relheight=0.5, anchor='nw')
        widgets['summonerSpell1Cooldown'] = summoner_1_cooldown

        summ_2_image = tk.Button(row, text='Summ2Image')
        summ_2_image.place(relx=0.4, rely=0.5, relwidth=0.2,
                           relheight=0.5, anchor='nw')
        widgets['summonerSpell2Image'] = summ_2_image

        summ_2_cooldown = ttk.Label(row, text='Ready', foreground='green')
        summ_2_cooldown.place(relx=0.6, rely=0.5,
                              relwidth=0.3, relheight=0.5, anchor='nw')
        widgets['summonerSpell2Cooldown'] = summ_2_cooldown

        ttk.Button(row, text='^').place(
            relx=0.9, rely=0, relwidth=0.1, relheight=0.5, anchor='nw')

        ttk.Button(row, text='v').place(
            relx=0.9, rely=0.5, relwidth=0.1, relheight=0.5, anchor='nw')

        return widgets

    def configure_row(self, row, enemy, main_obj) -> None:
        # Champ Image
        self.configure_champion_image(
            row['championImage'], enemy['championIcon'])
        # Champ Name
        # self.configure_text(row['championName'], enemy['championName'])
        # Summoner 1 Image
        self.configure_summoner_image(row['summonerSpell1Image'],
                                      enemy['summonerSpells']['summonerSpellOne']['icon'])
        # Summoner 1 Cooldown
        # self.configure_button(row['summonerSpell1Icon'], lambda: print('test'))
        self.configure_button(row['summonerSpell1Image'], lambda: main_obj.update_and_start_cooldown(
            enemy, enemy['summonerSpells']['summonerSpellOne']['name'], row['summonerSpell1Cooldown']))
        # Summoner 2 Image
        self.configure_summoner_image(row['summonerSpell2Image'],
                                      enemy['summonerSpells']['summonerSpellTwo']['icon'])
        # Summoner 2 Cooldown
        self.configure_button(row['summonerSpell2Image'], lambda: main_obj.update_and_start_cooldown(
            enemy, enemy['summonerSpells']['summonerSpellTwo']['name'], row['summonerSpell2Cooldown']))
        return

    def configure_champion_image(self, widget, image):
        self._configure_image(widget, image, champion=True)

    def configure_summoner_image(self, widget, image):
        self._configure_image(widget, image, summoner=True)

    def _configure_image(self, widget, image: bytes, champion: bool = False, summoner: bool = False):
        if champion and summoner:
            assert False, 'Champion and summoner cannot both be true'
        if not champion and not summoner:
            assert False, 'Must be either a champion or a summoner'
        if image not in self._images:
            if champion:
                img = self.resize_champ_image(image)
            elif summoner:
                img = self.resize_summoner_image(image)
            else:
                assert False
            tk_champ_image = ImageTk.PhotoImage(img)
            self._images[image] = tk_champ_image
        widget.configure(image=self._images[image])
        return

    def resize_champ_image(self, image, new_width=100, new_height=100):
        img = Image.open(BytesIO(image))
        resized_img = img.resize((new_width, new_height))
        return resized_img

    def resize_summoner_image(self, image, new_width=50, new_height=50):
        img = Image.open(BytesIO(image))
        resized_img = img.resize((new_width, new_height))
        return resized_img

    def configure_text(self, widget, replace_text: str):
        widget.configure(text=replace_text)
        return

    def configure_button(self, widget, command):
        widget.configure(command=command)
        return

    def bind_refresh(self, func):
        self.configure_button(self.refresh_button, lambda: func())


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
