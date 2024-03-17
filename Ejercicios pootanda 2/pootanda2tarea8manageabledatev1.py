"""
Goal of the program: Dates management.
by Fran Ogallas
Development start date: 4th of February 2024. Last modification date: 11th of February 2024.
"""

import datetime
from pootanda2tarea8menu import Menu


class ManageableDate:

    days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_title = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                   "Noviembre", "Diciembre"]

    def __init__(self, date=None):
        self.__date = date

    @property
    def date(self):
        return self.__date


    def int_input_service(self):
        while True:
            input_operand = input("Introduce el número a operar: ")
            try:
                input_operand = int(input_operand)
                break
            except ValueError:
                print("Valor erróneo.")
        return input_operand

    @staticmethod
    def leap_year(given_year):
        if given_year % 4 == 0:
            if given_year % 100 == 0:
                if given_year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def date_to_list(self, date):
        if type(date) == datetime.date:
            return [date.year, date.month, date.day]
        else:
            raise ValueError("date_to_list() was not input a datetime.date value")

    def date_to_days(self, date):
        if type(date) == datetime.date:
            finished_months = 0
            for n in range((date.month -2)):
                finished_months += ManageableDate.days_each_month[n]
            leap_year_extra_days = 0
            for n in range(date.year):
                if self.leap_year(n) is True:
                    leap_year_extra_days += 1
            return (date.year * 365) + leap_year_extra_days + finished_months + date.day
        else:
            raise ValueError("date_to_list() was not input a datetime.date value")

    def tomorrow(self, date_list): # date_list was [year, month, day]
        output_date = date_list.copy()
        output_date[2] = output_date[2] + 1
        if output_date[1] == 2 and self.leap_year(output_date[0]) is True:
            if output_date[2] > 29:
                output_date[1] += 1
                output_date[2] = 1
        elif output_date[2] > ManageableDate.days_each_month[(output_date[1] - 1)]:
            output_date[1] += 1
            output_date[2] = 1
        if output_date[1] > len(ManageableDate.days_each_month):
            output_date[0] += 1
            output_date[1] = 1
            output_date[2] = 1
        if output_date[0] > 9999:
            raise ValueError("year is over nine thousand (nine hundred ninety-nine")
        else:
            return output_date

    def yesterday(self, date_list): # date_list was [year, month, day]
        output_date = date_list.copy()
        output_date[2] = output_date[2] - 1
        if output_date[1] == 3 and self.leap_year(output_date[0]) is True and output_date[2] < 1:
            output_date[1] = 2
            output_date[2] = 29
        elif output_date[2] < 1:
            output_date[1] -= 1
            output_date[2] = ManageableDate.days_each_month[output_date[1]]
        if output_date[1] <= 0:
            output_date[0] -= 1
            output_date[1] = 12
            output_date[2] = 31
        if output_date[0] < 1:
            raise ValueError("This program does not work with dates before 01-01-0001")
        else:
            return output_date

    def change_n_days(self, given_amount, date_list):
        output_date = date_list.copy()
        if given_amount == 0:
            return date_list
        else:
            for n in range(abs(given_amount)):
                if given_amount < 0:
                    output_date = self.yesterday(output_date)
                elif given_amount > 0:
                    output_date = self.tomorrow(output_date)
            return output_date

    def change_month(self, given_amount, date_list): # date_list was [year, month, day]
        output_date = date_list.copy()
        if given_amount == 0:
            return date_list
        else:
            for n in range(abs(given_amount)):
                days_this_month = ManageableDate.days_each_month[(output_date[1] - 1)]
                if given_amount == 0:
                    return output_date
                else:
                    if output_date[1] == 2 and self.leap_year(output_date[0]) is True:
                        days_this_month = 29
                    if given_amount < 0:
                        output_date = self.change_n_days(-days_this_month, output_date)
                    elif given_amount > 0:
                        output_date = self.change_n_days(days_this_month, output_date)
            return output_date

    def change_year(self, given_amount, date_list): # date_list was [year, month, day]
        output_date = date_list.copy()
        for n in range(abs(given_amount)):
            if given_amount > 0:
                output_date = self.change_month(12, output_date)
            elif given_amount < 0:
                output_date = self.change_month(-12, output_date)
        return output_date


    @staticmethod
    def input_format_validator():
        while True:
            input_date = input("Introduce una fecha con el formato dd/mm/aaaa (o me cargo el programa): ")
            date_testtool = input_date
            for n in range(len(input_date)):
                if ord(input_date[n]) > 47 and ord(input_date[n]) < 58:
                    date_testtool = date_testtool[:n] + "X" + date_testtool[(n + 1):]
            if date_testtool == "XX/XX/XXXX":
                return input_date
            else:
                print("Error de introducción. Introduce la fecha de nuevo")

    @staticmethod
    def date_reformatter(given_input_date):
        input_day = int(given_input_date[0:2])
        input_month = int(given_input_date[3:5])
        input_year = int(given_input_date[6:11])
        return [input_year, input_month, input_day]

    @staticmethod
    def input_date():
        keyboard_input = (ManageableDate.date_reformatter(ManageableDate.input_format_validator()))
        year = keyboard_input[0]
        month = keyboard_input[1]
        day = keyboard_input[2]
        return [year, month, day]

    @staticmethod
    def validate_date(year, month, day):
        if year is None or month is None or day is None:
            return False
        elif year < 1 or year > 9999:
            return False
        elif month < 1 or month > 12:
            return False
        elif day < 1:
            return False
        elif day > ManageableDate.days_each_month[month - 1]:
            if month != 2 or ManageableDate.leap_year(year) is False and day > 28:
                return False
            else:
                if day > 29:
                    return False
                else:
                    return True
        else:
            return True

    def set_date(self, year, month, day, validation):
        if validation is True:
            self.__date = datetime.date(year, month, day)
        elif validation is False:
            raise ValueError("ERROR. This date is not valid.")

    def setter_macrotool(self):
        given_date = self.input_date()
        year = given_date[0]
        month = given_date[1]
        day = given_date[2]
        green_light = self.validate_date(year, month, day)
        self.set_date(year, month, day, green_light)

    def day_difference(self, date1, date2):
        return self.date_to_days(date1) - self.date_to_days(date2)

    def comparison_macrotool(self, given_date):
        year = given_date[0]
        month = given_date[1]
        day = given_date[2]
        green_light = self.validate_date(year, month, day)
        if green_light is False:
            raise ValueError("ERROR. The second date of the comparison is not valid.")
        given_date = datetime.date(year, month, day)
        if self.__date == given_date:
            return "Ambas son la misma fecha."
        else:
            if self.__date > given_date:
                return (f"La fecha introducida es más ANTIGUA que la fecha almacenada."
                        f"\ncon una diferencia de {self.day_difference(self.__date, given_date)} días.")
            else:
                return (f"La fecha introducida es más RECIENTE que la fecha almacenada."
                        f"\ncon una diferencia de {self.day_difference(given_date, self.__date)} días.")

    def __str__(self):
        date_list = self.date_to_list(self.__date)
        return f"{date_list[2]} de {ManageableDate.month_title[(date_list[1] - 1)]} de {date_list[0]}"

    def manage_days(self):
        amount = self.int_input_service()
        date_list = self.date_to_list(self.__date)
        new_date = self.change_n_days(amount, date_list)
        self.set_date(new_date[0], new_date[1], new_date[2], True)

    def manage_months(self):
        amount = self.int_input_service()
        date_list = self.date_to_list(self.__date)
        new_date = self.change_month(amount, date_list)
        self.set_date(new_date[0], new_date[1], new_date[2], True)

    def manage_years(self):
        amount = self.int_input_service()
        date_list = self.date_to_list(self.__date)
        new_date = self.change_year(amount, date_list)
        self.set_date(new_date[0], new_date[1], new_date[2], True)

    def __eq__(self, other):
        if type(other) == ManageableDate:
            return self.date_to_days(self) == self.date_to_days(other)

    def __gt__(self, other):
        if type(other) == ManageableDate:
            return self.date_to_days(self) > self.date_to_days(other)

def main():
    stored_date = ManageableDate()
    menu = Menu("Introducir una fecha", "Añadir días", "Añadir meses",
                "Añadir años", "Comparar la fecha almacenada con otra", "Mostrar fecha",
                "Terminar")
    while True:
        option = menu.choose()
        if option != 1 and stored_date.date is None and option != menu.last_option:
            print("Debes introducir primero una fecha\n")
        else:
            if option == 1:
                stored_date.setter_macrotool()
                print("Su fecha ha sido almacenada con éxito.")
            elif option == 2:
                stored_date.manage_days()
            elif option == 3:
                stored_date.manage_months()
            elif option == 4:
                stored_date.manage_years()
            elif option == 5:
                input_date = ManageableDate.input_date()
                print(stored_date.comparison_macrotool(input_date))
            elif option == 6:
                print(stored_date)
            elif option == 7:
                break
            else:
                print("ERROR. Opción no aceptada. Volviendo al menú principal...")

if __name__ == "__main__":
    main()
