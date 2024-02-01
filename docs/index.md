# First Automated Chart

Learn how you can use Python and the Datawrapper API to create a limitless number of charts and maps.

## What you will learn

tk

## What you will need

tk

## Getting started

```
pipenv install jupyterlab pandas datawrapper
```

## Create a Datawrapper API key

tk

## Connect to Datawrapper


```python
from datawrapper import Datawrapper
```

```python
dw.get_my_account()
```

```python
{'id': 182176,
 'email': 'b@palewi.re',
 'name': 'Test user',
 'role': 'editor',
 'language': 'en-US',
 'teams': [{'id': '5TyD7GtQ',
   'name': 'Test Team',
   'url': '/v3/teams/5TyD7GtQ'},
  {'id': 'Edbuu5W-', 'name': 'Test Team 2 tun74', 'url': '/v3/teams/Edbuu5W-'},
  {'id': 'GmKk-rn5', 'name': 'Test Team', 'url': '/v3/teams/GmKk-rn5'},
  {'id': 'gRo6dmAV', 'name': 'Test Team 2 4b0vz', 'url': '/v3/teams/gRo6dmAV'},
  {'id': 'idN3ldf1', 'name': 'Test Team 2 ogm0v', 'url': '/v3/teams/idN3ldf1'},
  {'id': 'Y9EGmpwr', 'name': 'Test Team', 'url': '/v3/teams/Y9EGmpwr'}],
 'chartCount': 11488,
 'url': '/v3/users/182176',
 'entitlements': {}}
```

## Import data

```python
import pandas as pd
```

```python
df = pd.read_csv(
    "https://raw.githubusercontent.com/palewire/first-automated-chart/main/_notebooks/arrests.csv",
    parse_dates=["ArrestDateTime"]
)
```

```python
df.head()
```

## Create a chart

```python
df['year'] = df.ArrestDateTime.dt.year
```

```python
df.year.value_counts()
```

```python
totals_by_year = df.year.value_counts().sort_index().reset_index()
```

```python
chart_config = dw.create_chart(
    title="Baltimore Arrests",
    chart_type="column-chart",
    data=totals_by_year
)
```

```python
chart_config
```

```python
chart_id = chart_config["id"]
```

```python
dw.publish_chart(chart_id)
```

```python
dw.display_chart(chart_id)
```

## Set the chart description

```python
dw.update_description(
    chart_id,
    source_name="OpenBaltimore",
    source_url="https://data.baltimorecity.gov/datasets/baltimore::bpd-arrests/about",
    byline="First Automated Chart",
)
```

```python
dw.publish_chart(chart_id)
```

```python
dw.display_chart(chart_id)
```

## Style the chart

```python
metadata = {
    "visualize": {
        "base-color": "#bf7836"  # IRE's accent color
    }
}
```

```python
dw.update_chart(chart_id, metadata=metadata)
```

```python
dw.publish_chart(chart_id)
```

```python
dw.display_chart(chart_id)
```

## Create many charts

```python
df.head()
```

```python
df.District.value_counts()
```

```python
def create_chart(district: str):
    district_df = df[df.District == district]
    district_by_year = district_df.year.value_counts().sort_index().reset_index()
    chart_config = dw.create_chart(
        title=f"Arrests in Baltimore's {district} District",
        chart_type="column-chart",
        data=district_by_year,
        metadata={
            "visualize": {
                "base-color": "#113421"  # IRE's accent color
            }
        }
    )
    chart_id = chart_config["id"]
    dw.update_description(
        chart_id,
        source_name="OpenBaltimore",
        source_url="https://data.baltimorecity.gov/datasets/baltimore::bpd-arrests/about",
        byline="Ben Welsh",
    )

    dw.publish_chart(chart_id)
    return dw.display_chart(chart_id)
```

```python
create_chart("Western")
```

```python
chart_list = []
for district in df.District.dropna().unique():
    print(f"Creating chart for the {district} District")
    c = create_chart(district)
    chart_list.append(c)
```

```python
from IPython.display import display
```

```python
display(*chart_list)
```

## Create a chart that runs on a schedule

```python
from datetime import timedelta
```

```python
df.ArrestDateTime.max()
```

```python
seven_days_ago = df.ArrestDateTime.max() - timedelta(days=7)
```

```python
last_week_df = df[df.ArrestDateTime >= seven_days_ago]
```

```python
last_week_df.ChargeDescription.value_counts()
```

```python
top_charges_df = (
    last_week_df.ChargeDescription.value_counts()
        .reset_index()
        .head(10)
)
```

```python
chart_config = dw.create_chart(
    title=f"Top 10 arrest charges in Baltimore last week",
    chart_type="d3-bars",
    data=top_charges_df,
    metadata={
        "visualize": {
            "base-color": "#113421",
            "thick": True,
        },
        "describe": {
            "source-name": "OpenBaltimore",
            "source-url": "https://data.baltimorecity.gov/datasets/baltimore::bpd-arrests/about",
            "byline": "Ben Welsh"
        }
    }
)
```

```python
chart_id = chart_config["id"]
```

```python
dw.publish_chart(chart_id)
```

```python
dw.display_chart(chart_id)
```

## About this class

tk