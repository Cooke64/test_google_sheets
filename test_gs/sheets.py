from typing import Union, List

import gspread


gspread = gspread.service_account(
    filename='testtasks-353319-1e1a43323701.json')


class GetSheet:

    def __init__(self, gspread):
        self.gspread = gspread
        self.sheets = gspread.open("test")
        self.worksheet = self.sheets.sheet1

    def __last_filled_row(self):
        """Получаем количество заполненных строк в таблице."""
        str_list = list(filter(None, self.worksheet.col_values(1)))
        return len(str_list)

    def update_sheet(self, col: str, value: Union[int, str]):
        """Обновление определенной ячейки.
        Можем передавать строковый и числовой тип данных.
        """
        self.worksheet.update(col, value)

    def get_item_from_sell(self, cell: str) -> str:
        """Получение объекта из ячейки. В параметр cell
        передается значение искомой ячейки.
        """
        item = self.worksheet.acell(cell).value
        return item

    def get_last_row(self) -> List[int]:
        """Получение последнего обновленной строки в таблице.
        list_of_lists значение последней заполненной строки.
        """
        list_of_lists = self.worksheet.row_values(self.__last_filled_row())
        return list_of_lists


sheet = GetSheet(gspread)
