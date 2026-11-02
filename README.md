# Laboratorio ADK UCV

Mono-agente académico construido con **Google ADK**, dependencias gestionadas con **Poetry**, versionado en **GitHub** y análisis de calidad con **SonarQube/SonarCloud** mediante **GitHub Actions**.

## Requisitos
- Python 3.11 o superior (requerido por google-adk)
- Poetry, Git, cuenta GitHub y SonarCloud
- API Key de Google AI Studio

## Instalación
```bash
poetry install
cp .env.example .env   # luego editar con tu GOOGLE_API_KEY
```

## Ejecución
```bash
poetry run adk run agente_ucv
poetry run adk web --port 8000   # http://localhost:8000
```

## Herramientas (tools) del agente
| Tool | Descripción |
|------|-------------|
| `explicar_concepto(concepto)` | Explica 8 conceptos técnicos (API, algoritmo, base de datos, framework, git, docker, ci/cd, machine learning) |
| `calcular_promedio(numeros)` | Calcula el promedio de una lista de números, con validación de entrada |

## Pruebas
```bash
poetry run pytest --cov=agente_ucv --cov-report=term
```

## CI/CD
El workflow `.github/workflows/sonarqube.yml` instala dependencias, ejecuta pytest con cobertura y envía el análisis a SonarQube. Requiere el secreto `SONAR_TOKEN` en GitHub.

## Estructura
```
agente_ucv/   agente y tools
tests/        pruebas unitarias
```

Autor: César Alexander Rojas Sinche — Universidad César Vallejo
