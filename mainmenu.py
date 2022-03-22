from tkinter import Tk, Menu

root = Tk()
root.title('Menu')


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Close')
file_menu.add_separator()

sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Option 1')
sub_menu.add_command(label='Option 2')

file_menu.add_cascade(
    label="More Help",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="Greetings User!",
    menu=file_menu,
    underline=0
)

help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')

root.mainloop()