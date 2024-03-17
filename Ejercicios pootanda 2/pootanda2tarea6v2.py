"""
Goal of the program: A duration object to store timespans inside of it.
by Fran Ogallas
Development start date: 29th of January 2024. Last modification date: 16th of February 2024.
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Duration:

    SECONDS_EACH_MINUTE = 60
    MINUTES_EACH_HOUR = 60

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and minutes is None and seconds is None:
            another_duration = hours
            self.__hours = another_duration.__hours
            self.__minutes = another_duration.__minutes
            self.__seconds = another_duration.__seconds
        else:
            self.duration_setter(hours, minutes, seconds)

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value: int):
        if value < 0:
            raise ValueError("Hours must not have a negative value")
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value: int):
        self.duration_setter(self.__hours, value, self.__seconds)

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        self.duration_setter(self.__hours, self.__minutes, value)

    def adjust_duration(self, hours, minutes, seconds):
        extra_minutes = seconds // Duration.SECONDS_EACH_MINUTE
        seconds % Duration.SECONDS_EACH_MINUTE
        if seconds >= Duration.SECONDS_EACH_MINUTE:
            seconds = seconds % Duration.SECONDS_EACH_MINUTE
        elif seconds < 0:
            seconds = Duration.SECONDS_EACH_MINUTE - (seconds % (Duration.SECONDS_EACH_MINUTE))

        minutes += extra_minutes

        extra_hours = minutes // Duration.MINUTES_EACH_HOUR
        if minutes >= Duration.MINUTES_EACH_HOUR:
            minutes = minutes % Duration.MINUTES_EACH_HOUR
        elif minutes < 0:
            minutes = Duration.MINUTES_EACH_HOUR - (minutes % (Duration.MINUTES_EACH_HOUR))

        hours += extra_hours
        if hours < 0:
            raise ValueError("Has generado una duración negativa.")

        return [hours, minutes, seconds]

    def duration_setter(self, hours, minutes, seconds):
        adjustment = self.adjust_duration(hours, minutes, seconds)
        if adjustment[0] < 0:
            raise ValueError("Has generado una duración negativa.")
        else:
            self.__hours = adjustment[0]
            self.__minutes = adjustment[1]
            self.__seconds = adjustment[2]

    def __str__(self):
        return f"{self.__hours}h, {self.__minutes}min y {self.__seconds} segundos"

    def add_hours(self, change: int):
        self.hours += change

    def add_minutes(self, change: int):
        self.minutes += change

    def add_seconds(self, change: int):
        self.seconds += change

    def subtract_hours(self, change: int):
        self.hours -= change

    def subtract_minutes(self, change: int):
        self.minutes -= change

    def subtract_seconds(self, change: int):
        self.seconds -= change

    def __add__(self, other: Duration):
        result_hours = self.__hours + other.__hours
        result_minutes = self.__minutes + other.__minutes
        result_seconds = self.__seconds + other.__seconds
        return Duration(result_hours, result_minutes, result_seconds)

    def __sub__(self, other):
        result_hours = self.__hours - other.__hours
        result_minutes = self.__minutes - other.__minutes
        result_seconds = self.__seconds - other.__seconds
        return Duration(result_hours, result_minutes, result_seconds)


def main():
    print("Programa para testear objetos de la clase Duration:\n")
    duration1 = Duration(1, 30, 30)
    print(f"Duración 1: {duration1}")
    duration2 = Duration(duration1)
    print("Tras crear una copia de la Duración 1, procedemos a modificarla para que sea distinta.")
    duration2.subtract_minutes(-80)
    print(f"Duración 2: {duration2}")
    duration3 = duration1 + duration2
    print(f"Duración 3: {duration3}")
    duration4 = duration2 - duration1
    print(f"Duración 4: {duration4}")


if __name__ == "__main__":
    main()
