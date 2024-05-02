{{- define "app-labels" -}}
{{- if .Chart.AppVersion -}}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end -}}
app.kubernetes.io/maintainer: "Nikolay Nechaev"
{{- end -}}
