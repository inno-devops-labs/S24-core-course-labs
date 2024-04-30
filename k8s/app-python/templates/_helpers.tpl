{{/*
Environment variables
*/}}
{{- define "app-python.env" -}}
- name: APP_TIMEZONE
  value: "Europe/Moscow"
- name: VISITS_FILE
  value: "/app/data/visits.txt"
{{- end }}