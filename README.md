# Food Crops Project
L'objectif de ce projet est de créer une API permettant de traiter et manipuler les données venant du fichier "FeedGrains.csv".

## Environnement de développement
Version de python
> python 3.7

Systèmes d'exploitation
> Windows et Mac

Librairie python 
> pandas, argparse

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
python Lunch.py
```

Pour filtrer les données de food-crops selon des critères : 
```
python Lunch.py -cg <str> -ig <str> -gl <str> -u <str>
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
python Lunch.py -ig PRICES
python Lunch.py -gl 'United States'
python Lunch.py -cg SORGHUM -gl 'United States'
```
#### Remarque
Tous les paramètres sont optionnels, le script peut être lancé avec n'importe quel nombre d'argument

# Déroulement du projet 

## Répartition des tâches

![](images/gantt.png)

#### Difficultés rencontrées
La majeure partie de la difficulté venait de la compréhension du sujet, afin de bien cerner le travail demandé. Paul et Magali étant à l'aise en programmation, la partie code n'a pas vraiment posé de problème, et au contraire, ces derniers ont pu aider Jules et Julien, qui se sont concentrés sur la manière de modéliser le programme. Cette répartition des tâches découle d'un fort esprit d'équipe et d'une bonne répartition des compétences.
