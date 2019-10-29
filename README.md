# Food Crops Project
L'objectif de ce projet est de créer une API permettant de traiter et manipuler les données venant du fichier "FeedGrains.csv".
  
  
## L'API s'utilise comme suit:
### Chargement des données :
  ```python
  # Création d'une usine pour instancier les différents objets
  factory = FoodCropFactory()
  
  # Création de l'objet principal pour le traitement des données
  fcd = FoodCropsDataset(factory)
  # Chargement des données venant de "FeedGrains.csv"
  fcd.load("FeedGrains.csv")
  ```

### Utilisation des données :
Pour retrouver la valeur d'une ou plusieurs mesures on utilise la méthode findMeasurement de FoodCropsDataset qui prend en argument le groupe des cultures vivière (`CommodityGroup()`), le groupe de l'indicateur (`IndicatorGroup`), la position géographique et l'unité.

Exemple :

```python
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup

# Trouver le prix qui correspondent aux cultures de sorghum.
fcd.findMeasurements(CommodityGroup.SORGHUM, IndicatorGroup.PRICES)
```

