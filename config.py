"""
Fitxer de configuració per al projecte de clustering de bàsquet FEB
"""

# Configuració de la connexió a MongoDB
MONGODB_URI = "mongodb+srv://polgarcial1305_db_user:Admin1234@cluster0.vyllvsr.mongodb.net/?appName=Cluster0"  # MongoDB Atlas
DATABASE_NAME = "feb_db"

# Vistes de la base de dades
COLLECTIONS = {
    "partits": "partits",
    "players_shots": "FEB3_players_shots",
    "players_statistics": "FEB3_players_statistics", 
    "teams_statistics": "FEB3_teams_statistics"
}

# Paràmetres del projecte
MINUTES_MINIMES = 5  # Minuts mínims per considerar un jugador
PARTITS_MINIMS = 10  # Partits mínims per considerar un jugador

# Temporades i competicions a analitzar
TEMPORADES = ["2023-2024", "2024-2025"]
COMPETICIONS = ["111"]  # ID de la LIGA EBA

# Criteris de neteja
NULL_THRESHOLD = 0.3  # Percentatge màxim de valors nuls permesos

# Ruta per guardar dades processades
DATA_PATH = "data/"
