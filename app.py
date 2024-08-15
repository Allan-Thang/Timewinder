import sys
import tkinter as tk
from io import BytesIO
from tkinter import ttk

from PIL import Image, ImageTk, UnidentifiedImageError

from dict_types import EnemyData, RowWidgets
from game_time_tracker import GameTimeTracker


class App():
    def __init__(self, gtt: GameTimeTracker):
        self.gtt = gtt
        width = 250
        height = 550
        title = 'Shiva\'s Summoner Spell Tracker'
        self._images = {}
        # Create the main window
        self.root = tk.Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
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

        row0 = tk.Frame(self.mainframe, background='red', name='row0')
        row0.grid(row=0, column=0, sticky='NSEW', pady=2, padx=2)
        row0.propagate(False)

        row1 = tk.Frame(self.mainframe, background='blue', name='row1')
        row1.grid(row=1, column=0, sticky='NSEW', pady=2, padx=2)

        row2 = tk.Frame(self.mainframe, background='green', name='row2')
        row2.grid(row=2, column=0, sticky='NSEW', pady=2, padx=2)

        row3 = tk.Frame(self.mainframe, background='yellow', name='row3')
        row3.grid(row=3, column=0, sticky='NSEW', pady=2, padx=2)

        row4 = tk.Frame(self.mainframe, background='purple', name='row4')
        row4.grid(row=4, column=0, sticky='NSEW', pady=2, padx=2)

        row5 = tk.Frame(self.mainframe, background='orange', name='row5')
        row5.grid(row=5, column=0, sticky='NSEW', pady=2, padx=2)

        self.refresh_button = ttk.Button(row0, text='Refresh')
        self.refresh_button.pack(fill='both', expand=True)

        self.row_widgets_container: list[RowWidgets] = []
        self.row_widgets_container.append(
            self.create_champ_row_layout(row1))
        self.row_widgets_container.append(
            self.create_champ_row_layout(row2))
        self.row_widgets_container.append(
            self.create_champ_row_layout(row3))
        self.row_widgets_container.append(
            self.create_champ_row_layout(row4))
        self.row_widgets_container.append(
            self.create_champ_row_layout(row5))

        # btn = tk.Button(self.mainframe, text='Close')
        # btn.pack()
        # btn.bind('<Button>', lambda event, a=1, b=2: self.test(event, a, b))

        return

    # def test(self, event, a, b):
    #     print(event.num, a, b)

    def refresh(self):
        print('refresh')

    def create_champ_row_layout(self, row: tk.Frame) -> RowWidgets:
        champ_image = ttk.Label(row, text='ChampImage')
        champ_image.place(relx=0, rely=0, relwidth=0.4,
                          relheight=1, anchor='nw')

        champ_name = ''

        summoner_1_image = tk.Button(row, text='Summ1Image')
        summoner_1_image.place(relx=0.4, y=0, relwidth=0.2,
                               relheight=0.5, anchor='nw')

        summoner_1_cooldown = ttk.Label(row, text='Ready', foreground='green')
        summoner_1_cooldown.place(
            relx=0.6, rely=0, relwidth=0.3, relheight=0.5, anchor='nw')

        summoner_2_image = tk.Button(row, text='Summ2Image')
        summoner_2_image.place(relx=0.4, rely=0.5, relwidth=0.2,
                               relheight=0.5, anchor='nw')

        summoner_2_cooldown = ttk.Label(row, text='Ready', foreground='green')
        summoner_2_cooldown.place(relx=0.6, rely=0.5,
                                  relwidth=0.3, relheight=0.5, anchor='nw')

        move_row_up_button = ttk.Button(row, text='^')
        move_row_up_button.place(
            relx=0.9, rely=0, relwidth=0.1, relheight=0.5, anchor='nw')

        move_row_down_button = ttk.Button(row, text='v')
        move_row_down_button.place(
            relx=0.9, rely=0.5, relwidth=0.1, relheight=0.5, anchor='nw')

        enemy = None

        widgets = RowWidgets(row=row,
                             champion_image=champ_image,
                             champion_name=champ_name,
                             summoner_spell_one_image=summoner_1_image,
                             summoner_spell_one_cooldown=summoner_1_cooldown,
                             summoner_spell_two_image=summoner_2_image,
                             summoner_spell_two_cooldown=summoner_2_cooldown,
                             move_row_up_button=move_row_up_button,
                             move_row_down_button=move_row_down_button,
                             enemy=enemy)
        return widgets

    def configure_row_widgets(self, row_widgets: RowWidgets, enemy: EnemyData, main_obj) -> None:
        # Champ Name
        row_widgets['champion_name'] = enemy['champion_name']
        # Champ Image
        row_widgets['champion_image'].configure(
            image='', text=row_widgets['champion_name'])
        # Summoner 1 Image
        self.configure_text(row_widgets['summoner_spell_one_image'],
                            enemy['summoner_spells'][0]['name'])
        row_widgets['summoner_spell_one_image'].configure(image='')
        row_widgets['summoner_spell_one_image'].bind('<Button>', lambda event: main_obj.update_and_start_cooldown(
            event, enemy, enemy['summoner_spells'][0]['name']))
        # Summoner 1 Cooldown
        self.configure_text(
            row_widgets['summoner_spell_one_cooldown'], 'Ready')
        # Summoner 2 Image
        self.configure_text(row_widgets['summoner_spell_two_image'],
                            enemy['summoner_spells'][1]['name'])
        row_widgets['summoner_spell_two_image'].configure(image='')
        row_widgets['summoner_spell_two_image'].bind('<Button>', lambda event: main_obj.update_and_start_cooldown(
            event, enemy, enemy['summoner_spells'][1]['name']))
        # Summoner 2 Cooldown
        self.configure_text(
            row_widgets['summoner_spell_two_cooldown'], 'Ready')
        # Move Row Up Button
        self.configure_button(row_widgets['move_row_up_button'],
                              lambda: self.move_row_up(row_widgets))
        # Move Row Down Button
        self.configure_button(row_widgets['move_row_down_button'],
                              lambda: self.move_row_down(row_widgets))
        row_widgets['enemy'] = enemy
        return

    def update_icons(self) -> None:
        need_to_update = False
        for row_widgets in self.row_widgets_container:
            if row_widgets['enemy'] is None:
                assert False, 'Row has no enemy'
            if row_widgets['champion_image'].cget('image') == '':
                need_to_update = True
                break
        if not need_to_update:
            return
        for row_widgets in self.row_widgets_container:
            try:
                self.configure_champion_image(
                    row_widgets['champion_image'], image=row_widgets['enemy']['champion_icon'])  # type: ignore # nopep8
                self.configure_summoner_image(
                    row_widgets['summoner_spell_one_image'], image=row_widgets['enemy']['summoner_spells'][0]['icon'])  # type: ignore # nopep8
                self.configure_summoner_image(
                    row_widgets['summoner_spell_two_image'], image=row_widgets['enemy']['summoner_spells'][1]['icon'])  # type: ignore # nopep8
            except UnidentifiedImageError as e:
                print(f'Image for {row_widgets['champion_name']}!{
                      row_widgets['summoner_spell_one_image'].cget('text')} hasn\'t downloaded yet: {e}')
                self.root.after(500, self.update_icons)
                return None
        return None

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
        self.configure_button(self.refresh_button, func)

    def move_row_up(self, active_row_widgets) -> None:
        # Find row number
        row_number = active_row_widgets['row'].grid_info()['row']
        if row_number <= 1:
            return

        self.swap_rows(row_number, row_number-1)
        return

    def move_row_down(self, active_row_widgets) -> None:
        # Find row number
        row_number = active_row_widgets['row'].grid_info()['row']
        if row_number >= len(self.row_widgets_container):
            return

        self.swap_rows(row_number, row_number+1)
        return

    def swap_rows(self, row_number_1, row_number_2) -> None:
        row_1 = self.row_widgets_container[row_number_1-1]['row']
        row_2 = self.row_widgets_container[row_number_2-1]['row']

        row_1.grid(row=row_number_2)
        row_2.grid(row=row_number_1)

        self.row_widgets_container[row_number_1-1], self.row_widgets_container[
            row_number_2-1] = self.row_widgets_container[row_number_2-1], self.row_widgets_container[row_number_1-1]
        return

    def on_close(self):
        self.gtt.quit()
        self.root.destroy()
        sys.exit()


def main():
    """
    main()
    """
    app = App(GameTimeTracker())
    # pf = Pulsefire()
    # champ_image = pf.fetch_champ_image('Zoe')
    # app.configure_image(app.champions['champ1']['championImage'], champ_image)
    app.root.mainloop()


if __name__ == '__main__':
    main()
