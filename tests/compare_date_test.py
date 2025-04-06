from datetime import datetime, date

step = 5
# La date string que tu veux comparer
date_str = "2025-04-01"
converted_date = datetime.strptime(date_str, "%Y-%m-%d").date()

# Par exemple, la date d'aujourd'hui
today = date.today()

# Comparaison en jours
delta_days = abs((converted_date - today).days)

if delta_days < step:
    
