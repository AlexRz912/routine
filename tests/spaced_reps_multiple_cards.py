import numpy as np
import matplotlib.pyplot as plt
import random

def courbe_oubli(t, f):
    """ Calcule la rétention selon l'exponentielle décroissante. """
    return np.exp(-t / f)

def simulate_reps_multiple_cards(nb_reps=6, nb_cartes=5, interval_base=1.5, f_init=2.0, prob_fail=0.3):
    """
    Simule plusieurs cartes avec répétitions espacées et échec possible.
    - nb_reps : nombre de répétitions
    - nb_cartes : nombre de cartes simulées
    - interval_base : facteur d'espacement entre répétitions
    - f_init : facteur de mémorisation initial
    - prob_fail : probabilité d'échec (quand tu oublies)
    """
    cartes = {i: {'f': f_init, 't0': 0, 'interval': 1} for i in range(nb_cartes)}
    times = []
    rets = []

    for i in range(nb_reps):
        for carte_id, carte in cartes.items():
            t_range = np.linspace(0, carte['interval'], 100)
            t_global = carte['t0'] + t_range
            r = courbe_oubli(t_range, carte['f'])

            # Ajout des résultats pour cette carte
            times.extend(t_global)
            rets.extend(r)

            # Simulation d'une révision réussie ou échouée
            if random.random() < prob_fail:  # Échec si tirage aléatoire inférieur à prob_fail
                carte['f'] *= 0.8  # Diminue la rétention
                carte['interval'] = 1  # Doit réviser plus tôt
            else:
                carte['f'] *= 1.6  # Augmente légèrement la rétention
                carte['interval'] *= interval_base  # Espacement augmente

            # Mise à jour du temps de révision pour cette carte
            carte['t0'] += carte['interval']

    return times, rets

# Exécution
x, y = simulate_reps_multiple_cards(nb_reps=6, nb_cartes=3)

# Tracé
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Révisions avec succès et échec")
plt.title("Simulation de répétition espacée avec échec sur plusieurs cartes")
plt.xlabel("Temps (jours)")
plt.ylabel("Taux de rétention")
plt.ylim(0, 1.05)
plt.grid(True)
plt.axhline(0.5, color='red', linestyle='--', label="Seuil critique")
plt.legend()
plt.show()
