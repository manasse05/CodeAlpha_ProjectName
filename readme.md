CodeAlpha - Task 1 : Web Scraping

1. Présentation du projet

Dans le cadre de mon stage en Data Analytics avec CodeAlpha, j'ai réalisé cette première tâche sur le Web Scraping.

L'objectif était de récupérer automatiquement des informations disponibles sur un site Internet, de les organiser dans un tableau, puis de nettoyer les données obtenues afin de créer un dataset exploitable.

Pour réaliser ce travail, j'ai utilisé le site Books to Scrape, un site spécialement conçu pour permettre de pratiquer le Web Scraping.

Site utilisé :

https://books.toscrape.com/

---

2. Objectif de la tâche

L'objectif principal de cette tâche était de :

- récupérer des données depuis un site Internet ;
- extraire les informations qui nous intéressent ;
- parcourir plusieurs pages du site ;
- organiser les données dans un tableau ;
- nettoyer certaines données ;
- enregistrer le résultat dans un fichier CSV.

Cette tâche m'a permis de pratiquer les premières étapes d'un travail de Data Analytics, notamment la récupération et la préparation des données.

---

3. Technologies et bibliothèques utilisées

J'ai utilisé :

- Python : pour écrire le programme de scraping ;
- Requests : pour récupérer les pages du site Internet ;
- BeautifulSoup : pour rechercher et extraire les informations présentes dans le code HTML ;
- Pandas : pour organiser les données et créer le fichier CSV ;
- VS Code : comme environnement de développement.

---

4. Données récupérées

Pour chaque livre, les informations suivantes ont été récupérées :

Colonne| Description
Titre| Nom du livre
Prix_GBP| Prix du livre en livres sterling
Disponibilite| Disponibilité du livre
Note| Note du livre sur une échelle de 1 à 5

---

5. Fonctionnement du scraping

Le programme commence par accéder à la première page du site.

Ensuite, il recherche les éléments correspondant aux livres présents sur la page.

Pour chaque livre, le programme récupère :

1. son titre ;
2. son prix ;
3. sa disponibilité ;
4. sa note.

Les informations récupérées sont ensuite enregistrées dans une liste.

Le programme utilise ensuite cette liste pour créer un tableau avec Pandas.

---

6. Parcours des différentes pages

Le site contient plusieurs pages de livres.

Au lieu de récupérer uniquement la première page, j'ai ajouté une partie du programme permettant de rechercher le bouton "next".

Lorsqu'une page suivante existe, le programme récupère son adresse et continue le scraping.

Le processus continue jusqu'à ce qu'il n'y ait plus de page suivante.

Grâce à cette méthode, le programme a récupéré les données de 1 000 livres.

---

7. Nettoyage des données

Après la récupération des données, certaines informations ont été nettoyées afin d'obtenir des données plus faciles à utiliser.

Prix

Le prix était récupéré avec le symbole de la monnaie.

Le symbole "£" a donc été retiré afin de pouvoir convertir le prix en nombre.

Par exemple :

£51.77

devient :

51.77

La colonne "Prix_GBP" peut ainsi être utilisée comme une donnée numérique.

Note

La note était initialement donnée sous forme de texte par le site.

Par exemple :

One
Two
Three
Four
Five

Ces valeurs ont été transformées en nombres :

One   → 1
Two   → 2
Three → 3
Four  → 4
Five  → 5

Cela permet d'avoir une colonne "Note" plus facile à exploiter par la suite.

---

8. Création du dataset

Après le scraping et le nettoyage, les données ont été regroupées avec Pandas.

Le résultat a été enregistré dans un fichier :

dataset.csv

Le fichier contient les colonnes suivantes :

Titre
Prix_GBP
Disponibilite
Note

Le dataset final contient :

1 000 lignes de données.

---

9. Vérification du dataset

Une vérification du fichier "dataset.csv" a également été effectuée.

Les éléments suivants ont été vérifiés :

- le nombre de lignes ;
- le nombre de colonnes ;
- les noms des colonnes ;
- les valeurs manquantes ;
- les doublons ;
- les types de données ;
- un aperçu des premières lignes.

Cette vérification permet de s'assurer que le fichier obtenu est correctement structuré avant de poursuivre avec les prochaines étapes du projet.

---

10. Fichiers du projet

Le projet contient principalement les fichiers suivants :

CodeAlpha_DataAnalytics/
│
├── scraping.py
├── check_dataset.py
├── dataset.csv
├── README.md
└── venv/

Description des fichiers

scraping.py
Contient le programme Python permettant de récupérer les données du site et de créer le dataset.

check_dataset.py
Permet de vérifier la qualité et la structure du dataset obtenu.

dataset.csv
Contient les données récupérées et nettoyées.

README.md
Présente et explique le projet.

venv/
Contient l'environnement virtuel Python utilisé pour le projet.

---

11. Résultat final

Le scraping a été réalisé avec succès.

Le programme a permis de récupérer les informations de 1 000 livres à partir du site Books to Scrape.

Les données ont ensuite été nettoyées et enregistrées dans un fichier CSV.

Ce travail constitue ma première étape dans le projet de Data Analytics de CodeAlpha et m'a permis de mettre en pratique le Web Scraping avec Python.

---

12. Conclusion

Cette tâche m'a permis de comprendre les principales étapes d'un processus de Web Scraping :

Site Internet → récupération des pages → extraction des données → nettoyage → création du dataset → vérification.

J'ai également appris à utiliser les bibliothèques Python "Requests", "BeautifulSoup" et "Pandas" dans un projet concret.