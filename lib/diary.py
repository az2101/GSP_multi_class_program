class Diary:
    def __init__(self):
        self._entries = []
        
    def add(self, diary_entry):
        self._entries.append(diary_entry)

    def all(self):
        return self._entries
    
    


