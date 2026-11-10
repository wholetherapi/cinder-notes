# Cinder Notes

Convert annotated notebooks into review-ready experiment reports.

## Release status

Released: v2.1.0 is publicly available from this repository.

## Usage

```
cinder-notes build --notebook experiments/campaign.ipynb --template data/templates.json
```

## Layout

- `src/cinder_notes.py` — notebook walker and renderer
- `data/templates.json` — report section templates
- `experiments/export_timing.md` — export timing measurements
