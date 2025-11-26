import os
import sys
import shutil
import subprocess
from pathlib import Path

def load_env():
    p = Path(__file__).parent / '.env'
    if p.exists():
        for line in p.read_text().splitlines():
            s = line.strip()
            if not s or s.startswith('#') or '=' not in s:
                continue
            k, v = s.split('=', 1)
            os.environ[k.strip()] = v.strip()

def main():
    os.chdir(Path(__file__).parent)
    load_env()
    if not shutil.which('node'):
        sys.stderr.write('node not found\n')
        sys.stderr.flush()
        sys.exit(1)
    cmd = ['node', str(Path('src') / 'index.js')]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
        proc.wait()
        sys.exit(proc.returncode or 0)
    except KeyboardInterrupt:
        try:
            proc.terminate()
        except Exception:
            pass
        proc.wait()
        sys.exit(proc.returncode or 0)

if __name__ == '__main__':
    main()