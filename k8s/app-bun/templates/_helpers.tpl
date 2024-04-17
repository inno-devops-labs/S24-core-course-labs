{{/*
Environment variables
*/}}
{{- define "app-bun.env" -}}
- name: APP_TIMEZONE
  value: "Europe/Paris"
- name: SOME_OTHER
  value: "value"
{{- end }}