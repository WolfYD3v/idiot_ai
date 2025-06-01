#!/bin/bash

cd "$(dirname "$0")"

if [ -d "aienv" ]; then
    source aienv/bin/activate
    echo "Environnement virtuel activé."
else
    echo "Pas d'environnement virtuel 'venv' trouvé. Lancement direct du script Python."
fi

echo "Lancement de mon_bot.py..."
python3 ai.py

echo "Script Python terminé."
