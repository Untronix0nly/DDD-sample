import logging
from typing import Callable, Type

from fastapi import FastAPI

from src.dependencies.registrator import dependencies


def register_dependencies(
    app: FastAPI, deps: dict[Type | Callable, Callable] = None
) -> None:
    if deps is None:
        deps = dependencies
    for interface, dependency in deps.items():
        app.dependency_overrides[interface] = dependency
    logging.info("\nDependencies mapping: %s", app.dependency_overrides)
