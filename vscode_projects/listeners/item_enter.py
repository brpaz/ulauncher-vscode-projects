import os
import subprocess
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import ItemEnterEvent


class ItemEnterEventListener(EventListener):

    def on_event(self, event: ItemEnterEvent, extension: Extension):
        """ Handles the click on an item of the extension """
        data = event.get_data()

        code_executable = extension.preferences['code_executable_path']
        new_env = os.environ.copy()
        del new_env['PYTHONPATH']
        if not data['path'].startswith('vscode-remote://'):
            subprocess.run([code_executable, data['path']], env=new_env)
        else:
            subprocess.run([code_executable, '--folder-uri', data['path']], env=new_env)
