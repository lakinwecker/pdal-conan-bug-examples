import platform
import os
from invoke import task
from pathlib import Path
from rich.console import Console

profile = "pdalexample"
console = Console()

def invoke_run(c, task):
    c.run(task, pty=True)

@task
def conanprofile(c):
    invoke_run(c, f"conan profile new {profile} --detect")
    invoke_run(c, f"conan profile update settings.compiler.libcxx=libstdc++11 {profile}")

@task
def installdeps(c):
    invoke_run(c, f"conan install . -if build/deps/conan --build missing --profile {profile}")

@task
def cmake(c):
    invoke_run(c, f"cmake -H. -Bbuild/release -DCMAKE_MODULE_PATH=$(pwd)/build/deps/conan -DCMAKE_BUILD_TYPE=RelWithDebInfo")

@task
def cmakedebug(c):
    invoke_run(c, f"cmake -H. -Bbuild/debug -DCMAKE_MODULE_PATH=$(pwd)/build/deps/conan -DCMAKE_BUILD_TYPE=Debug")

@task
def build(c):
    import multiprocessing
    cpus = multiprocessing.cpu_count()
    invoke_run(c, f"cmake --build build/release --config Release --parallel {cpus}")

@task
def builddebug(c):
    invoke_run(c, f"cmake --build build/debug --config Debug")

@task
def clean(c):
    invoke_run(c, f"cmake --build build/release --target clean")


