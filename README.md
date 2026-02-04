# 🏀 Projecte de Bàsquet - Clustering de Jugadors

## Què hem fet?
Aquest projecte analitza dades de jugadors de bàsquet per trobar grups similars. Hem usat machine learning per classificar els jugadors segons com juguen.

## 📋 Estructura
```
📂 basquet/
├── 📓 01_ETL_EDA.ipynb          # Part 1: Neteja i anàlisi de dades
├── 📓 02_Clustering_Model.ipynb   # Part 2: Model de clustering
├── 📓 03_Visualitzacio_Conclusions.ipynb  # Part 3: Gràfics i conclusions
├── 📄 jugadors_processats.csv   # Dades netejades
├── 📄 jugadors_con_clusters.csv # Dades amb grups assignats
├── 📄 cluster_profiles_resum_complet.csv  # Resum dels grups
├── 📄 requirements.txt          # Llibreries necessàries
└── ⚙️ config.py                # Configuració
```

## 🚀 Com executar-ho

### 1. Instal·lar les llibreries
```bash
pip install -r requirements.txt
```

### 2. Executar els notebooks (en ordre!)
1. `01_ETL_EDA.ipynb` - Neteja les dades
2. `02_Clustering_Model.ipynb` - Crea els grups
3. `03_Visualitzacio_Conclusions.ipynb` - Mostra resultats

## 🎯 Resultats principals

### Grups trobats:
- **Grup 0 (30.9%)**: Jugadors de rol limitat
  - Juguen pocs minuts, fan poques coses
  - Mitjana: 2.0 punts, 0.5 assistències, 1.2 rebots

- **Grup 1 (69.1%)**: Jugadors polivalents
  - Juguen bé i fan de tot
  - Mitjana: 8.7 punts, 1.6 assistències, 4.2 rebots

### 📊 Mètriques del model:
- **Silhouette Score**: 0.296 (està bé)
- **Variància explicada**: 71.1% (molt bé)
- **Balanceig**: 0.45 (raonable)

## 🏀 Per a què serveix?
- **Per a equips**: Sabre quins tipus de jugadors necessites
- **Per a entrenadors**: Dissenar estratègies segons els jugadors
- **Per a scouts**: Trobar jugadors similars als que busques

## 👨‍💻 Autor
Projecte fet per a l'assignatura de Sistemes d'Aprenentatge Automàtic
Institut Sa Palomera - Curs 2025-2026

---
*Nota: Les visualitzacions es generen quan s'executen els notebooks*
