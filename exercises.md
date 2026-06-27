# Exercice 1 — Analyseur de logs (dict + defaultdict + Counter + fonctions)

## Contexte

Tu travailles sur un serveur. Tu reçois une liste de logs :

```python
logs = [
    "2025-01-01 INFO user_login alice",
    "2025-01-01 ERROR database_failed",
    "2025-01-01 INFO user_login bob",
    "2025-01-02 WARNING disk_space_low",
    "2025-01-02 ERROR database_failed",
    "2025-01-02 INFO user_login alice",
]
```

## Objectifs

Créer un programme qui permet d'obtenir :

### 1. Nombre de logs par niveau

Résultat attendu :

```python
{
 "INFO": 3,
 "ERROR": 2,
 "WARNING": 1
}
```

Indice :
Utilise `Counter`.

---

### 2. Nombre d’actions par utilisateur

Résultat :

```python
{
 "alice": 2,
 "bob": 1
}
```

Indice :
Utilise `defaultdict(int)`.

---

### 3. Trouver les erreurs fréquentes

Résultat :

```python
database_failed : 2
```

---

### 4. Créer une fonction :

```python
def analyze_logs(logs):
    ...
```

qui retourne :

```python
{
 "levels": ...,
 "users": ...,
 "errors": ...
}
```

---

Bonus :

Ajouter une gestion d’erreur :

```python
try:
    ...
except:
    ...
```

si un log est mal formé.

---

# Exercice 2 — Gestion d’un réseau social (sets + dict + fonctions)

Tu as les abonnements suivants :

```python
user_A = {
    "python",
    "machine learning",
    "data science",
    "linux"
}


user_B = {
    "python",
    "cloud",
    "docker",
    "linux"
}
```

## Questions

### 1. Centres d’intérêt communs

Trouve :

```python
{
"python",
"linux"
}
```

Utilise :

```python
intersection
```

---

### 2. Centres d’intérêt uniquement chez A

Résultat :

```python
{
"machine learning",
"data science"
}
```

Utilise :

```python
difference
```

---

### 3. Tous les centres d’intérêt

Résultat :

```python
{
"python",
"machine learning",
"data science",
"linux",
"cloud",
"docker"
}
```

Utilise :

```python
union
```

---

### 4. Créer une fonction :

```python
def compare_users(user1, user2):
    return {
        "common": ...,
        "only_user1": ...,
        "all": ...
    }
```

---

Bonus :

Créer une recommandation :

Si deux utilisateurs ont plus de 2 intérêts communs :

```
"Vous devriez devenir amis"
```

---

# Exercice 3 — Gestion d’un catalogue produit (namedtuple + dict + lambda)

Tu as :

```python
products = [
    ("Laptop", 1200, "IT"),
    ("Mouse", 25, "IT"),
    ("Chair", 150, "Furniture"),
    ("Desk", 300, "Furniture")
]
```

---

## Étape 1

Transforme chaque produit en :

```python
Product(
name="Laptop",
price=1200,
category="IT"
)
```

avec :

```python
namedtuple
```

---

## Étape 2

Créer une fonction :

```python
def expensive_products(products, limit):
    ...
```

Exemple :

```python
expensive_products(products,500)
```

retourne :

```python
[
Laptop
]
```

---

## Étape 3

Trier les produits par prix :

Utilise :

```python
lambda
```

Résultat :

```python
Mouse
Chair
Desk
Laptop
```

---

## Étape 4

Créer un dictionnaire par catégorie :

Résultat :

```python
{
"IT":[
 Laptop,
 Mouse
],

"Furniture":[
 Chair,
 Desk
]
}
```

Indice :

`defaultdict(list)`

---

# Exercice 4 — Mini analyseur de texte (Counter + strings + fonctions)

Texte :

```python
text = """
Python is easy.
Python is powerful.
Python is everywhere.
"""
```

Créer une fonction :

```python
def text_analyzer(text):
    ...
```

qui retourne :

```python
{
"words": 8,
"unique_words": 6,
"most_common": "python"
}
```

---

## Étapes :

### 1. Nettoyer le texte

Transformer :

```
Python
python
```

en même mot.

Indice :

```python
lower()
```

---

