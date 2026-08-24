from db import connection

class TareaService:
    """Capa de servicio para manipular las tareas en SQLite."""

    # ----------------------------------------------------------------------
    # LISTAR
    # ----------------------------------------------------------------------
    @classmethod
    def list(cls) -> list[dict]:
        """Devuelve todas las tareas ordenadas por ID."""
        if connection is None:
            return []
        rows = connection.execute("SELECT id, titulo, descripcion, status, fecha FROM tareas ORDER BY id").fetchall()
        return [dict(row) for row in rows]


    # ----------------------------------------------------------------------
    # NEXT ID
    # ----------------------------------------------------------------------
    @classmethod
    def next_id(cls) -> int:
        """Obtiene el siguiente ID incremental."""
        if connection is None:
            return 1
        row = connection.execute("SELECT COALESCE(MAX(id), 0) + 1 AS next_id FROM tareas").fetchone()
        return int(row["next_id"])


    # ----------------------------------------------------------------------
    # INSERTAR
    # ----------------------------------------------------------------------
    @classmethod
    def insert(cls, tarea_dict: dict) -> dict:
        """Inserta una tarea y devuelve la fila almacenada."""
        if connection is None:
            return {}

        tarea_dict["id"] = cls.next_id()
        connection.execute(
            "INSERT INTO tareas (id, titulo, descripcion, status, fecha) VALUES (?, ?, ?, ?, ?)",
            (tarea_dict["id"], tarea_dict["titulo"], tarea_dict["descripcion"], tarea_dict["status"], tarea_dict["fecha"]),
        )
        connection.commit()

        return cls.get(tarea_dict["id"]) or {}


    # ----------------------------------------------------------------------
    # OBTENER UNA TAREA
    # ----------------------------------------------------------------------
    @classmethod
    def get(cls, id_value: int) -> dict | None:
        """Obtiene una tarea por ID."""
        if connection is None:
            return None
        row = connection.execute(
            "SELECT id, titulo, descripcion, status, fecha FROM tareas WHERE id = ?",
            (id_value,),
        ).fetchone()
        return dict(row) if row else None


    # ----------------------------------------------------------------------
    # ACTUALIZAR
    # ----------------------------------------------------------------------
    @classmethod
    def update(cls, id_value: int, tarea_updates: dict) -> dict | None:
        """Actualiza una tarea por id."""
        if connection is None:
            return None

        # No permitir modificar el ID
        tarea_updates.pop("id", None)

        connection.execute(
            "UPDATE tareas SET titulo = ?, descripcion = ?, status = ?, fecha = ? WHERE id = ?",
            (tarea_updates["titulo"], tarea_updates["descripcion"], tarea_updates["status"], tarea_updates["fecha"], id_value),
        )
        connection.commit()
        return cls.get(id_value)


    # ----------------------------------------------------------------------
    # ELIMINAR
    # ----------------------------------------------------------------------
    @classmethod
    def delete(cls, id_value: int) -> bool:
        """Elimina una tarea por id."""
        if connection is None:
            return False

        result = connection.execute("DELETE FROM tareas WHERE id = ?", (id_value,))
        connection.commit()
        return result.rowcount > 0
