Le projet est structuré en plusieurs fichiers, chacun ayant un rôle précis dans le fonctionnement global du programme. Cette organisation modulaire permet une meilleure lisibilité du code, facilite la maintenance et améliore la collaboration entre les membres de l’équipe.

# Structure du projet

Le projet contient les fichiers suivants :

python-execute/
│
├── main.py
├── label.py
├── analyse.py
└── README.md
-  main.py

Ce fichier constitue le point d’entrée principal du programme.

Il permet :

d’exécuter le programme principal
de coordonner les différentes fonctions
d’assurer la communication entre les modules
de lancer les traitements nécessaires

Développé par :
ANATO Elysé

-  label.py

Ce module est responsable de la gestion des labels ou de l’organisation des éléments à traiter.

Il permet :

d’assigner ou manipuler des labels
d’organiser les données selon certaines règles
de préparer les informations pour l’analyse

Développé par :
Da Sylva Fayad
Amir

-  analyse.py

Ce module est dédié à la phase d’analyse des données.

Il permet :

d’effectuer les traitements analytiques
d’interpréter les données
de produire des résultats exploitables

Développé par :
Houekpetodji Jeanne
FANOU Osé

Fonctionnement général

Le programme fonctionne selon les étapes suivantes :

Le fichier main.py est exécuté.
Les données sont préparées à l’aide du module label.py.
Les données sont ensuite analysées via analyse.py.
Les résultats sont retournés ou affichés selon le traitement effectué.
Équipe du projet

Ce projet a été réalisé par :

ANATO Elysé — Développement de main.py
Da Sylva Fayad — Développement de label.py
Amir — Développement de label.py
Houekpetodji Jeanne — Développement de analyse.py
FANOU Osé — Développement de analyse.py