### 2. Découper les mots

Indice :

```python
split()
```

---

### 3. Compter les mots

Avec :

```python
Counter
```

---

### 4. Trouver les mots uniques

Avec :

```python
set
```

---

Bonus :

Créer une compréhension :

```python
[word for word in words if len(word)>5]
```

pour trouver les mots longs.

---

# Exercice 5 — Gestionnaire de bibliothèque (dataclass + collections)

Tu dois créer un petit système de gestion d’une bibliothèque.

---

## Étape 1 — Créer une classe `Book` avec `@dataclass`

Chaque livre doit avoir :

* `title` : titre du livre
* `author` : auteur
* `category` : catégorie
* `year` : année de publication
* `available` : disponibilité (par défaut `True`)

Exemple attendu :

```python
book = Book(
    title="Clean Code",
    author="Robert Martin",
    category="Programming",
    year=2008
)

print(book)
```

Résultat :

```python
Book(
title='Clean Code',
author='Robert Martin',
category='Programming',
year=2008,
available=True
)
```

---

## Étape 2 — Ajouter des méthodes dans la dataclass

Ajoute une méthode :

```python
def borrow(self):
    ...
```

Comportement :

Si le livre est disponible :

```python
available = False
```

et retourne :

```python
"Book borrowed successfully"
```

Sinon :

```python
"Book already borrowed"
```

---

Ajoute aussi :

```python
def return_book(self):
    ...
```

qui remet :

```python
available = True
```

---

# Étape 3 — Créer une classe `Library`

Cette classe doit contenir :

```python
@dataclass
class Library:
    name: str
    books: list
```

Exemple :

```python
library = Library(
    "My Library",
    []
)
```

---

## Étape 4 — Ajouter une méthode d’ajout

Créer :

```python
def add_book(self, book):
    ...
```

Exemple :

```python
library.add_book(
    Book(
        "Python Crash Course",
        "Eric Matthes",
        "Programming",
        2019
    )
)
```

---

## Étape 5 — Rechercher des livres

Créer :

```python
def search_by_category(self, category):
    ...
```

Exemple :

```python
library.search_by_category("Programming")
```

Retour :

```python
[
Book(...),
Book(...)
]
```

---

# Étape 6 — Statistiques de la bibliothèque

Créer :

```python
def statistics(self):
    ...
```

Cette fonction doit retourner :

```python
{
    "total_books": 10,
    "available": 7,
    "borrowed": 3,
    "categories": {
        "Programming":4,
        "Science":2
    }
}
```

Indice :

Utilise :

* `Counter`
* `defaultdict`

---

# Étape 7 — Trier les livres

Créer :

```python
def sort_by_year(self):
    ...
```

Retourner les livres triés :

du plus ancien :

```python
2001
2005
2010
```

au plus récent.

Indice :

```python
sorted(
    books,
    key=lambda book: book.year
)
```

---

# Étape 8 — Bonus : validation avec `__post_init__`

Dans une dataclass, ajoute :

```python
def __post_init__(self):
    ...
```

Vérifie que :

* l'année est positive
* le titre n'est pas vide

Exemple :

```python
Book(
"",
"Martin",
"Programming",
-2000
)
```

doit lever :

```python
ValueError
```

---

# Exemple de données pour tester

```python
books = [

Book(
"Clean Code",
"Robert Martin",
"Programming",
2008
),

Book(
"Python Crash Course",
"Eric Matthes",
"Programming",
2019
),

Book(
"A Brief History of Time",
"Stephen Hawking",
"Science",
1988
),

Book(
"The Pragmatic Programmer",
"David Thomas",
"Programming",
1999
)

]
```

---

## Bonus niveau +++

Ajoute une classe :

```python
@dataclass
class User:
    name: str
    borrowed_books: list
```

Puis ajoute :

```python
def borrow_book(self, library, title):
    ...
```

Le système doit :

1. chercher le livre
2. vérifier sa disponibilité
3. le retirer de la bibliothèque
4. l’ajouter aux livres de l’utilisateur

Cet exercice est très proche de ce qu’on fait en Python professionnel : les `dataclass` servent souvent à représenter des **entités métier** (User, Product, Transaction, ModelConfig, etc.).
