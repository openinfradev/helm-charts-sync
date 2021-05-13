# helm-charts-sync
This repository consists of a list of helm charts used by decapod and a script for syncing those charts.  
You can find the list in [charts.yml](https://github.com/openinfradev/helm-charts-sync/blob/main/charts.yml).

## CI Pipeline
The [github action](https://github.com/openinfradev/helm-charts-sync/blob/main/.github/workflows/sync.yaml) periodically syncs latest upstream charts into [helm-repo](https://github.com/openinfradev/helm-repo).
