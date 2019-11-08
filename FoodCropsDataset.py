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

        self.__measurements = []

    def load(self, datasetPath: str):
        dataframe = pandas.read_csv(datasetPath)
        dataframe = dataframe.dropna()
        dataframe.reset_index(drop=True)

        units = {
            1: self.factory.createCount(1, "Million bushels"),
            2: self.factory.createSurface(2, "Million acres"),
            3: self.factory.createVolume(3, "Bushels"),
            4: self.factory.createUnitRatio(4, self.factory.createPrice(100, "Dollars"), self.factory.createVolume(101, "bushel"), "Dollars per bushel"),
            5: self.factory.createUnitRatio(5, self.factory.createPrice(100, "Dollars"), self.factory.createWeight(102, 1, "cwt"), "Dollars per cwt"),
            6: self.factory.createUnitRatio(6, self.factory.createWeight(3, 1, "Bushels"), self.factory.createSurface(103, "acre"), "Bushels per acre"),
            7: self.factory.createWeight(7, 1, "1,000 metric tons"),
            8: self.factory.createWeight(8, 1, "Million metric tons"),
            9: self.factory.createWeight(9, 1, "1,000 tons"),
            10: self.factory.createSurface(10, "1,000 acres"),
            11: self.factory.createUnitRatio(11, self.factory.createWeight(104, 1, "Tons"), self.factory.createSurface(103, "acre"), "Tons per acre"),
            12: self.factory.createUnitRatio(11, self.factory.createPrice(100, "Dollars"), self.factory.createWeight(105, 1, "ton"), "Dollars per ton"),
            13: self.factory.createRatio(13, "Ratio"),
            14: self.factory.createUnitRatio(14, self.factory.createPrice(106, "Cents"), self.factory.createWeight(107, 1, "pound"), "Cents per pound"),
        }

        for index, row in dataframe.iterrows():
            # Récupération du groupe de l'indicateur
            indicatorGroup = IndicatorGroup(row["SC_Group_ID"])
            # Création/récupération de l'unité de l'indicateur
            id = row["SC_Unit_ID"]
            createUnit = units[id]
            unit = createUnit(id, row["SC_Unit_Desc"])
            # Création/récupération de l'indicateur
            indicator = self.factory.createIndicator(row["SC_Attribute_ID"], row["SC_Frequency_ID"], row["SC_Frequency_Desc"], row["SC_Geography_ID"], indicatorGroup, unit)
            
            # Récupération de groupe des cultures vivières
            commodityGroup = CommodityGroup(row["SC_GroupCommod_ID"])
            # Crétion/récupération de la culture vivière
            commodity = self.factory.createCommodity(commodityGroup, row["SC_Commodity_ID"], row["SC_Commodity_Desc"])
    
            # Création de la mesure
            measurement = self.factory.createMeasurement(index, row["Year_ID"], row["Amount"], row["Timeperiod_ID"], row["Timeperiod_Desc"], commodity, indicator)
            self.__measurements.append(measurement)

            if commodityGroup in self.__commodityMeasurementIndex:
                self.__commodityMeasurementIndex[commodityGroup].append(measurement)
            else:
                self.__commodityMeasurementIndex[commodityGroup] = [measurement]

            if indicatorGroup in self.__indicatorGroupMeasurementIndex:
                self.__indicatorGroupMeasurementIndex[indicatorGroup].append(measurement)
            else:
                self.__indicatorGroupMeasurementIndex[indicatorGroup] = [measurement]

            if row["SC_GeographyIndented_Desc"] in self.__locationMeasurementIndex:
                self.__locationMeasurementIndex[row["SC_GeographyIndented_Desc"]].append(measurement)
            else:
                self.__locationMeasurementIndex[row["SC_GeographyIndented_Desc"]] = [measurement]

            if unit in self.__unitMeasurementIndex:
                self.__unitMeasurementIndex[unit].append(measurement)
            else:
                self.__unitMeasurementIndex[unit] = [measurement]

    def findMeasurements(self, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> list:
        measurementList = self.__measurements[:]
        if commodityGroup is not None:
            new_list = []
            l = self.__commodityMeasurementIndex.get(commodityGroup, [])
            for measure in measurementList:
                if measure in l:
                    new_list.append(measure)
            measurementList = new_list

        if indicatorGroup is not None:
            new_list = []
            l = self.__indicatorGroupMeasurementIndex.get(indicatorGroup, [])
            for measure in measurementList:
                if measure in l:
                    new_list.append(measure)
            measurementList = new_list

        if geographicalLocation is not None:
            new_list = []
            l = self.__locationMeasurementIndex.get(geographicalLocation, [])
            for measure in measurementList:
                if measure in l:
                    new_list.append(measure)
            measurementList = new_list
        
        if unit is not None:
            new_list = []
            l = self.__unitMeasurementIndex.get(unit, [])
            for measure in measurementList:
                if measure in l:
                    new_list.append(measure)
            measurementList = new_list

        return measurementList

if __name__ == "__main__":
    f = FoodCropFactory()
    fcd = FoodCropsDataset(f)
    fcd.load("FeedGrains.csv")

    print(fcd.findMeasurements(CommodityGroup.SORGHUM, IndicatorGroup.TRANSPORTATION))

