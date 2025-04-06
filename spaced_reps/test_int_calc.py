from interval_calc import IntervalCalc

def test_interval_calc():
    # Cas 1 : Nouvelle carte (force initiale)
    print("----- Cas 1 : Nouvelle carte -----")
    interval_calc_new_card = IntervalCalc("2025-04-05", 19)
    print(f"Intervalle pour nouvelle succès : {interval_calc_new_card.interval} jours")
    retention_rate_new_card = interval_calc_new_card.calc_retention_rate(success=True)
    print(f"Taux de rétention après succès : {retention_rate_new_card:.4f}")
    print(f"Force après echec (nouvelle carte) : {interval_calc_new_card.force:.4f}")

    # Cas 2 : Carte avec une force établie passée en paramètre
    # print("\n----- Cas 2 : Carte avec force établie -----")
    # interval_calc_existing_card = IntervalCalc("2025-03-01", force=3.5)
    # print(f"Intervalle pour carte existante : {interval_calc_existing_card.interval} jours")
    # interval_calc_existing_card.calc_retention_rate(success=False)
    # print(f"Taux de rétention après échec : {retention_rate_existing_card:.4f}")
    # print(f"Force après échec (carte existante) : {interval_calc_existing_card.force:.4f}")

if __name__ == "__main__":
    test_interval_calc()