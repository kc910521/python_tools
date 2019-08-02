#!/usr/bin/python3

import xlrd


class ExcelUtils:

    def __init__(self, directory, sheet_number=0):
        self.book = xlrd.open_workbook(directory)  # 打开一个excel
        self.bookSheetNumber = sheet_number
        self.sheet = self.book.sheet_by_index(self.bookSheetNumber)

    def export_value_of(self, row_number=0, col_number=0):
        return self.sheet.cell(row_number, col_number).value

    def get_rows(self):
        return self.sheet.get_rows()

    def accelerate(self):
        pass


if __name__ == '__main__':
    print("hello my fucking world")
    # with open("/home/caikun/Documents/fucku.txt", "r", encoding="utf-8") as f:
    #     fTextList = f.readlines()

    exceltool = ExcelUtils('/home/caikun/.deepinwine/Deepin-WXWork/drive_c/users/caikun/Downloads/55024-20190725.xlsx')

    appIdList = []
    for i in exceltool.get_rows():
        # 筛掉4列为0的数据
        if i[4].value != 0:
            # print(i[4])
            appIdList.append(str(i[3].value))
    # my_car = Car()
    # my_car.fetchDt(appIdList)
    print(appIdList)


# my_car = Car()
    # print("I'm a car!")
    # while True:
    #     action = input("What should I do? [A]ccelerate, [B]rake, "
    #              "show [O]dometer, or show average [S]peed?").upper()
    #     if action not in "ABOS" or len(action) != 1:
    #         print("I don't know how to do that")
    #         continue
    #     if action == 'A':
    #         my_car.accelerate()
    #     elif action == 'B':
    #         my_car.brake()
    #     elif action == 'O':
    #         print("The car has driven {} kilometers".format(my_car.odometer))
    #     elif action == 'S':
    #         print("The car's average speed was {} kph".format(my_car.average_speed()))
    #     my_car.step()
    #     my_car.say_state()