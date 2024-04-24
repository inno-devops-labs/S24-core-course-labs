{{/*
Environment variables
*/}}
{{- define "app-python.env" -}}
- name: APP_TIMEZONE
  value: "Europe/Paris"
- name: VISITS_FILE
  value: "/app/data/visits.txt"
{{- end }}