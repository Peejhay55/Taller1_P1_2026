# Taller 1 — Proyecto Django con Bootstrap

**Autor:** Pablo José Benítez Trujillo

Proyecto web desarrollado con el framework **Django** y estilos con **Bootstrap**. Permite gestionar y reseñar películas, incluyendo carga de datos desde archivos CSV y visualización con gráficas.

---

## 📋 Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

---

## 🚀 Paso a paso para clonar y ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Peejhay55/Taller1_P1_2026.git
cd Taller1_P1_2026
```

### 2. Crear y activar un entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias con `requirements.txt`

El archivo `requirements.txt` contiene todas las librerías necesarias para que el proyecto funcione. Para instalarlas ejecuta:

```bash
pip install -r requirements.txt
```

Este comando instalará automáticamente:
- **django** — framework web principal
- **Pillow** — manejo de imágenes
- **pandas** — procesamiento de datos (CSV)
- **matplotlib** — generación de gráficas

### 4. Aplicar las migraciones de la base de datos

```bash
python manage.py migrate
```

### 5. (Opcional) Cargar datos iniciales desde el CSV

```bash
python cvs_to_json.py
python manage.py loaddata movies.json
```

### 6. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre tu navegador y ve a: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Estructura principal del proyecto

```
Taller1_P1_2026/
├── manage.py            # Utilidad de línea de comandos de Django
├── requirements.txt     # Dependencias del proyecto
├── movies_initial.csv   # Datos iniciales de películas
├── cvs_to_json.py       # Script para convertir CSV a JSON
├── movie/               # App de películas
├── moviesreview/        # Configuración principal del proyecto Django
└── news/                # App de noticias
```

---

## 🛠️ Tecnologías utilizadas

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Pillow](https://python-pillow.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
