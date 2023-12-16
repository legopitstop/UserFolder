import customtkinter
import UserFolder
from UserFolder import ctkdialog
from enum import Enum

user = UserFolder.User('_test')

class values(Enum):
    item1 = 'item1'
    item2 = 'item2'
    item3 = 'item3'
    item4 = 'item4'
    item5 = 'item5'

config = UserFolder.Config(section='metadata')
config.registerItem('option1', 'value1', str, 'Option1', 'String config item')
config.registerItem('option2', True, bool, 'Option2', 'Boolean config item')
config.registerItem('option3', 1, int, 'Option3', 'Integer config item', from_=0, to=10)
config.registerItem('option4', 1.0, float, 'Option4', 'Float config item', from_=0.0, to=1.0)
config.registerItem('option5', 50, range, 'Option5', 'Range config item')
config.registerItem('option6', values.item1, values, 'Option6', 'Enum config item')

root = customtkinter.CTk()
root.title('Main Window')
root.minsize(500, 500)
customtkinter.CTkButton(root, text='Open ConfigDialog', command=lambda: ctkdialog.CTkConfigDialog(parent=root)).pack()
customtkinter.CTkButton(root, text='Open User Folder', command=user.show).pack()
root.mainloop()