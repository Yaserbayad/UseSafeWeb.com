#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8").lower()


def main() -> None:
    required_files = [
        ".gitignore",
        "REPOSITORY_STRUCTURE.md",
        "website/README.md",
        "website/src/README.md",
        "website/public/README.md",
        "website/config/README.md",
        "website/tests/README.md",
        "infrastructure/README.md",
        "infrastructure/adguard-server/README.md",
        "docs/README.md",
        "tests/repository-structure/verify_structure.py",
    ]
    for relative in required_files:
        require((ROOT / relative).is_file(), f"missing canonical structure file: {relative}")

    structure = read("REPOSITORY_STRUCTURE.md")
    for phrase in [
        "/website",
        "/infrastructure/adguard-server",
        "/tests",
        "/docs",
        "plans/master",
        "current_state.md",
        "ownership",
        "generated",
        "secret",
        "no duplicate authority",
    ]:
        require(phrase in structure, f"repository structure contract missing: {phrase}")

    website = read("website/README.md")
    for phrase in [
        "typescript",
        "next.js",
        "tsk-0361",
        "no local database",
        "generated build output",
        "secrets",
    ]:
        require(phrase in website, f"website ownership contract missing: {phrase}")

    infra = read("infrastructure/adguard-server/README.md")
    for phrase in [
        "ubuntu 24.04 lts",
        "adguard",
        "tsk-0455",
        "deploy_or_recover.sh",
        "secrets outside git",
        "azure control-plane",
    ]:
        require(phrase in infra, f"adguard-server ownership contract missing: {phrase}")

    config = read("website/config/README.md")
    for phrase in ["non-secret", "runtime secret", "environment", "outside git"]:
        require(phrase in config, f"website config contract missing: {phrase}")

    docs = read("docs/README.md")
    require("non-authoritative" in docs and "plans/master" in docs, "docs must not duplicate planning authority")

    ignore = read(".gitignore")
    for pattern in [
        "node_modules/",
        ".next/",
        "coverage/",
        "dist/",
        ".env",
        "*.pem",
        "*.key",
        "*.p12",
        "*.pfx",
        "secrets/",
    ]:
        require(pattern in ignore, f".gitignore missing secret/generated exclusion: {pattern}")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    forbidden_runtime_paths = []
    for path in tracked:
        low = path.lower()
        if not (low.startswith("website/") or low.startswith("infrastructure/")):
            continue
        name = Path(low).name
        if name == ".env" or name.startswith(".env.") or low.endswith((".pem", ".key", ".p12", ".pfx")) or "/secrets/" in f"/{low}":
            forbidden_runtime_paths.append(path)
    require(not forbidden_runtime_paths, "tracked runtime secret-like paths: " + ", ".join(forbidden_runtime_paths))

    print("PASS: TSK-0454 canonical source/infrastructure/config/test/docs structure, authority boundaries, generated-file locations, and secret exclusions verified.")


if __name__ == "__main__":
    main()
