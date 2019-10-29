# Food Crops Project
L'objectif de ce projet est de créer une API permettant de traiter et manipuler les données venant du fichier "FeedGrains.csv".
  
  
L'API s'utilise comme suit:
  ```python
  # Création d'une usine pour instancier les différents objets
  factory = FoodCropFactory()
  
  # Création de l'objet principal pour le traitement des données
  fcd = FoodCropsDataset(factory)
  # Chargement des données venant de "FeedGrains.csv"
  fcd.load("FeedGrains.csv")
  ```
