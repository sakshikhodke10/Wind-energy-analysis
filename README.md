# Wind Energy & German Electricity-Market Data Analysis

Analysis of German electricity-market data from [SMARD](https://www.smard.de) — the
Federal Network Agency's (Bundesnetzagentur) market-data platform — with a focus on
**wind-energy generation**: comparing offshore vs. onshore output and how it varies
over time.

The project provides a small, reusable `SmartData` module for importing, cleaning,
resampling and visualising the data, together with notebooks that use it for an
end-to-end wind-energy analysis.

## Highlights

- **`SmartData` class** — imports SMARD CSV exports into pandas, cleans the data
  (low photovoltaic generation zeroed), and interpolates to a uniform 15-minute
  resolution.
- **Visualization** — line and stacked-area time plots plus KDE distribution plots,
  with figure export.
- **Wind-energy analysis** — offshore vs. onshore monthly generation (2016 vs. 2024),
  30-day rolling-mean time series, and generation distributions.
- **Test-driven** — unit tests for the data-import pipeline with `pytest`.

## Project structure

```
.
├── src/            # SmartData module + SMARD data fetcher
├── notebooks/
│   ├── 01_data_analysis.ipynb         # import, clean, interpolate
│   ├── 02_visualization.ipynb         # time & distribution plots
│   └── 03_wind_energy_analysis.ipynb  # offshore vs. onshore study
├── data/           # SMARD CSV exports
├── exports/        # generated figures
└── tests/          # pytest suite
```

## Getting started

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

Open the notebooks in `notebooks/` (run them from that folder so the relative
`../data` and `../src` paths resolve), or run the tests:

```bash
pytest
```

## Data

Data is sourced from [SMARD.de](https://www.smard.de), the German Federal Network
Agency's electricity-market data platform. Representative CSV exports are included
under `data/` so the notebooks run out of the box.

## Tech stack

Python · pandas · NumPy · matplotlib · seaborn · pytest
