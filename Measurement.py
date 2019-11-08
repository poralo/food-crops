from Commodity import Commodity
from Indicator import Indicator
from Describable import Describable

class Measurement(Describable):
    def __init__ (self, id: int, year : int, value : float, timeperiodId : int, timeperiodDescr : str, commodity : Commodity, indicator : Indicator):
        self.__year = year
        self.__value = value
        self.__timeperiodId = timeperiodId
        self.__timeperiodDescr = timeperiodDescr
        self.commodity = commodity
        self.indicator = indicator

    def descibe(self):
        return f'Measurement of {self.__value}: année-{self.__year}, période-{self.__timeperiod}-{self.__timeperiodDescr}, commodity-{self.commodity}, indicator-{self.indicator}'
