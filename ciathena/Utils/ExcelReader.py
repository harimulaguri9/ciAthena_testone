from openpyxl import load_workbook

class ExcelReader:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.wb = load_workbook(file_path)
        self.sheet = self.wb[sheet_name]

    def get_questions(self):
        questions = []
        for row in self.sheet.iter_rows(min_row=2, values_only=True):  # skip header
            if row[0]:
                questions.append(row[0])
        return questions
