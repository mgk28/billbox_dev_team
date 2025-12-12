from __future__ import annotations
import os
from .cmd_tools import run_cmd

def git_status() -> str:
    return run_cmd("git status --porcelain")

def git_commit(message: str) -> str:
    run_cmd("git add -A")
    return run_cmd(f'git commit -m "{message}"')

def git_push(branch: str = "main") -> str:
    # assumes remote already configured
    return run_cmd(f"git push origin {branch}")

def ensure_gh_auth() -> str:
    # requires GITHUB_TOKEN in env, gh installed
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return "No GITHUB_TOKEN set. Skipping gh auth."
    # non-interactive login:
    return run_cmd('echo "$GITHUB_TOKEN" | gh auth login --with-token')
