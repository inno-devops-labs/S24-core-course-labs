{{- define "labelslib.labels" -}}
helm.sh/chart: {{ include "labelslib.chart" . }}
{{ include "labelslib.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "labelslib.selectorLabels" -}}
app.kubernetes.io/name: {{ include "labelslib.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "labelslib.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "labelslib.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}