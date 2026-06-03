# Visual Data Analytics & Data Science Exercise Set
## plotly.express · plotly.graph_objects · Dash · seaborn · matplotlib

---

## Purpose

Build and sharpen visual analytics skills for technical interviews and portfolio projects.
Emphasis on Plotly (all three levels) + Dash interactive applications.
Seaborn/Matplotlib covered for statistical plots and publication-quality figures.

**Format:** Every exercise is build-to-spec — you receive a precise requirements list,
build the chart, then pass assertions on both the data and figure properties.
A one-sentence business interpretation follows each chart.

**Total: 77 exercises across 8 notebooks.**

---

## Full Curriculum

| # | Notebook | Level | Topics | Exercises |
|---|---|---|---|---|
| `V01` | `plotly_express_foundations` | Beginner | scatter, line, bar, histogram, box, violin, area, waterfall | 10 |
| `V02` | `plotly_express_advanced` | Beginner→Mid | facets, animations, sunburst, treemap, choropleth, parallel coords, funnel | 10 |
| `V03` | `plotly_graph_objects_foundations` | Mid | go.Scatter, go.Bar, go.Heatmap, annotations, shapes, indicators, pie, Sankey, geo | 10 |
| `V04` | `plotly_graph_objects_advanced` | Mid→Advanced | dual axes, error bars, radar, 3D scatter, contour, custom legend, PCA 3D, animated heatmap, parcats | 10 |
| `V05` | `plotly_subplots_dashboards` | Advanced | make_subplots, shared axes, mixed types, inset charts, unequal grids, geo+xy, EDA dashboard function | 10 |
| `V06` | `dash_basics` | Advanced | layout, callbacks, State, dcc.Store, DataTable, Tabs, full analytics app | 8 |
| `V07` | `seaborn_matplotlib` | Beginner→Mid | figure/axes level, regplot, residuals, pairplot, FacetGrid, clustermap, GridSpec | 8 |
| `V08` | `visual_capstone` | Advanced | Full 6-phase analytical dashboard: revenue intelligence, RFM, geo, board report, Dash app | 1 project |

---

## Exercise Format

Each exercise follows this structure:
1. **Spec** — exact requirements (chart type, colors, titles, axes, features)
2. **Starter code** — dataset pre-computed, scaffold ready
3. **Your implementation** — build to spec
4. **Assert block** — tests figure properties AND underlying data
5. **Interpretation markdown** — one sentence business insight

---

## Setup

```bash
pip install plotly dash seaborn matplotlib pandas numpy scikit-learn jupyter
jupyter notebook
```

For Dash exercises (V06, V08):
- Each app runs `app.run(jupyter_mode='inline', port=XXXX)`
- **Interrupt the kernel cell** (`■` button or `I, I` keyboard shortcut) to stop an app before running the next one
- Each exercise uses a different port (8051–8058, 8080) to avoid conflicts

---

## Recommended Order

**Week 1 — Plotly Express**
```
V01 → V02
```

**Week 2 — Graph Objects**
```
V03 → V04
```

**Week 3 — Subplots + Dash**
```
V05 → V06
```

**Week 4 — Seaborn + Capstone**
```
V07 → V08
```

---

## What Makes a Chart Pass in an Interview

Most candidates can make a chart appear. The differentiators are:

| Skill | How it's tested here |
|---|---|
| Axis control | Titles, tick formatting, range limits, log scale |
| Color semantics | Color carries meaning (growth=green, decline=red) |
| Annotations | Calling out peaks, anomalies, reference lines |
| Interactivity | Hover templates, click actions, animations |
| Layout composition | make_subplots, insets, mixed chart types |
| Business framing | Interpretation cell after every chart |
| Reusability | ChartFactory, apply_corporate_theme, eda_dashboard functions |

---

## Difficulty Map

| Notebook | Difficulty | Why |
|---|---|---|
| V01 Express Foundations | ⭐⭐ | API familiarity, one-liners mostly |
| V02 Express Advanced | ⭐⭐⭐ | Animations, hierarchical charts, go.Waterfall |
| V03 GO Foundations | ⭐⭐⭐ | Lower-level API, figure composition |
| V04 GO Advanced | ⭐⭐⭐⭐ | 3D, dual axes, animated heatmaps |
| V05 Subplots | ⭐⭐⭐⭐ | Layout management, mixed types |
| V06 Dash | ⭐⭐⭐⭐ | Callbacks, State, Store patterns |
| V07 Seaborn/mpl | ⭐⭐⭐ | Knowing when NOT to use Plotly |
| V08 Capstone | ⭐⭐⭐⭐⭐ | Full product — 6 phases, 6 callbacks |

---

## Datasets Used

All datasets load automatically via `sklearn.datasets.fetch_openml` — no manual downloads.

| Dataset | Used in | Key features |
|---|---|---|
| Online Retail (UK) | V01–V06, V08 | Transactions, dates, countries, products |
| California Housing | V01, V03–V05, V07 | Numeric features, geographic |
| German Credit | V03–V05, V07 | Mixed types, binary outcome |
| Synthetic SaaS | V02 | Segments, regions, time series |
| Synthetic OHLCV | V03, V04 | Financial time series |

---

## Assertion Philosophy

Assertions test both layers:

```python
# Layer 1: The data is correct
assert len(fig.data[0].x) == 15  # 15 bars for 15 countries

# Layer 2: The figure is configured correctly
assert fig.layout.barmode == 'group'
assert fig.data[0].marker.color == '#1565C0'
assert fig.layout.xaxis.title.text == 'Country'
```

This mirrors real interview evaluations where both correctness and quality are assessed.
