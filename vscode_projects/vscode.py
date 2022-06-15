import os
import json
import glob
import datetime
from memoization import cached
from typing import List


class Client(object):
    """ Client to interact with VS Code API"""

    @cached(ttl=60)
    def get_projects(self, preferences: dict):
        """ Returns projects """

        project_manager_projects = []
        workspace_projects = []

        names_index = []
        if preferences['include_project_manager'] == 'true':
            project_manager_projects = self.get_projects_from_project_manager(
                preferences)

            for p in project_manager_projects:
                names_index.append(p["name"])

        if preferences['include_recent_workspaces'] == 'true':
            workspace_projects = self.get_projects_from_workspaces(
                preferences, names_index)

        all_projects = project_manager_projects + workspace_projects
        return all_projects

    def get_projects_from_project_manager(self, preferences):
        mapped_projects = []
        projects = []
        full_project_path = os.path.expanduser(
            preferences['projects_file_path'])

        if os.path.isfile(full_project_path):
            with open(full_project_path) as projects_file:
                projects = json.load(projects_file)
        else:
            project_files = os.listdir(full_project_path)

            for projects_file in project_files:
                projects_file = os.path.join(full_project_path, projects_file)
                with open(projects_file) as file:
                    projects += json.load(file)

        for project in projects:
            mapped_projects.append({
                'name':
                project['name'],
                'path':
                project.get('fullPath') or project.get('rootPath'),
                'type':
                'project',
            })

        return mapped_projects

    def get_projects_from_workspaces(self, preferences: dict,
                                     exclude_list: List[str]):
        """ Reads VS Code recent workspaces """
        abs_path = os.path.expanduser(preferences['config_path'])
        file_list = glob.glob(abs_path +
                              "/User/workspaceStorage/*/workspace.json")

        recent_workspaces = []
        for workspace_file in file_list:
            f = open(workspace_file, 'r')
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

                # make sure to include only folders that still exist
                if os.path.isdir(path) and path != "/tmp":
                    currentData['mtime'] = datetime.datetime.fromtimestamp(
                        os.stat(path).st_mtime)
                    recent_workspaces.append(currentData)

        recent_workspaces.sort(reverse=True, key=lambda p: p['mtime'])
        projects = []
        for w in recent_workspaces:
            if w['name'] in exclude_list:
                continue

            projects.append({
                'name': w['name'],
                'path': w['path'],
                'type': 'workspace'
            })

        return projects
