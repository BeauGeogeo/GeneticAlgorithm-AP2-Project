-------------------------------
 ``algogen`` module
-------------------------------

Algorithe Génétique 
-------------------

Ceci est un algorithme génétique qui nous permettra de résoudre les quatres différents problèmes.

En voici l'algorithme : 

créer n individus aléatoirement et les ranger dans population
calculer pour chaque individu de population son degré d'adaptation
répéter g fois
   next_gen_1 = sélectionner par tournoi n/2 individus de population
   next_gen_2 = créer n/2 individus par croisements entre individus de population
   next_gen = next_gen1 + next_gen2
   faire muter chacun des individus de next_gen
   calculer pour chaque individu de next_gen son degré d'adaptation
   meilleurs = les 5 individus les mieux adaptés de population
   retirer de next_gen les 5 individus les moins bien adaptés
   population devient meilleurs + next_gen
solution = individu le mieux adapté de population

.. autoclass:: general_interface.algogen.AlgoGen
   :members:



