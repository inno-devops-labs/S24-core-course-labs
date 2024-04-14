{{- define "app.mySecrets" -}}
{{- if not .Values.secretData.secretName }}
- name: SECRET
    valueFrom:
    secretKeyRef:
        name: secret
        key: secret
{{- else }}
- name: SECRET
  valueFrom:
    secretKeyRef:
          name: {{ .Values.secretData.secretName }}
          key: {{ .Values.secretData.secretKey }}
{{- end }}
{{- end }}