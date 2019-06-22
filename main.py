""" Main Module """

import json
import logging
import os
import subprocess

# pylint: disable=import-error
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

LOGGING = logging.getLogger(__name__)


class VSCodeProjectsExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(VSCodeProjectsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        items = []

        if not os.path.exists(os.path.expanduser(extension.preferences['projects_file_path'])):
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='Projects file not found',
                                    description='Please make sure you have the Project Manager VSCode extension properly installed',
                                    on_enter=HideWindowAction())
            ])

        with open(os.path.expanduser(extension.preferences['projects_file_path'])) as f:
            projects = json.load(f)

        query = event.get_argument()
        if query:
            projects = [x for x in projects if query.strip().lower()
                        in x['name'].lower()]

        for project in projects[:8]:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=project['name'],
                                             description=project['fullPath'],
                                             on_enter=ExtensionCustomAction(
                                                 project),
                                             on_alt_enter=OpenAction(project['fullPath'])))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    """ Handles item enter """

    def on_event(self, event, extension):
        """ Event handler """
        data = event.get_data()

        subprocess.call(["code", data['fullPath']])


if __name__ == '__main__':
    VSCodeProjectsExtension().run()
