from Unit import Unit
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Indicator import Indicator
from MeasurementType import MeasurementType
from Commodity import Commodity
from Measurement import Measurement


class FoodCropFactory():

    def __init__(self):
        pass

    def createVolume(self, id: int) -> Unit:
        pass

    def createPrice(self, id: int) -> Unit:
        pass

    def createWeight(self, id: int, weight: float) -> Unit:
        pass

    def createSurface(self, id: int) -> Unit:
        pass

    def createCount(self, id: int, what: str) -> Unit:
        pass

    def createRatio(self, id: int) -> Unit:
        pass

    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit) -> Unit:
        pass

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Unit:
        pass

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        pass

    def createMesurement(self, id: int, description: str) -> MeasurementType:
        pass

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          type: MeasurementType, commodity: Commodity, indicator: Indicator) -> Measurement:
        pass
