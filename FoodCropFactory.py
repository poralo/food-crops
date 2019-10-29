from Unit import Unit
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Indicator import Indicator
from MeasurementType import MeasurementType
from Commodity import Commodity
from Measurement import Measurement

from Price import Price
from Weight import Weight
from Volume import Volume
from Surface import Surface
from Count import Count
from Ratio import Ratio
from UnitRatio import UnitRatio
import pandas


class FoodCropFactory():

    def __init__(self):
        self.__unitsRegistry = {}
        self.__indicatorsRegistry = {}
        self.__commodityRegistry = {}
        self.__measurementTypeRegistry = {}

    def createVolume(self, id: int) -> Unit:
        if id not in self.__unitsRegistry:
            u = Volume(id)
            self.__unitsRegistry[id] = u
            return u
        else:
            return self.__unitsRegistry[id]

    def createPrice(self, id: int) -> Unit:
        if id not in self.__unitsRegistry:
            p = Price(id)
            self.__unitsRegistry[id] = p
            return p
        else:
            return self.__unitsRegistry[id]

    def createWeight(self, id: int, weight: float) -> Unit:
        if id not in self.__unitsRegistry:
            w = Weight(id, weight)
            self.__unitsRegistry[id] = w
            return w
        else:
            return self.__unitsRegistry[id]

    def createSurface(self, id: int) -> Unit:
        if id not in self.__unitsRegistry:
            s = Surface(id)
            self.__unitsRegistry[id] = s
            return s
        else:
            return self.__unitsRegistry[id]

    def createCount(self, id: int, what: str) -> Unit:
        if id not in self.__unitsRegistry:
            c = Count(id)
            self.__unitsRegistry[id] = c
            return c
        else:
            return self.__unitsRegistry[id]

    def createRatio(self, id: int) -> Unit:
        if id not in self.__unitsRegistry:
            r = Ratio(id)
            self.__unitsRegistry[id] = r
            return r
        else:
            return self.__unitsRegistry[id]

    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit) -> Unit:
        if id not in self.__unitsRegistry:
            ur = UnitRatio(id, unit1, unit2)
            self.__unitsRegistry[id] = ur
            return ur
        else:
            return self.__unitsRegistry[id]

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Commodity:
        if id not in self.__commodityRegistry :
            c = Commodity(group, id, name)
            self.__commodityRegistry[id] = c
            return c
        else:
            return self.__commodityRegistry[id]

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        if id not in self.__indicatorsRegistry:
            i = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
            self.__indicatorsRegistry[id] = i
            return i
        else:
            return self.__indicatorsRegistry[id]

    def createMeasurementType(self, id: int, description: str) -> MeasurementType:
        if id not in self.__measurementTypeRegistry:
            m = MeasurementType(id, description)
            self.__measurementTypeRegistry[id] = m
            return m
        else:
            return self.__measurementTypeRegistry[id]

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          type: MeasurementType, commodity: Commodity, indicator: Indicator) -> Measurement:
        m = Measurement(id, year, value, timeperiodDesc, type, commodity, indicator)
        return m
