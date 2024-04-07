{{- define "libchart.labels" -}}

{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}


{{- define "library-chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "libchart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}