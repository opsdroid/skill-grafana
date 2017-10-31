# opsdroid skill grafana

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to notify on alerts from Grafana.

## Requirements

Grafana.

## Configuration

```yaml
skills:
  - name: grafana
    room: "#monitoring"  # (Optional) room to send alert to
```

## Usage

Configure a webhook alert in grafana which points to your opsdroid webhook.

![Webhook Config](https://cloud.githubusercontent.com/assets/1610850/22939440/96b31a8a-f2d6-11e6-9913-602ce467a4e1.png)
