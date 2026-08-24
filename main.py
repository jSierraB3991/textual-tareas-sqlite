#!/usr/bin/env python3.14
from TareaService import TareaService

def show_conky():
    tareas = TareaService.list()
    font = "DejaVu Sans Mono"
    color_date = "white"

    for t in tareas:
        sp = 30 - len(t['titulo'])
        if sp < 1:
            sp = 1
        sp = "." * sp
        print(
            f"${{color green}}{t['id']}${{color}} "
            f"${{color yellow}}{t['titulo']}${{color}}"
            f"${{color gray}}{sp}${{color}}"
        )
        sp = (" " * 30)
        print(
            f"   ${{font {font}:size=10}}{sp}"
            f"${{color {color_date}}}{t['fecha']}${{color}}${{font}}"
        )


if __name__ == "__main__":
    show_conky()
