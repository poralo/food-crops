from Unit import Unit
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from MeasurementType import MeasurementType
from Commodity import Commodity
from Indicator import Indicator


class FoodCropFactory():

    def __init__(self):
        pass

    def createVolume(self, id: int) -> Unit:
        # Return Unit
        pass

    def createPrice(self, id: int):
        # Return Unit
        pass

    def createWeight(self, id: int, weight: float):
        # Return Unit
        pass

    def createSurface(self, id: int):
        # Return Unit
        pass

    def createCount(self, id: int, what: str):
        # Return Unit
        pass

    def createRatio(self, id: int):
        # Return Unit
        pass

    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit):
        # Return Unit
        pass

    def createCommodity(self, group: CommodityGroup, id: int, name: str):
        # Return Unit
        pass

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit):
        # Return Indicator
        pass

    def createMesurement(self, id: int, description: str):
        # Return MeasurementType
        pass

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          type: MeasurementType, commodity: Commodity, indicator: Indicator):
        # Return Measurement
        pass
