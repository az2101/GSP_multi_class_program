
class ReadableEntryFinder():
    def __init__(self, diary):
        self._diary = diary

    def extract(self, wpm, minutes):
        readable_entries = [entry for entry in self._diary.all() if self._entry_readable_in_time(wpm, minutes, entry)]

        if len(readable_entries) == 0:
            return None
        return max(readable_entries, key=lambda entry: self._word_count(entry.contents))

    def _entry_readable_in_time(self, wpm, minutes, entry):
        readable_amount = wpm * minutes
        return self._word_count(entry.contents) <= readable_amount
    
    def _word_count(self, string):
        return len(string.split())
    
    
