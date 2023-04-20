define player = Character('我')
define hitomi = Character('Hitomi', image='hitomi')
image bg black = Color('#00000000')

transform chr_resize:
    zoom 0.4
    yoffset 200

init python:
    import requests
    def set_select(key: str) -> None:
        api_url = 'localhost'
        requests.get(f'https://{api_url}/rescuelimbo/increase?key={key}')
