from CommodityGroup import CommodityGroup

class Commodity():

    def __init__(self, group: CommodityGroup, id: int, name: str):
        self.id = id
        self.__name = name
