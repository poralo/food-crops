from IndicatorGroup import IndicatorGroup
from Unit import Unit
from Describable import Describable

class Indicator(Describable):

    def __init__(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup, unit: Unit):
        self.id = id
        self.unit = unit
        self.indicatorGroup = indicatorGroup
        self.__frequency = frequency
        self.__frequencyDesc = freqDesc
        self.__geogLocation = geogLocation

    def describe(self):
        return f'Indicator {self.id} : unité-{self.unit}, localisation-{self.__geogLocation}, fréquence-{self.__frequencyDesc}  '
