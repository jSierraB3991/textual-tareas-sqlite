# Textual Tareas MongoDB


[![Textual Tareas CRUD con MongoDB](https://img.youtube.com/vi/0WohGIjuyH4/0.jpg)](https://www.youtube.com/watch?v=0WohGIjuyH4)


Aplicación TUI construida con **Textual**, **MongoDB**, **Pydantic** y arquitectura modular.  
Permite crear, editar, listar y eliminar tareas usando una interfaz de terminal moderna y dinámica.

Este repositorio también incluye una presentación interactiva creada con **reveal-md**, así como las instrucciones para generar su versión en PDF.

---

## Estrucutra de archivos y Responsabilidades

```bash
├ .env               # Configuración de entorno
├ app.py             # Punto de entrada principal
├ conky_config.conf  # Configuración del widget Conky
├ db.py              # Conexión a MongoDB
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
- MongoDB en ejecución  
- Node.js + npm (solo si deseas ver la presentación)

---

## 🚀 Instalación del proyecto

```bash
git clone https://github.com/fitorec/textual-tareas-mongodb
cd textual-tareas-mongodb
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# o en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Aplicaciones construidas con Textual

### 1. Posting

Cliente HTTP/API completo y usable desde la terminal — una suerte de “Postman en consola”. Ideal para desarrollar, probar APIs o explorar endpoints sin salir de la terminal. ([Textual Documentation][1])
**URL**: [https://posting.sh/](https://posting.sh/)

---

### 2. Dolphie

Herramienta de monitoreo y administración para bases de datos MySQL/MariaDB/ProxySQL con interfaz TUI. Perfecto para administradores DB o desarrolladores que necesitan supervisar bases en tiempo real. ([Textualize][2])
**URL (GitHub)**: [https://github.com/charles-001/dolphie](https://github.com/charles-001/dolphie)

---

### 3. Elia

Cliente de terminal para interactuar con modelos de lenguaje (LLMs / ChatGPT / similares). Útil para quien trabaja en ciencia de datos, NLP, prototipado rápido de consultas a LLMs sin salir de la terminal. ([Darren Burns][3])
**URL (GitHub)**: [https://github.com/matthiasbeyer/elia](https://github.com/matthiasbeyer/elia)

---

### 4. Harlequin

IDE de base de datos en la terminal: permite trabajar con bases SQL desde TUI, similar a herramientas gráficas pero en consola. Ideal para desarrolladores que prefieren trabajar sin salir del editor o terminal. ([GitHub][4])
**URL (GitHub)**: [https://github.com/tconbeer/harlequin](https://github.com/tconbeer/harlequin)

---

### 5. Toolong

Visualizador/manipulador de archivos de log, JSONL y otros streams de texto desde terminal con interfaz interactiva. Muy útil para desarrolladores y operaciones (DevOps) que necesitan analizar logs rápidamente desde consola. ([Textual Documentation][1])
**URL (GitHub)**: [https://github.com/anishathalye/toolong](https://github.com/anishathalye/toolong)

---

### 6. gupshup

Cliente de chat en terminal hecho con Textual — puede servir para mensajería, chat bots, o integración con servicios de mensajería desde consola. Útil para desarrolladores que crean apps de chat o integraciones desde la terminal. ([GitHub][4])
**URL (GitHub)**: [https://github.com/matthiasbeyer/gupshup](https://github.com/matthiasbeyer/gupshup)

---

### 7. kupo

Explorador de archivos en terminal, con interfaz amigable y navegación visual. Útil para quienes trabajan frecuentemente en terminal y quieren una interfaz mejor que `ls`/`cd` simples. ([GitHub][4])
**URL (GitHub)**: [https://github.com/anishathalye/kupo](https://github.com/anishathalye/kupo)

---

### 8. NoteSH

Aplicación de notas adhesivas (“sticky-notes”) en terminal, basada en Textual — ideal para productividad, tomar apuntes rápidos sin salir de la terminal. ([GitHub][5])
**URL (GitHub)**: [https://github.com/jmhobbs/notesh](https://github.com/jmhobbs/notesh)

---

### 9. textual‑paint

Editor de dibujo en terminal — “MS Paint en la consola”. Puede ser útil como experimento, demo, o base para herramientas ASCII-art, edición rápida de arte en terminal o prototipos. ([GitHub][6])
**URL (GitHub)**: [https://github.com/oleksis/textual-paint](https://github.com/oleksis/textual-paint)

---

### 10. termtyper

Aplicación de práctica de mecanografía (typing test) en terminal, construida con Textual. Buena para demos, para ver cómo Textual maneja eventos de teclado, widgets dinámicos y actualización de UI en tiempo real. ([GitHub][5])
**URL (GitHub)**: [https://github.com/oleksis/termtyper](https://github.com/oleksis/termtyper)
