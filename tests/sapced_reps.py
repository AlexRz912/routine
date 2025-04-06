import numpy as np
import matplotlib.pyplot as plt

def courbe_oubli(t, f):
    return np.exp(-t / f)

def simulate_reps(nb_reps=5, interval_base=1.5, f_init=1.0):
    """
    Simule une série de répétitions espacées.
    - nb_reps : nombre de répétitions
    - interval_base : combien de jours on attend entre chaque révision (augmente à chaque répétition)
    - f_init : facteur de mémorisation initial

    """
    f = f_init
    times = []
    rets = []
    t0 = 0  # début
    interval = 1

    for i in range(nb_reps):
        # Courbe entre deux répétitions
        t_range = np.linspace(0, interval, 100)
        t_global = t0 + t_range
        r = courbe_oubli(t_range, f)

        times.extend(t_global)
        rets.extend(r)

        # Simulation d'une révision réussie → boost de f
        f *= 1.6  # plus tu révise, plus tu retiens
        t0 += interval
        interval *= interval_base  # répétition de plus en plus espacée

    return times, rets

# Exécution
x, y = simulate_reps(nb_reps=6)

# Tracé
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Répétitions espacées")
plt.title("Simulation de la courbe de l'oubli avec répétitions")
plt.xlabel("Temps (jours)")
plt.ylabel("Taux de rétention")
plt.ylim(0, 1.05)
plt.grid(True)
plt.axhline(0.5, color='red', linestyle='--', label="Seuil critique")
plt.legend()
plt.show()

