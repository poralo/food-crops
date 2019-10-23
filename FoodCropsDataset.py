from FoodCropsFactory import FoodCropFactory
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Unit import Unit

import pandas

class FoodCropsDataset:
    def __init__(self, factory: FoodCropFactory):
        self.factory = factory

        self.__commodityMeasurementIndex = {}
        self.__indicatorGroupMeasurementIndex = {}
        self.__locationMeasurementIndex = {}
        self.__unitMeasurementIndex = {}

    def load(self, datasetPath: str):
        dataframe = pandas.read_csv("FeedGrains.csv")

        for index, row in dataframe.iterrows():
            self.factory.createIndicator(index)

    def findMeasurements(self, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> list:
        MeasurementList = ()
        if commodityGroup :
            for list in commodityType :
                for item in list :
                    if item == commodityGroup and item not in MeasurementList :
                        MeasurementList.add(item) // en supposant que les items dans nos dico soient des measurements
        if IndicatorGroup :
            for list in commodityType :
                for item in list :
                    if item == commodityGroup and item not in MeasurementList :
                        MeasurementList.add(item)
        if geographicalLocation :
            for list in commodityType :
                for item in list :
                    if item == commodityGroup and item not in MeasurementList :
                        MeasurementList.add(item)
        if unit :
            for list in commodityType :
                for item in list :
                    if item == commodityGroup and item not in MeasurementList :
                        MeasurementList.add(item)

        return MeasurementList
