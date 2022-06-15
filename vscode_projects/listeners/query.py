from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    def on_event(self, event: KeywordQueryEvent, extension: Extension):
        """ Handles the event """
        query = event.get_argument() or ""

        return extension.get_projects(query)
