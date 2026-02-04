# 🏀 Projecte de Bàsquet – Clustering de Jugadors

## Introducció
En aquest projecte s’ha treballat amb dades reals de jugadors de bàsquet amb l’objectiu d’identificar **perfils de jugadors similars** mitjançant tècniques de *machine learning no supervisat*.  
A partir de les estadístiques individuals de partit, s’ha aplicat un model de *clustering* per agrupar els jugadors segons la seva manera de jugar i el seu rendiment a pista.

Aquest projecte segueix les fases típiques d’un procés de *data analysis*: ETL, modelització, visualització i interpretació de resultats.

---

## 📋 Estructura del projecte

```
📂 basquet/
├── 📓 01_ETL_EDA.ipynb
├── 📓 02_Clustering_Model.ipynb
├── 📓 03_Visualitzacio_Conclusions.ipynb
├── 📄 jugadors_processats.csv
├── 📄 jugadors_con_clusters.csv
├── 📄 cluster_profiles_resum_complet.csv
├── 📄 requirements.txt
└── ⚙️ config.py
```

---

## 🚀 Com executar el projecte

### 1. Instal·lació de les llibreries
```bash
pip install -r requirements.txt
```

### 2. Execució dels notebooks
Executar-los en aquest ordre:
1. 01_ETL_EDA.ipynb  
2. 02_Clustering_Model.ipynb  
3. 03_Visualitzacio_Conclusions.ipynb  

---

## 🎯 Resultats principals

### Clústers obtinguts

- **Clúster 0 (30,9%) – Jugadors de rol limitat**  
  Mitjanes: 2.0 punts, 0.5 assistències, 1.2 rebots  

- **Clúster 1 (69,1%) – Jugadors polivalents**  
  Mitjanes: 8.7 punts, 1.6 assistències, 4.2 rebots  

---

## 📊 Qualitat del model
- Silhouette Score: 0.296  
- Variància explicada: 71,1%  
- Balanceig: 0.45  

---

## 🏀 Aplicacions
- Anàlisi de rols
- Suport a decisions tècniques
- Scouting

---

## 📝 Conclusions
El projecte permet identificar perfils de jugadors a partir de dades reals utilitzant tècniques de clustering i seguir un flux de treball típic de data analysis.


# Alumne
Pol Garcia
