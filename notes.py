import datetime


last_id = 0

def get_current_datetime():
    data = datetime.datetime.today().__format__("%Y-%m-%d %H:%M:%S")
    return data

def change_id():
    global last_id
    last_id += 1
    return last_id

class Note:
    def __init__(self, data, title=''):
        self.data = data
        self.title = title
        self.created_date = get_current_datetime()
        self.id = change_id()

    def searched(self, filter):
        return filter in self.data or filter in self.title
    
    def get_id(self):
        return self.id
    
    
class Notebook:
    def __init__(self):
        self.notes = []
    
    def new_note(self, data, titile=''):
        self.notes.append(Note(data, titile))
    
    def _search_note(self, note_id:str):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def modify_data(self, note_id, data):
        note = self._search_note(note_id)
        if note:
            note.data = data
            return True
        return False
    
    def modify_title(self, note_id, title):
        note = self._search_note(note_id)
        if note:
            note.title = title
            return True
        return False
    
    def search(self, filter):
        return [note for note in self.notes if note.searched(filter)]


