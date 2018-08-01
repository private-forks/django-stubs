# Stubs for django.contrib.staticfiles.handlers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.handlers.wsgi import WSGIHandler
from typing import Any

from django.core.handlers.wsgi import WSGIRequest

class StaticFilesHandler(WSGIHandler):
    handles_files: bool = ...
    application: Any = ...
    base_url: Any = ...
    def __init__(self, application: Any) -> None: ...
    def load_middleware(self) -> None: ...
    def get_base_url(self): ...
    def _should_handle(self, path: Any): ...
    def file_path(self, url: str) -> str: ...
    def serve(self, request: Any): ...
    def get_response(self, request: WSGIRequest): ...
    def __call__(self, environ: Any, start_response: Any): ...