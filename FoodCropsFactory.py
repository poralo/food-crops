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


class FoodCropFactory():

    def __init__(self):
        self.__unitsRegistry = {}
        self.__indicatorsRegistry = {}
        self.__commodityRegistry = {}
        self.__measurementTypeRegistry = {}

    def createVolume(self, id: int) -> Unit:
        # Vérifier que l'unité n'existe pas déjà
        v = Volume(id)
        return v

    def createPrice(self, id: int) -> Unit:
        p = Price(id)
        return p

    def createWeight(self, id: int, weight: float) -> Unit:
        w = Weight(id, weight)
        return w

    def createSurface(self, id: int) -> Unit:
        s = Surface(id)
        return s

    def createCount(self, id: int, what: str) -> Unit:
        c = Count(id, what)
        return c

    def createRatio(self, id: int) -> Unit:
        r = Ratio(id)
        return r

    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit) -> Unit:
        u = UnitRatio(id, unit1, unit2)
        return u

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Unit:
        if id not in commodityRegistry :
            c = Commodity(group, id, name)
            commodityRegistry[id] = group,name
            return c

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        i = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
        return i

    def createMaesurementType(self, id: int, description: str) -> MeasurementType:
        m = MeasurementType(id, description)
        return m

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          type: MeasurementType, commodity: Commodity, indicator: Indicator) -> Measurement:
        m = Measurement(id, year, value, timeperiodDesc, type, commodity, indicator)
        return m
