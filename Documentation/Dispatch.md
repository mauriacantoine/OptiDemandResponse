# Meeting, May 5th

### Notes:

On a laissé tomber les curtailable ( machine à café et washing machine)

Les data on peut etre besoin d’etre interpolé ou mises à la bonne échelle

Le travail est divisé entre:

* EV- Edo
* Thermal - Athur
* Printer - Antoine

Le modèle tournera sur une semaine du 7 au 11 avril 2019, ¼ hour résolution

On peut diviser le travail en 3 grandes parties: data; model; analysis

### Tasks:

- [x] Collecter les data et les mettre sur le main github: les données de demande (heating, electrical consumption d’un bureau), de supply( ensoleillement ) et les tarifs ( cf: sources overleaf),interpoler ou mettre à l’échelle si nécessaire,  avec un bloc jupyter spécifique
- [x] Créer pour chaque appliance une fonction qui la caractérise
- [ ] Créer la objective function
- [x] Implémenter les contraintes
- [ ] Créer une fonction qui appelle et résolve le problème (pour un petit horizon dans un premier temps)

# Meeting 09.05

Tasks:

- [ ] Antoine : faire opti sur 5 jours
- [ ] All : créer cost function pour chaque appliance
- [ ] Antoine : Créer une cost function globale + results
- [ ] Arthur : modéliser peak and base (créer array pour chaque time slot)
- [ ] Edouard : nettoyer le code pour le faire beau et uniformiser les variables si possible

  # Meeting 14.05

  Tasks:
  - [ ] Arthur : implémente la Base Peak solution + plot la température au cours de la semaine + check les paramètre de heating + check les prices for PV electricity selling 
  - [ ] Antoine:  ajouter le power threshold 
  - [ ] \

# To do in the future

* Rolling horizon
* Add PV scenario:  The PV Energy production is always directly substracted to the total energy demand. If the delta is negative, the extra quantity will be sold to the spot market (need to find the data of the prices)
* Consider the LCOE of pv for internal consumption.


