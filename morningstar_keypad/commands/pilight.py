from urllib.parse import urlencode

from commands.web import HttpRequestCommand


class PilightSwitchCommand(HttpRequestCommand):
    def __init__(self, url: str, device: str, state: str):
        command = urlencode({"device": device, "state": state})
        encoded_uri = f'{url}/control?{command}'
        super(PilightSwitchCommand, self).__init__(encoded_uri)


pilight_url = None


def use_pilight_url(url: str):
    global pilight_url
    pilight_url = url


def turn_on(device: str):
    return PilightSwitchCommand(pilight_url, device, 'on')


def turn_off(device: str):
    return PilightSwitchCommand(pilight_url, device, 'off')
