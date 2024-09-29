import sys
from notes import Notebook

class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1':self.show_notes,
            '2':self.search_notes,
            '3':self.add_note,
            '4':self.modify_note,
            '5':self.quit,
        }
    
    def display_menu(self):
        print(
            """
    Notebook Menu

    1.Show all Notes
    2.Search Notes
    3.Add Note
    4.Modufy note
    5.Quit
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} in not a valid option.')
    
    def show_notes(self, notres=None):
        if not notres:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}:{note.title}\n{note.data}')
    
    def search_notes(self):
        filter = input('Enter filter: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_note(self):
        data = input('Enter note data: ')
        self.notebook.new_note(data)
        print('Note added successfully.')
    
    def modify_note(self):
        id = input('Enter note id: ')
        data = input('Enter a new data: ')
        title = input('Enter a new title: ')

        if data:
            self.notebook.modify_data(id, data)
        if title:
            self.notebook.modify_title(id, title)
    
    def quit(self):
        print('Thank you for using the notebook.')
        sys.exit()

if __name__ == '__main__':
    Menu().run()

