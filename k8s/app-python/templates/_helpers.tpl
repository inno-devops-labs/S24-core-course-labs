{{/*
Environment variables
*/}}
{{- define "app-python.env" -}}
- name: APP_TIMEZONE
  value: "Europe/Paris"
- name: SOME_OTHER
  value: "value"
{{- end }}