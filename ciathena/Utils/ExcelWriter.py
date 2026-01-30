from openpyxl import Workbook

class ExcelWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.row = 1
        # Write header
        self.sheet.cell(row=1, column=1, value="Question")
        self.sheet.cell(row=1, column=2, value="Answer")
        self.sheet.cell(row=1, column=3, value="SQL_Query")
        self.sheet.cell(row=1, column=4, value="SQL_icon")
        self.sheet.cell(row=1, column=5, value="Share_icon")
        self.sheet.cell(row=1, column=6, value="Save_icon")
        self.sheet.cell(row=1, column=7, value="View_fullscreen_icon")
        self.sheet.cell(row=1, column=8, value="data_view_icon")
        self.sheet.cell(row=1, column=9, value="Download_icon")
        self.sheet.cell(row=1, column=10, value="STATUS")


    def write_row(self, question, answer, sql_query, sql_icon,share_icon,save_icon,view_fullscreen_icon,data_view_icon, download_icon,status):
        self.row += 1
        self.sheet.cell(row=self.row, column=1, value=question)
        self.sheet.cell(row=self.row, column=2, value=answer)
        self.sheet.cell(row=self.row, column=3, value=sql_query)
        self.sheet.cell(row=self.row, column=4, value=sql_icon)
        self.sheet.cell(row=self.row, column=5, value=share_icon)
        self.sheet.cell(row=self.row, column=6, value=save_icon)
        self.sheet.cell(row=self.row, column=7, value=view_fullscreen_icon)
        self.sheet.cell(row=self.row, column=8, value=data_view_icon)
        self.sheet.cell(row=self.row, column=9, value=download_icon)
        self.sheet.cell(row=self.row, column=10, value=status)


    def save(self):
        self.wb.save(self.file_path)
