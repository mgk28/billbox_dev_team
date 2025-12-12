from __future__ import annotations
import os
import shlex
import subprocess
from pathlib import Path

REPO_ROOT = Path(os.getenv("CREW_REPO_ROOT", Path.cwd())).resolve()
ALLOW_DANGEROUS = os.getenv("ALLOW_DANGEROUS_COMMANDS", "false").lower() == "true"

DENY = {"rm", "sudo", "shutdown", "reboot", "mkfs", "dd", "killall", ">", ">>"}

ALLOW_PREFIXES = [
    "python", "pip", "uv", "pytest",
    "node", "npm", "pnpm",
    "git", "gh",
    "vercel", "railway",
    "alembic",
]

def run_cmd(cmd: str, cwd: str = ".", timeout: int = 900) -> str:
    if any(tok in cmd for tok in ["&& rm", "rm -rf", "sudo "]):
        raise ValueError("Dangerous command pattern blocked.")

    parts = shlex.split(cmd)
    if not parts:
        raise ValueError("Empty command.")
    if (parts[0] in DENY) and not ALLOW_DANGEROUS:
        raise ValueError(f"Command '{parts[0]}' is denied.")

    if not any(parts[0] == p or cmd.startswith(p + " ") for p in ALLOW_PREFIXES):
        raise ValueError(f"Command '{parts[0]}' not allowed. Add to allowlist if needed.")

    workdir = (REPO_ROOT / cwd).resolve()
    if not str(workdir).startswith(str(REPO_ROOT)):
        raise ValueError("CWD outside repo root not allowed.")

    proc = subprocess.run(
        cmd,
        cwd=str(workdir),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        text=True,
        env=os.environ.copy()
    )
    return proc.stdout
