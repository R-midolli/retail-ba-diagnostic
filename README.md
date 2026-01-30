# 📊 Retail BA Diagnostic — Store Performance Segmentation & Opportunity Mapping

<p align="left">
  <img alt="Python"  src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="SQL"     src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img alt="Pandas"  src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img alt="Plotly"  src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img alt="DuckDB"  src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=000000" />
  <img alt="Kaggle"  src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" />
  <img alt="Git"     src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img alt="GitHub"  src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

---

## 🧭 Contexte

Ce dépôt présente un cas Business Analyst orienté retail basé sur la compétition Kaggle **Store Sales — Time Series Forecasting** (Corporación Favorita, Équateur).

Le périmètre n’est pas la prévision : l’objectif est de construire une **couche KPI magasin**, de **segmenter le réseau**, et de **décrire des écarts de performance** à partir d’indicateurs calculés sur les données.

---

## 🎯 Objectifs

- Produire une table **KPI magasin** fiable et exploitable (dataset “store_kpis”).
- Segmenter le parc magasins pour une lecture “pilotage” (profils/segments).
- Mettre en évidence des écarts **performance vs potentiel** à partir d’indicateurs calculés.
- Générer des visualisations cohérentes (libellés en français) + un **dashboard HTML**.

---

## 🗂️ Données utilisées

Le dataset Kaggle fournit notamment :

- `train.csv` : ventes journalières par magasin et famille de produits.
- `transactions.csv` : transactions journalières par magasin (proxy d’activité).
- `stores.csv` : référentiel magasins (type, cluster, localisation, etc.).

Les fichiers bruts sont attendus dans `data/raw/` (non versionnés).

---

## 🧪 Ce qui a été fait (workflow)

1. **Ingestion & préparation**
   - Chargement des fichiers Kaggle et contrôles minimaux pour fiabiliser les agrégations.

2. **ETL & couche KPI magasin**
   - Agrégation des signaux de ventes / activité au niveau magasin.
   - Sortie d’un artefact léger : `data/processed/store_kpis.csv`.

3. **Segmentation & diagnostic**
   - Segmentation du réseau magasins selon les KPI calculés.
   - Lecture descriptive des profils (comparaison entre segments, écarts observés).

4. **Visualisation & export**
   - Graphiques Plotly (libellés en français).
   - Export du dashboard : `reports/dashboard_retail.html`.

---

## 📦 Livrables

- Notebook principal : `notebooks/01_ba_case_cleaned.ipynb`
- Table KPI : `data/processed/store_kpis.csv`
- Dashboard HTML : `reports/dashboard_retail.html`
- ETL : `src/etl_pipeline.py` + `run_etl.sh`

---

## 🗺️ Structure du projet

```text
retail-ba-diagnostic/
├─ data/
│  ├─ raw/                      # Kaggle raw files (not committed)
│  └─ processed/
│     └─ store_kpis.csv          # Store KPIs (committed)
├─ notebooks/
│  ├─ 01_ba_case_cleaned.ipynb   # Main notebook
│  └─ _scratch/                  # WIP notebooks (ignored)
├─ reports/
│  ├─ dashboard_retail.html      # Exported dashboard
│  └─ figures/                   # Figures (optional)
├─ src/
│  └─ etl_pipeline.py
├─ run_etl.sh
├─ pyproject.toml
├─ uv.lock
└─ README.md
```
