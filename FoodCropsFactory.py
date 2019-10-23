from Unit import Unit
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Indicator import Indicator
from MeasurementType import MeasurementType
from Commodity import Commodity
from Measurement import Measurement

from Weight import Weight


class FoodCropFactory():

    def __init__(self):
        pass

    def createVolume(self, id: int) -> Volume:
        pass

    def createPrice(self, id: int) -> Price:
        pass

    def createWeight(self, id: int, weight: float) -> Weight:
        w = Weight(id, weight)
        return w

    def createSurface(self, id: int) -> Surface:
        pass

    def createCount(self, id: int, what: str) -> Count:
        pass

    def createRatio(self, id: int) -> Ratio:
        pass

    def createUnitRatio(self, id: int, unit1: Unit, unit2: Unit) -> UnitRation:
        pass

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Commodity:
        pass

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        pass

    def createMesurement(self, id: int, description: str) -> MeasurementType:
        pass

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          type: MeasurementType, commodity: Commodity, indicator: Indicator) -> Measurement:
        pass
