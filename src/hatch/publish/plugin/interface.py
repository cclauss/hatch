from __future__ import annotations

from abc import ABC, abstractmethod


class PublisherInterface(ABC):
    """
    Example usage:

    === ":octicons-file-code-16: plugin.py"

        ```python
        from hatch.publish.plugin.interface import PublisherInterface


        class SpecialPublisher(PublisherInterface):
            PLUGIN_NAME = 'special'
            ...
        ```

    === ":octicons-file-code-16: hooks.py"

        ```python
        from hatchling.plugin import hookimpl

        from .plugin import SpecialPublisher


        @hookimpl
        def hatch_register_publisher():
            return SpecialPublisher
        ```
    """

    PLUGIN_NAME = ''
    """The name used for selection."""

    def __init__(self, app, root, cache_dir, project_config, plugin_config):
        self.__app = app
        self.__root = root
        self.__cache_dir = cache_dir
        self.__project_config = project_config
        self.__plugin_config = plugin_config

    @property
    def app(self):
        """
        An instance of [Application](../utilities.md#hatchling.bridge.app.Application).
        """
        return self.__app

    @property
    def root(self):
        """
        The root of the project tree as a path-like object.
        """
        return self.__root

    @property
    def cache_dir(self):
        """
        The directory reserved exclusively for this plugin as a path-like object.
        """
        return self.__cache_dir

    @property
    def project_config(self) -> dict:
        """
        === ":octicons-file-code-16: pyproject.toml"

            ```toml
            [tool.hatch.publish.<PLUGIN_NAME>]
            ```

        === ":octicons-file-code-16: hatch.toml"

            ```toml
            [publish.<PLUGIN_NAME>]
            ```
        """
        return self.__project_config

    @property
    def plugin_config(self) -> dict:
        """
        This is defined in Hatch's [config file](../../config/hatch.md).

        === ":octicons-file-code-16: config.toml"

            ```toml
            [publish.<PLUGIN_NAME>]
            ```
        """
        return self.__plugin_config

    @abstractmethod
    def publish(self, artifacts: list[str], options: dict):
        """
        :material-align-horizontal-left: **REQUIRED** :material-align-horizontal-right:

        This is called directly by the [`publish`](../../cli/reference.md#hatch-publish) command
        with the arguments and options it receives.
        """
