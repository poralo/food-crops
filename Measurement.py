from MeasurementType import MeasurementType
from Commodity import Commodity
from Indicator import Indicator

class Measurement ():
    def __init__ (self, year : int, value : float, timeperiodId : int, timeperiodDescr : str, type : MeasurementType, commodity : Commodity, indicator : Indicator):
        self.year = year
        self.value = value
        self.timeperiodId = timeperiodId
        self.timeperiodDescr = timeperiodDescr
        self.type = type
        self.commodity = commodity
        self.indicator = indicator
