import sys
from radon.complexity import cc_visit
from radon.visitors import ComplexityVisitor
from pathlib import Path

MAX_CC = 10

def check_file(path):
    text = Path(path).read_text()
    blocks = cc_visit(text)
    bad = [b for b in blocks if b.complexity > MAX_CC]
    return bad

def main():
    bad_overall = []
    for p in Path("src").rglob("*.py"):
        bad = check_file(p)
        if bad:
            for b in bad:
                print(f"{p}:{b.lineno} {b.name} CC={b.complexity}")
            bad_overall.extend(bad)
    if bad_overall:
        print("ERROR: Complejidad ciclomática alta detectada.")
        sys.exit(1)
    print("OK: Complejidad dentro de umbrales.")
    sys.exit(0)

if __name__ == "__main__":
    main()
