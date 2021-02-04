""" Main Module """

import json
import logging
import os
import subprocess
import glob
import datetime

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from memoization import cached

LOGGING = logging.getLogger(__name__)


class VSCodeProjectsExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(VSCodeProjectsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def read_workspaces(self):
        """ Reads VS Code recent workspaces """
        absPath = os.path.expanduser(self.preferences['config_path'])
        fileList = glob.glob(absPath + "/User/workspaceStorage/*/workspace.json")
        dirList = []
        for workspacePath in fileList:
            f = open(workspacePath, 'r')
            data = json.load(f)

            f.close()

            if 'folder' not in data:
                continue

            pointer = data['folder'].find('file://')
            if (pointer >= 0):
                path = data['folder'][7:]
                # get workspace name
                namePointer = path.rfind('/')
                name = path[namePointer + 1:]
                currentData = {'name': name, 'path': path}
                dirList.append(currentData)

        return dirList

    @cached(ttl=60)
    def get_projects(self):
        """ Returns projects """

        mappedProjects = []
        projects_index = []

        if self.preferences['include_project_manager'] == 'true':
            projects = []
            full_project_path = os.path.expanduser(
                self.preferences['projects_file_path'])

            if os.path.isfile(full_project_path):
                with open(full_project_path) as projects_file:
                    projects = json.load(projects_file)
            else:
                project_files = os.listdir(full_project_path)

                for projects_file in project_files:
                    projects_file = os.path.join(full_project_path,
                                                 projects_file)
                    with open(projects_file) as file:
                        projects += json.load(file)

            for project in projects:
                projects_index.append(project['name'])
                mappedProjects.append({
                    'name':
                    project['name'],
                    'path':
                    project.get('fullPath') or project.get('rootPath'),
                    'type':
                    'project',
                })

        if self.preferences['include_recent_workspaces'] == 'true':
            recent_workspaces = self.read_workspaces()
            for w in recent_workspaces:
                if w['name'] not in projects_index:
                    mappedProjects.append({
                        'name': w['name'],
                        'path': w['path'],
                        'type': 'workspace'
                    })

        # get project's time of most recent content modification
        for p in mappedProjects:
            if os.path.exists(p['path']):
                p['mtime'] = datetime.datetime.fromtimestamp(os.stat(p['path']).st_mtime)
            else:
                p['mtime'] = datetime.datetime.min

        mappedProjects.sort(reverse=True, key=lambda p: p['mtime'])

        return mappedProjects


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        items = []
        query = event.get_argument() or ""
        projects = extension.get_projects()

        if query:
            projects = [
                item for item in projects
                if query.strip().lower() in item['name'].lower()
            ]

        if not projects:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='No projects found matching your criteria',
                    highlightable=False,
                    on_enter=HideWindowAction())
            ])

        for project in projects[:8]:

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


class ItemEnterEventListener(EventListener):
    """ Handles item enter """
    def on_event(self, event, extension):
        """ Event handler """
        data = event.get_data()

        code_executable = extension.preferences['code_executable_path']
        if not data['path'].startswith('vscode-remote://'):
            subprocess.run([code_executable, data['path']])
        else:
            subprocess.run([code_executable, '--folder-uri', data['path']])


if __name__ == '__main__':
    VSCodeProjectsExtension().run()
