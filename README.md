# Food Crops Project
L'objectif de ce projet est de créer une API permettant de traiter et manipuler les données venant du fichier "FeedGrains.csv".

## Environnement de développement
Version de python
> python 3.7

Systèmes d'exploitation
> Windows et Mac

Librairie python 
> pandas

Pour installer les modules nécessaires au bon fonctionnnement de food-crops:
```
pip install --upgrade *module name*
``` 
  
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

# Trouver la mesure du prix qui correspondent aux cultures de sorghum.
fcd.findMeasurements(CommodityGroup.SORGHUM, IndicatorGroup.PRICES)
```
## Lancement du script

Pour afficher toutes les données food-crops : 
```
python FoodCropsDataset.py
```

Pour filtrer les données de food-crops selon des critères : 
```
python FoodCropsDataset.py -cg <str> -ig <str> -gl <str> -u <str>
```
- -cg
Enum CommodityGroup
- -ig 
Enum IndicatorGroup
- --gl
Localisation géographique
- --u
Unité

#### Exemple
```
python FoodCropsDataset.py -ig PRICES
python FoodCropsDataset.py -gl 'United States'
python FoodCropsDataset.py -cg SORGHUM -gl 'United States'
```
#### Remarque
Tous les paramètres sont optionnels, le script peut être lancé avec n'importe quel nombre d'argument
