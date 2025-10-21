import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta
import pytest
import tempfile

import automate


def test_copy_to_release(tmp_path, monkeypatch):
    # preparar estructura src
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.txt").write_text("hola")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("PYTHONPATH", str(tmp_path))  # por si
    # override constant
    automate.SOURCE_FOLDER = "src"
    automate.RELEASE_FOLDER = "release"
    automate.copy_to_release()
    assert (tmp_path / "release" / "a.txt").exists()

def test_clean_temp_and_logs(tmp_path, monkeypatch):
    # crear temp folders y logs con fechas
    monkeypatch.chdir(tmp_path)
    for f in automate.TEMP_FOLDERS:
        p = tmp_path / f
        p.mkdir()
        # archivo viejo de log
        old = p / "old.log"
        old.write_text("x")
        # set mtime a 10 días antes
        old_time = datetime.now() - timedelta(days=10)
        os.utime(old, (old_time.timestamp(), old_time.timestamp()))
        # archivo reciente
        recent = p / "recent.log"
        recent.write_text("y")
    automate.DAYS_TO_KEEP_LOGS = 7
    automate.clean_temp_and_logs()
    assert not (tmp_path / automate.TEMP_FOLDERS[0] / "old.log").exists()

def test_compress_images(tmp_path, monkeypatch):
    # crear carpeta images con jpg
    img_folder = tmp_path / "images"
    img_folder.mkdir()
    # crear una imagen válida (PIL)
    from PIL import Image
    im = Image.new("RGB", (10, 10), color="red")
    im_path = img_folder / "test.jpg"
    im.save(im_path)
    monkeypatch.chdir(tmp_path)
    automate.IMAGES_FOLDER = "images"
    automate.compress_images()
    # si llega hasta aquí sin excepción, ok
    assert im_path.exists()
