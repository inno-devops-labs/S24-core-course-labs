{{- define "libchart.labels" -}}
app.kubernetes.io/name: {{ include "libchart.name" . }}
helm.sh/chart: "{{ include "libchart.chart" . }}"
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}