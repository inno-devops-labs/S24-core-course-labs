{{- define "libchart.labels" -}}

{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}


{{- define "librchart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "libchart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}