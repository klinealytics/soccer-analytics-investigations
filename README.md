# Soccer analytics investigations

Questions about soccer tactics and player skill, investigated with free
public data. Each question has its own notebook.

## Contents

- `downloading_data.ipynb`: downloads and quality-checks the data. Finds which
  StatsBomb competitions have full 360 coverage, tests the cached loaders, and
  checks the Metrica tracking files
- `soccer_utils.py`: shared helpers for loading and caching StatsBomb events

## Data

Nothing in `data/` is included in the repo. To recreate it:

- **StatsBomb open data** is loaded with mplsoccer's `Sbopen`. The loaders in
  `soccer_utils.py` download it on first run and cache it in `data/`.
- **Metrica Sports sample data** must be cloned by hand, from the repo folder:

  ```bash
  git clone --depth 1 https://github.com/metrica-sports/sample-data.git data/metrica
  ```

  Version used: commit e706dd5 (last updated 15 Apr 2021).

## Data sources and credits

<img src="img/statsbomb-logo.png" alt="StatsBomb" width="180">

- **[StatsBomb Open Data](https://github.com/statsbomb/open-data)**: event
  and 360 data. Data provided by StatsBomb.
- **[Metrica Sports sample data](https://github.com/metrica-sports/sample-data)**:
  anonymised tracking and event data.
- **[SkillCorner Open Data](https://github.com/SkillCorner/opendata)**:
  broadcast tracking and dynamic events, 2024/25 A-League.