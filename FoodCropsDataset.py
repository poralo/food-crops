from FoodCropFactory import FoodCropFactory
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
        dataframe = pandas.read_csv(datasetPath)

        for index, row in dataframe.head().iterrows():
            # Récupération du groupe de l'indicateur
            indicatorGroup = IndicatorGroup(row["SC_Group_ID"])
            # Création/récupération de l'unité de l'indicateur
            id = row["SC_Unit_ID"]
            unit = self.factory.createPrice(id)
            # Création/récupération de l'indicateur
            indicator = self.factory.createIndicator(row["SC_Attribute_ID"], row["SC_Frequency_ID"], row["SC_Frequency_Desc"], row["SC_Geography_ID"], indicatorGroup, unit)
            
            # Récupération de groupe de la commodité
            commodityGroup = CommodityGroup(row["SC_GroupCommod_ID"])
            # Crétion/récupération de la commodité
            commodity = self.factory.createCommodity(commodityGroup, row["SC_Commodity_ID"], row["SC_Commodity_Desc"])
            
            # Création/récupération du type de mesure
            measurementType = self.factory.createMeasurementType(0, "Ceci est un test")

            # Création de la mesure
            measurement = self.factory.createMeasurement(index, row["Year_ID"], row["Amount"], row["Timeperiod_ID"], row["Timeperiod_Desc"], measurementType, commodity, indicator)

    def findMeasurements(self, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> list:
        MeasurementList = ()
        if commodityGroup :
            for list in commodityType :
                for item in list :
                    if item == commodityGroup and item not in MeasurementList :
                        MeasurementList.add(item) # en supposant que les items dans nos dico soient des measurements
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

if __name__ == "__main__":
    f = FoodCropFactory()
    fcd = FoodCropsDataset(f)
    fcd.load("FeedGrains.csv")

    print(fcd.findMeasurements())
