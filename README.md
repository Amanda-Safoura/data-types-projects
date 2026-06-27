# 🐍 Data Types Projects — Python Practice

Ce repository contient une série de mini-projets Python réalisés pour pratiquer les **structures de données natives Python** et les **collections avancées**.

L'objectif est de passer de la simple connaissance syntaxique à l'utilisation pratique des bonnes structures selon le problème rencontré.

Les exercices couvrent notamment :

- listes, tuples, dictionnaires
- sets et opérations ensemblistes
- `defaultdict`
- `Counter`
- `namedtuple`
- `dataclass`
- fonctions et transformations de données
- `lambda`
- comprehensions

---

## 📌 Objectif du repository

En Python, connaître une structure de données ne consiste pas seulement à savoir l'écrire :

```python
my_dict = {}
```

La vraie question est :

> Quelle structure permet de résoudre efficacement ce problème ?

Ce repo contient des exercices orientés pratique pour développer ce réflexe.

---

## 📂 Structure du projet

```
data-types-projects/
│
├── README.md
│
├── exercise_01_logs_analyzer/
│   └── logs_analyzer.py
│
├── exercise_02_social_network/
│   └── social_network.py
│
├── exercise_03_product_catalog/
│   └── product_catalog.py
│
├── exercise_04_text_analyzer/
│   └── text_analyzer.py
│
├── exercise_05_library_manager/
│   └── library_manager.py
│
└── other/
    └── how-to-remove-punctuation-and-keep-words-in string.md
```

---

## 🚀 Exercices réalisés

### 1. Analyseur de logs serveur

📁 `exercise_01_logs_analyzer`

#### Objectif

Construire un analyseur capable d'extraire des informations depuis des logs applicatifs.

#### Notions utilisées

- `dict`
- `defaultdict`
- `Counter`
- fonctions
- gestion d'erreurs

#### Fonctionnalités

Le programme permet :

- compter le nombre de logs par niveau :

Exemple :

```python
{
    "INFO": 3,
    "ERROR": 2,
    "WARNING": 1
}
```

- compter les actions des utilisateurs :

```python
{
    "alice": 2,
    "bob": 1
}
```

- identifier les erreurs fréquentes

---

### 2. Analyse d'un réseau social

📁 `exercise_02_social_network`

#### Objectif

Comparer les intérêts entre utilisateurs.

#### Notions utilisées

- sets
- union
- intersection
- différence
- dictionnaires
- fonctions

#### Fonctionnalités

Comparer deux utilisateurs :

Exemple :

```python
{
    "common": {
        "python",
        "linux"
    },
    "only_user1": {
        "machine learning"
    },
    "all": {
        "python",
        "linux",
        "cloud"
    }
}
```

---

### 3. Gestionnaire de catalogue produit

📁 `exercise_03_product_catalog`

#### Objectif

Créer une structure de données représentant des produits.

#### Notions utilisées

- `namedtuple`
- dictionnaires
- `defaultdict`
- `lambda`
- tri avec `sorted`

#### Fonctionnalités

Le programme permet :

- créer des objets produits

Exemple :

```python
Product(
    name="Laptop",
    price=1200,
    category="IT"
)
```

- filtrer les produits selon un prix
- trier les produits
- regrouper par catégorie

Résultat :

```python
{
    "IT": [
        Product(...),
        Product(...)
    ],
    "Furniture": [
        Product(...)
    ]
}
```

---

### 4. Analyseur de texte

📁 `exercise_04_text_analyzer`

#### Objectif

Analyser automatiquement un texte.

#### Notions utilisées

- strings
- `Counter`
- sets
- fonctions
- comprehensions

#### Fonctionnalités

Le programme calcule :

- nombre total de mots
- nombre de mots uniques
- mot le plus fréquent

Exemple :

```python
{
    "words": 100,
    "unique_words": 60,
    "most_common": "python"
}
```

---

### 5. Gestionnaire de bibliothèque

📁 `exercise_05_library_manager`

#### Objectif

Créer une application métier simple avec des objets Python.

#### Notions utilisées

- `dataclass`
- méthodes de classes
- `Counter`
- `defaultdict`
- listes

#### Modèles utilisés

Livre :

```python
Book(
    title="Clean Code",
    author="Robert Martin",
    category="Programming",
    year=2008
)
```

Bibliothèque :

```python
Library(
    name="My Library",
    books=[]
)
```

#### Fonctionnalités

- ajouter un livre
- emprunter un livre
- retourner un livre
- rechercher par catégorie
- statistiques globales

---

## ▶️ Installation

Cloner le repository :

```bash
git clone https://github.com/Amanda-Safoura/data-types-projects.git
```

Entrer dans le dossier :

```bash
cd data-types-projects
```

---

## 🧠 Compétences développées

À travers ces exercices :

- ✅ Choisir la bonne structure Python selon le problème
- ✅ Manipuler efficacement les collections
- ✅ Transformer et analyser des données
- ✅ Écrire des fonctions réutilisables
- ✅ Modéliser des objets métier avec `dataclass`
- ✅ Comprendre les structures utilisées en Data Engineering et ML Engineering

---

## 🔜 Prochaines améliorations possibles

Quelques extensions possibles :

- ajouter des tests avec `pytest`
- ajouter un environnement virtuel
- ajouter un package Python
- ajouter une CI GitHub Actions
- transformer certains exercices en API avec FastAPI
- connecter les exercices à des fichiers CSV/JSON
