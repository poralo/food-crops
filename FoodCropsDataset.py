from FoodCropsFactory import FoodCropFactory
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Unit import Unit

class FoodCropsDataset:
    def __init__(self, factory: FoodCropFactory):
        self.factory = factory

    def load(self, datasetPath: str):
        pass

    def findMeasurements(self, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> list:
        pass