""" Main Module """

import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from vscode_projects.listeners.query import KeywordQueryEventListener
from vscode_projects.listeners.item_enter import ItemEnterEventListener
from vscode_projects.vscode import Client

LOGGING = logging.getLogger(__name__)

MAX_PROJECTS_IN_LIST = 8


class VSCodeProjectsExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(VSCodeProjectsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        self.vscode = Client()

    def get_projects(self, query: str):
        projects = self.vscode.get_projects(self.preferences)

        if query:
            projects = [
                item for item in projects
                if query.strip().lower() in item['name'].lower()
            ]

        if not projects:
            return self.show_no_results_message(query)

        items = []
        for project in projects[:MAX_PROJECTS_IN_LIST]:
            icon = 'images/icon.png'

            if project['type'] == 'workspace':
                icon = 'images/code-dark-icon.png'

            items.append(
                ExtensionResultItem(icon=icon,
                                    name=project['name'],
                                    description=project['path'],
                                    on_enter=ExtensionCustomAction(
                                        {'path': project['path']}),
                                    on_alt_enter=OpenAction(project['path'])))

        return RenderResultListAction(items)

    def show_no_results_message(self, query: str):
        """
        Helper function that renders a message saying there were not results
        """
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name='No projects found matching your query: %s' % query,
                highlightable=False,
                on_enter=HideWindowAction())
        ])
