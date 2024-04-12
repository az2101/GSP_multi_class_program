from dataclasses import dataclass

@dataclass
class DiaryEntry:
    title: str
    contents: str
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self.title = title
        self.contents = contents
        


