from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        options = ['airDots', 'nuove']
        my_list = event.query.split(" ")

        # uncume pro lite && move up

        items.append(Enable())
        items.append(Disable())

        return RenderResultListAction(items)


def Enable():
    return ExtensionResultItem(icon='images/on.jpg',
                               name='Enable Caffeine',
                               description='',
                               on_enter=RunScriptAction("caffeine", None))


def Disable():
    return ExtensionResultItem(icon='images/off.jpg',
                               name='Disable Caffeine',
                               description='and connect to the phone',
                               on_enter=RunScriptAction("killall caffeine", None))


if __name__ == '__main__':
    GnomeSessionExtension().run()
