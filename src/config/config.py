import configparser
import typing
import os

ConfigT = typing.TypeVar('ConfigT', bound='Config')


class Config:
    _instance = None
    _config = None

    def __new__(cls: typing.Type[ConfigT], *args, **kwargs) -> ConfigT:
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename: str):
        if self._config is None:
            if not os.path.exists(filename):
                raise FileNotFoundError(
                    f"Le fichier de configuration '{filename}' n'existe pas.")
            self.filename = filename
            self._config = configparser.ConfigParser()

    def load(self: ConfigT) -> ConfigT:
        self._config.read(self.filename, encoding='utf-8')
        return self

    def write(self: ConfigT) -> None:
        with open(self.filename, 'w', encoding='utf-8') as configfile:
            self._config.write(configfile)

    def get(self, section: str, option: str) -> str:
        if not self._config.has_section(section):
            raise ValueError(
                f"La section '{section}' n'existe pas dans le fichier de configuration.")
        if not self._config.has_option(section, option):
            raise ValueError(
                f"L'option '{option}' n'existe pas dans la section '{section}'.")
        return self._config.get(section, option)

    def set(self: ConfigT, section: str, option: str, value: str) -> ConfigT:
        if not self._config.has_section(section):
            self._config.add_section(section)
        self._config.set(section, option, value)
        return self
