# ⚡ Automatización de Tareas del Entorno de Desarrollo

👤 Autor: Juan Gabriel Pared
📚 Materia: Metodología de Sistemas II
📁 Proyecto: Automatización de tareas repetitivas y análisis de calidad de código

---

## 📝 Descripción

Este proyecto tiene como objetivo automatizar tareas repetitivas del entorno de desarrollo y mejorar la calidad del código mediante herramientas de análisis. Entre las tareas automatizadas se incluyen:

🧹 Limpieza de archivos temporales y logs antiguos.

📂 Copiado de archivos a una carpeta release.

🖼️ Compresión y optimización de imágenes.

Además, se integran herramientas para mantener y medir la calidad del código:

✅ Linting y formateo automático con hooks de pre-commit (Black, isort).

🧪 Pruebas automatizadas con pytest y cobertura de código.

📊 Análisis de complejidad ciclomática con Radon.

💀 Detección de código muerto con Vulture.

🔁 Detección de código duplicado con jscpd.

---

## 📂 Estructura del Proyecto
AUTOMATIONS
├── .github/workflows/        # CI/CD (GitHub Actions)
├── tests/                    # Tests unitarios
├── tools/                    # Scripts de análisis de calidad
├── venv/                     # Entorno virtual
├── automate.py               # Script principal de automatización
├── requirements-dev.txt      # Dependencias para desarrollo y testing
├── radon-report.txt          # Ejemplo de reporte de Radon
└── .pre-commit-config.yaml   # Configuración de pre-commit hooks

---

## 🚀 Uso

Activar el entorno virtual:

venv\Scripts\activate


Ejecutar el script de chequeo de calidad:

python tools/check_quality.py


Ejecutar tareas individuales del script automate.py según necesidad (limpieza de logs, copiado a release, compresión de imágenes).

## 🛠️ Herramientas principales

Python 3.x

Pytest, Coverage

Radon

Vulture

jscpd

Black, isort (pre-commit hooks)
