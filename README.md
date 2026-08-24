# Textual Tareas SQLite

[![Textual Tareas CRUD con SQLite](https://img.youtube.com/vi/0WohGIjuyH4/0.jpg)](https://www.youtube.com/watch?v=0WohGIjuyH4)

Aplicación TUI construida con **Textual**, **SQLite**, **Pydantic** y arquitectura modular.
Permite crear, editar, listar y eliminar tareas usando una interfaz de terminal moderna y dinámica.

Este repositorio también incluye una presentación interactiva creada con **reveal-md**, así como las instrucciones para generar su versión en PDF.

---

## Estrucutra de archivos y Responsabilidades

```bash
├ .env               # Configuración de entorno
├ app.py             # Punto de entrada principal
├ conky_config.conf  # Configuración del widget Conky
├ db.py              # Conexión a SQLite
├ TareaSchema.py     # sModelo de validación Pydantic
├ MainScreen.py      # Pantalla Principal
├ requirements.txt   # Dependencias del proyecto
├ style.css          # Estilos de la interfaz
├ TareaFormScreen.py # Formulario de creación/edición
└ TareaService.py    # Operaciones CRUD
```

---

## 📦 Requisitos

- Python 3.11+
- SQLite (incluido en Python)
- Node.js + npm (solo si deseas ver la presentación)

---

## 🚀 Instalación del proyecto

```bash
git clone https://github.com/fitorec/textual-tareas-sqlite
cd textual-tareas-sqlite
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# o en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Aplicaciones construidas con Textual

### 1. Posting

Cliente HTTP/API completo y usable desde la terminal — una suerte de “Postman en consola”. Ideal para desarrollar, probar APIs o explorar endpoints sin salir de la terminal.

**URL**: [https://posting.sh/](https://posting.sh/)

---

### 2. Dolphie

Herramienta de monitoreo y administración para bases de datos MySQL/MariaDB/ProxySQL con interfaz TUI. Perfecto para administradores DB o desarrolladores que necesitan supervisar bases en tiempo real.
**URL (GitHub)**: [https://github.com/charles-001/dolphie](https://github.com/charles-001/dolphie)

---

### 3. Elia

Cliente de terminal para interactuar con modelos de lenguaje (LLMs / ChatGPT / similares). Útil para quien trabaja en ciencia de datos, NLP, prototipado rápido de consultas a LLMs sin salir de la terminal.

**URL (GitHub)**: [https://github.com/darrenburns/elia](https://github.com/darrenburns/elia)

---

### 4. Harlequin

IDE de base de datos en la terminal: permite trabajar con bases SQL desde TUI, similar a herramientas gráficas pero en consola. Ideal para desarrolladores que prefieren trabajar sin salir del editor o terminal.

**URL (GitHub)**: [https://github.com/tconbeer/harlequin](https://github.com/tconbeer/harlequin)

---

### 5. Toolong

Visualizador/manipulador de archivos de log, JSONL y otros streams de texto desde terminal con interfaz interactiva. Muy útil para desarrolladores y operaciones (DevOps) que necesitan analizar logs rápidamente desde consola.

**URL (GitHub)**: [https://github.com/Textualize/toolong](https://github.com/Textualize/toolong)

---

### 6. gupshup

Cliente de chat en terminal hecho con Textual — puede servir para mensajería, chat bots, o integración con servicios de mensajería desde consola. Útil para desarrolladores que crean apps de chat o integraciones desde la terminal.

**URL (GitHub)**: [https://github.com/kraanzu/gupshup](https://github.com/kraanzu/gupshup)

---

### 7. kupo

Explorador de archivos en terminal, con interfaz amigable y navegación visual. Útil para quienes trabajan frecuentemente en terminal y quieren una interfaz mejor que `ls`/`cd` simples.

**URL (GitHub)**: [https://github.com/darrenburns/kupo](https://github.com/darrenburns/kupo)

---

### 8. Net-Textorial

Herramienta TUI para ingenieros de redes que parsea datos de dispositivos de red comparando salida CLI cruda vs estructurada. Útil para automatización de redes.

**URL**: <https://github.com/dannywade/net-textorial>

---

### 9. Trogon

Genera interfaces terminales amigables automáticamente para aplicaciones CLI basadas en Click. Perfecto para desarrollo de herramientas de línea de comandos.

**URL**: <https://github.com/Textualize/trogon>

---

### 10. termtyper

Aplicación de práctica de mecanografía (typing test) en terminal, construida con Textual. Buena para demos, para ver cómo Textual maneja eventos de teclado, widgets dinámicos y actualización de UI en tiempo real. ([GitHub][5])
**URL (GitHub)**: [https://github.com/jenniferdewan/termtyper](https://github.com/jenniferdewan/termtyper)
