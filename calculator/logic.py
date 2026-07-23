def calcolatore_liquido(nico_target, totale_ml, percentuale_aroma):
    ml_aroma = (totale_ml * percentuale_aroma) / 100
    ml_nicotina = (totale_ml * nico_target) / 20
    ml_base_neutra = totale_ml - ml_aroma - ml_nicotina

    risultati = {
        "ml_aroma": ml_aroma,
        "ml_nicotina": ml_nicotina,
        "ml_base_neutra": ml_base_neutra
    }
    return risultati