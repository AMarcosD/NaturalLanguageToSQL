import yaml
from pathlib import Path

# Ruta al archivo schema.yml
SCHEMA_PATH = Path("sofia_health") / "models" / "staging" / "schema.yml"
OUTPUT_PATH = Path("schema_summary.txt")

def cargar_schema(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def generar_resumen(schema):
    resumen = []
    for model in schema.get("models", []):
        name = model.get("name", "Sin nombre")
        description = model.get("description", "Sin descripción")
        resumen.append(f"Tabla: {name}")
        resumen.append(f"Descripción: {description}")

        columns = model.get("columns", [])
        if columns:
            resumen.append("Columnas:")
            for col in columns:
                col_name = col.get("name", "Sin nombre")
                col_desc = col.get("description", "Sin descripción")
                resumen.append(f"     - {col_name}: {col_desc}")

                tests = col.get("tests", [])
                for test in tests:
                    if isinstance(test, dict) and "relationships" in test:
                        rel = test["relationships"]
                        resumen.append(f"Relación: {col_name} → {rel.get('to')}.{rel.get('field')}")

        resumen.append("")  #Espacio entre tablas
    return "\n".join(resumen)

def guardar_resumen(resumen, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(resumen)
    print(f"resumen guardado en: {path}")

if __name__ == "__main__":
    schema_data = cargar_schema(SCHEMA_PATH)
    resumen = generar_resumen(schema_data)
    guardar_resumen(resumen, OUTPUT_PATH)
