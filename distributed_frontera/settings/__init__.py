# -*- coding: utf-8 -*-
from frontera.settings import BaseSettings

from distributed_frontera.settings import default_settings


class Settings(BaseSettings):
    def __init__(self, module=None, attributes=None):
        super(Settings, self).__init__(default_settings, attributes)

        if module:
            self.add_module(module)