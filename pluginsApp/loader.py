import importlib
from .models import Plugin
import sys
import os

def load_active_plugins():
    plugins = []
    for plugin in Plugin.objects.filter(is_active=True):
        try:
            module = importlib.import_module(f'pluginsApp.plugins.{plugin.name}', package="plugins")
            plugin_class = getattr(module, f'{plugin.name}Plugin')
            plugin_class.name = plugin.name
            plugins.append(plugin_class())
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading plugin {plugin.name}: {e}")
    return plugins
