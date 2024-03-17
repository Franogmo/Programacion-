"""
Goal of the program: A mutable class to substitute datetime.date
by Fran Ogallas
Development start date: 6th of February 2024. Last modification date: 15th of February 2024.
"""
from typeguard import typechecked


class NewDate:

    DAYS_EACH_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_TITLE = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                   "Noviembre", "Diciembre"]
    NAMES_OF_DAYS_OF_WEEK = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def __init__(self, day, month=None, year=None):
        if isinstance(day, NewDate) and month is None and year is None:
            another_date = day
            if self.validate_date(another_date.__year, another_date.__month, another_date.__day) is True:
                self.__day = another_date.__day
                self.__month = another_date.__month
                self.__year = another_date.__year
            else:
                raise ValueError("Has introducido una fecha u otra información que no es válida.")
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if self.validate_date(year, month, day) is True:
                self.__day = day
                self.__month = month
                self.__year = year
            else:
                raise ValueError("Has introducido una fecha u otra información que no es válida.")
        else:
            raise ValueError("Has introducido una fecha u otra información que no es válida.")

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @typechecked()
    def leap_year(self, given_year: int):
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

    def newdate_to_days(self, given_newdate):
        months_to_days = 0
        if given_newdate.__month > 1:
            for n in range((given_newdate.__month - 1)):
                months_to_days += NewDate.DAYS_EACH_MONTH[n]
                if n == 1 and given_newdate.leap_year(given_newdate.__year) is True:
                    months_to_days += 1
        leap_year_extra_days = 0
        for n in range(given_newdate.__year):
            if n > 0 and given_newdate.leap_year(n) is True:
                leap_year_extra_days += 1
        return (given_newdate.__year * 365) + leap_year_extra_days + months_to_days + given_newdate.__day

    def days_to_newdates_list(self, days_amount):
        days_left = days_amount
        day = 1
        month = 1
        year = 0
        while True:
            if (days_left > 365 and self.leap_year(year) is False) or (days_left > 366 and self.leap_year(year) is True):
                if self.leap_year(year) is False:
                    days_left -= 365
                else:
                    days_left -= 366
                year += 1
            else:
                break
        while days_left > 0 and days_left > (NewDate.DAYS_EACH_MONTH[(month - 1)]):
            if month == 2 and self.leap_year(year) is True and days_left >= 29:
                if days_left > 29:
                    days_left -= (NewDate.DAYS_EACH_MONTH[month - 1] + 1)
                    month += 1
                else:
                    break
            else:
                days_left -= NewDate.DAYS_EACH_MONTH[month - 1]
                month += 1
        if year == 0:
            year = 1
        return [(day + days_left), month, year]

    def validate_date(self, year, month, day):  # INPUT ORDER HERE IS YEAR - MONTH - DAY. Recycled from another program
        if year is None or month is None or day is None:
            print("1")
            return False
        elif year < 1 or year > 9999:
            print("2")
            return False
        elif month < 1 or month > 12:
            print("3")
            return False
        elif day < 1:
            print("4")
            return False
        elif day > NewDate.DAYS_EACH_MONTH[month - 1]:
            if month != 2 and self.leap_year(year) is False and day > 28:
                return False
            else:
                if day > 29:
                    return False
                else:
                    return True
        else:
            return True

    def set_date(self, day, month, year):
        validation = self.validate_date(year, month, day)
        if validation is True:
            self.__day = day
            self.__month = month
            self.__year = year
        elif validation is False:
            raise ValueError("ERROR. This date is not valid.")

    @typechecked()
    def change_newdate(self, change: int):
        total_days = self.newdate_to_days(self)
        total_days += change
        days_to_list = self.days_to_newdates_list(total_days)
        self.set_date(days_to_list[0], days_to_list[1], days_to_list[2])

    def __sub__(self, other):
        if isinstance(other, NewDate):
            operand1 = self.newdate_to_days(self)
            operand2 = self.newdate_to_days(other)
            return operand1 - operand2
        else:
            raise TypeError("NewDates can only subtract other NewDates")

    def __eq__(self, other):
        if isinstance(other, NewDate):
            if self.newdate_to_days(self) == self.newdate_to_days(other):
                return True
            else:
                return False
        else:
            raise TypeError("Sólo se puede comparar un dato tipo NewDate con otro dato tipo NewDate.")

    def __lt__(self, other):
        if isinstance(other, NewDate):
            if self.newdate_to_days(self) < self.newdate_to_days(other):
                return True
            else:
                return False
        else:
            raise TypeError("Sólo se puede comparar un dato tipo NewDate con otro dato tipo NewDate.")

    def __len__(self):
        return self.newdate_to_days(self)

    def __str__(self):
        return f"{self.__day} de {NewDate.MONTH_TITLE[(self.__month - 1)]} de {self.__year}"

    def compare_newdates(self, other):
        if self == other:
            return "Ambas son la misma fecha"
        else:
            if self < other:
                return f"{self} es una fecha más antigua que {other}"
            else:
                return f"{self} es una fecha más reciente que {other}"

    def week_day(self):
        x = self.__year - 1
        days_before_month = self.newdate_to_days(self) - self.__day
        week_day = (x % 7 + (x // 4 - (3 * (x // 100 + 1) // 4)) % 7 + days_before_month % 7 + self.__day % 7) % 7
        return NewDate.NAMES_OF_DAYS_OF_WEEK[week_day]


def main():
    date1 = NewDate(5, 1, 2024)
    print(date1)
    date2 = NewDate(date1)
    date2.change_newdate(6)
    print(date2)
    date3 = NewDate(date1)
    date3.change_newdate(-9)
    print(date3)
    date4 = date1 - date3
    print(f"{date4} días")
    print(date3 == date1)
    print(date3 < date1)
    print(f"¿El año de la fecha es bisiesto?: {date1.leap_year(date1.year)}")
    print(date1.week_day())


if __name__ == "__main__":
    main()
