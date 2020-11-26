# collective-sorting

On commence par remplir une matrice de dimension N avec le caractère '0' qui représente un emplacement vide.

Ensuite on a une fonction `fill_with(number_of_objects, object_type)` qui nous sert à remplir notre matrice aléatoirement un certain nombre d'objet. Ainsi on remplit 200 objets 'A' et 200 objets 'B'. Enfin on a une fonction `fill_agent` qui place dans la matrice un certain nombre d'agent 'X' (il s'agit de leur représentation dans la matrice, les agents sont placés dans une liste.

Nous avons un scheduler qui itère sur les agents de cette liste et permet à chaque agent de se déplacer aléatoirement `I` fois et prendre et déposer des objets.

Dans l'énoncé, il est demandé :
`Une case de l’environnement ne peut contenir à la fois qu’un agent ou un objet ou être vide.`

Pour simplifier notre implémentation écrit en python, on décide qu'un agent peut se trouver sur un objet. En revanche 2 agents ne peuvent se trouver sur un même emplacement, et un agent ne peut déposer un objet sur une case ayant un objet.

`Un agent se déplace aléatoirement d’un nombre i (i>= 1) de cases, dans l’environnement dans les directions: N,S,E,O. le nombre i est un paramètre que l’on fixe selon l’étendue de l’environnement et le nombre d’agents disponibles.`

On considère qu'à chaque déplacement il peut prendre ou déposer un objet. L'agent n'effectue pas i déplacements aléatoires puis décide de prendre ou déposer un objet.

L'agent a une probabilité de prendre un objet et de déposer un objet :
Pprise= (k+ /(k+ + f))^2
Pdépôt= (f/(k-+f))^2

La probabilité Pprise n'est prise en compte seulement si l'agent est sur une case où un objet est présent et s'il n'a pas déjà d'objet dans les mains.

La probabilité Pdépôt n'est prise en compte seulement si l'agent est sur une case où il n'y a pas d'objet présent et s'il a un objet dans les mains.

On créé une fonction de décision qui nous permet d'effectuer ou non une action en fonction de ces probabilité :

```python
    def decision(self, probability):
        return random.random() < probability
```

f is an estimation of the fraction of nearby points occupied by objects of the same type.

La fonction f qui est utilisé dans les fonction de probabilité représente.

```python
def f(self, encountered_object):
    return self.get_number_of_around(encountered_object)/self.number_of_boxes()
```

q2

```python
def f_a(self):
    nb_a = self.t.count('A')
    nb_b = self.t.count('B')
    return (nb_a + nb_b * ERREUR)/len(self.t)

def f_b(self):
    nb_a = self.t.count('A')
    nb_b = self.t.count('B')
    return (nb_b + nb_a * ERREUR)/len(self.t)
```