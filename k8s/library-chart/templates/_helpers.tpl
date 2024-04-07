{{/*
    Expand the name of the chart.
    */}}
    {{- define "library-chart.name" -}}
    {{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
    {{- end }}