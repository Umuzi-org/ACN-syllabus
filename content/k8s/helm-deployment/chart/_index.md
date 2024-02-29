---
_db_id: 1033
content_type: project
flavours:
- none
from_repo: k8s/manual-app-deployment/project-overview
prerequisites:
  hard:
  - k8s/manual-app-deployment/project-overview
  soft:
  - k8s/helm-deployment
ready: true
submission_type: continue_repo
tags:
- kubernetes
- helm
title: Helm Chart
---

The first step to create our Helm chart is the folder structure and basic template files. We will call our application `buttons`.

On your GitHub repository, create the following folder structure and empty files:

```
├── helm
│   └── buttons
│       ├── Chart.yaml
│       ├── templates
│       │   ├── _helpers.tpl
│       └── values.yaml
```

In the `helm/buttons.Chart.yaml` file add the content below containing the chart metadata:

```yaml
apiVersion: v2

name: buttons
description: A Helm chart for the Buttons app
type: application
version: 0.1.0
appVersion: 0.1.0
```

The `helm/buttons/templates/_helpers.tpl` file will have _a lot_ of boilerplate to make our chart work. This is the default content when creating a new chart with the `helm create` command.

```yaml
{{/*
Expand the name of the chart.
*/}}
{{- define "button.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "button.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "button.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "button.labels" -}}
helm.sh/chart: {{ include "button.chart" . }}
{{ include "button.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "button.selectorLabels" -}}
app.kubernetes.io/name: {{ include "button.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "button.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "button.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
```

Using the templates like this allows us to inject the content from `values.yaml` (and from other places, like CLI parameters) into the YAML files, making it very useful for environment specific deployments like staging, UAT, QA etc.

On the `helm/buttons/values.yaml` file, add the two lines below. They indicate the credentials used by Kubernetes to pull the Docker images from Harbor. This parameter will be used later by the Deployment templates.

```yaml
imagePullSecrets:
  - name: your-regcred
```

Commit your changes to the GitHub repository. Let's do your first Helm installation.

On your EC2 instance, pull the changes:

```
# pulls the changes
cd /home/ubuntu/umuzi-k8s
git pull
```

Enter the `helm` directory and let's install our chart!
```
cd /home/ubuntu/umuzi-k8s/helm

# generates the file using the chart templates
# empty for now, since we don't have any, yet!
helm template buttons

# runs the dry-run process, showing what will be installed but doing nothing
helm install buttons buttons --dry-run --debug

# installs the helm chart
helm install buttons buttons

# lists the installed helm charts
helm list
```