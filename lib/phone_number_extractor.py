import re

class PhoneNumberExtractor():
    def __init__(self, diary):
        self._diary = diary
        

    def extract_numbers(self):
        phone_numbers = []
        for entry in self._diary.all():
            contents = entry.contents
            phone_numbers += re.findall(r'\b0[0-9]{10}\b', contents)
        unique_phone_numbers =[]
        for phone_number in phone_numbers:
            if phone_number not in unique_phone_numbers:
                unique_phone_numbers.append(phone_number)
        return unique_phone_numbers
    

    


