import os
import subprocess
from typing import Optional

import pkg_resources
import typer

from fastapi_cli.constants import Database, License, PackageManager, PythonVersion
from fastapi_cli.context import AppContext, ProjectContext
from fastapi_cli.generator import generate_app, generate_project
from fastapi_cli.helpers import bullet, launch_cli, yes_no

app = typer.Typer(
    add_completion=False,
    help="Managing FastAPI projects made easy!",
    name="Manage FastAPI",
)


@app.command(help="Creates a FastAPI project.")
def startproject(
    name: str,
    interactive: bool = typer.Option(False, help="Run in interactive mode."),
    database: Optional[Database] = typer.Option(None, case_sensitive=False),
    docker: bool = typer.Option(False),
    license_: Optional[License] = typer.Option(None, "--license", case_sensitive=False),
    packaging: PackageManager = typer.Option(PackageManager.PIP),
    pre_commit: bool = typer.Option(False, "--pre-commit"),
    python: PythonVersion = typer.Option(PythonVersion.THREE_DOT_EIG),
):
    if interactive:
        result = launch_cli(
            ("packaging", bullet(PackageManager)),
            ("python", bullet(PythonVersion)),
            ("license", bullet(License)),
            ("pre_commit", yes_no("pre commit")),
            ("docker", yes_no("docker")),
            ("database", bullet(Database)),
        )
        context = ProjectContext(name=name, **result)
    else:
        context = ProjectContext(
            name=name,
            packaging=packaging,
            python=python,
            license=license_,
            pre_commit=pre_commit,
            docker=docker,
            database=database,
        )
    generate_project(context)


@app.command(help="Creates a FastAPI component.")
def startapp(name: str):
    context = AppContext(name=name)
    generate_app(context)


@app.command(help="Run a FastAPI application.")
def run(prod: bool = typer.Option(False)):
    args = []
    if not prod:
        args.append("--reload")
    app_file = os.getenv("FASTAPI_APP", "app.main")
    subprocess.call(["uvicorn", f"{app_file}:app", *args])


def version_callback(value: bool):
    if value:
        version = pkg_resources.get_distribution("fastapi-cli").version
        typer.echo(f"fastapi-cli, version {version}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the Manage FastAPI version information.",
    )
):
    ...
