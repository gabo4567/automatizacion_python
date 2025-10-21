import subprocess
import sys

# --- Configuración de umbrales ---
COVERAGE_MIN = 0.8        # 80%
RADON_CC_MAX = 10         # complejidad máxima por función
VULTURE_MAX_CONF = 50     # solo reportar código muerto con >50% confianza
JSCPD_MIN_TOKENS = 50     # tokens mínimos para considerar duplicación

# --- Ejecutar pytest con cobertura ---
print("🧪 Ejecutando tests y cobertura...")
try:
    result = subprocess.run(
        ["pytest", "--cov=.", "--cov-report=term"],
        check=True,
        text=True,
        capture_output=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(e.stdout)
    print(e.stderr)
    print("❌ Tests fallaron o cobertura no alcanzada.")
    sys.exit(1)

# --- Ejecutar Radon (complejidad ciclomática) ---
print("\n📊 Analizando complejidad con Radon...")
try:
    result = subprocess.run(
        ["radon", "cc", "-s", "-a", "automate.py"],
        check=True,
        text=True,
        capture_output=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("❌ Error ejecutando Radon")
    sys.exit(1)

# --- Ejecutar Vulture (código muerto) ---
print("\n💀 Buscando código muerto con Vulture...")
try:
    result = subprocess.run(
        ["vulture", "automate.py", "--min-confidence", str(VULTURE_MAX_CONF)],
        check=False,
        text=True,
        capture_output=True
    )
    if result.stdout.strip():
        print("⚠️ Código muerto encontrado:")
        print(result.stdout)
    else:
        print("✅ No se encontraron problemas graves de código muerto.")
except Exception as e:
    print(f"❌ Error ejecutando Vulture: {e}")
    sys.exit(1)

# --- Ejecutar jscpd (duplicación de código) ---
print("\n🔁 Detectando código duplicado con jscpd...")
try:
    # excluimos venv y otras carpetas irrelevantes
    result = subprocess.run(
        [
            r"C:\Users\gabri\AppData\Roaming\npm\jscpd.cmd",
            "--min-tokens", str(JSCPD_MIN_TOKENS),
            ".", 
            "--exclude", "venv/**", 
            "--exclude", ".git/**"
        ],
        check=False,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace"
    )
    output = result.stdout or ""
    if "duplicates found" in output.lower() or "clones found" in output.lower():
        print("⚠️ Código duplicado detectado:")
        print(output)
    else:
        print("✅ No se encontraron duplicaciones relevantes.")
except Exception as e:
    print(f"❌ Error ejecutando jscpd: {e}")
    sys.exit(1)

print("\n🎯 Chequeo de calidad completado.")
