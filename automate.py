import os
import shutil
from datetime import datetime, timedelta
from PIL import Image

# ----- CONFIGURACIÓN -----
TEMP_FOLDERS = ["__pycache__", "temp", "logs"]
SOURCE_FOLDER = "src"
RELEASE_FOLDER = "release"
IMAGES_FOLDER = "images"
DAYS_TO_KEEP_LOGS = 7

# ----- LIMPIAR ARCHIVOS TEMPORALES Y LOGS -----
def clean_temp_and_logs():
    print("🧹 Limpiando archivos temporales y logs antiguos...")
    now = datetime.now()
    for folder in TEMP_FOLDERS:
        if not os.path.exists(folder):
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)
                if "log" in file:
                    mtime = datetime.fromtimestamp(os.path.getmtime(path))
                    if (now - mtime) > timedelta(days=DAYS_TO_KEEP_LOGS):
                        os.remove(path)
                        print(f"  - Borrado log viejo: {path}")
                elif folder == "__pycache__" or file.endswith(".tmp"):
                    os.remove(path)
                    print(f"  - Borrado temporal: {path}")

# ----- COPIAR ARCHIVOS A RELEASE -----
def copy_to_release():
    print("📦 Copiando archivos a carpeta release...")
    if os.path.exists(RELEASE_FOLDER):
        shutil.rmtree(RELEASE_FOLDER)
    shutil.copytree(SOURCE_FOLDER, RELEASE_FOLDER)
    print(f"  - Archivos copiados a '{RELEASE_FOLDER}/'")

# ----- COMPRIMIR IMÁGENES -----
def compress_images():
    print("🖼️ Comprimiendo imágenes...")
    if not os.path.exists(IMAGES_FOLDER):
        print("  - No hay carpeta de imágenes.")
        return
    for file in os.listdir(IMAGES_FOLDER):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(IMAGES_FOLDER, file)
            img = Image.open(path)
            img.save(path, optimize=True, quality=70)
            print(f"  - Comprimida: {file}")

# ----- EJECUCIÓN -----
if __name__ == "__main__":
    clean_temp_and_logs()
    copy_to_release()
    compress_images()
    print("\n✅ Tareas completadas.")
