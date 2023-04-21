define player_name = '黎明'
define player = Character('player_name', dynamic=True)
define hitomi = Character('Hitomi', image='hitomi_catear')
image bg black = Color('#000000ff')
image overlay black = Color('#000000ff')
image overlay dark = Color('#000000bb')

transform chr_display:
    yoffset 200

init python:
    def set_select(key: str):
        if renpy.emscripten():
            return
        if not requests:
            import requests
        api_url = 'localhost'
        requests.get(f'https://{api_url}/rescuelimbo/increase?key={key}')

    def fullscreen():
        if renpy.emscripten:
            renpy.emscripten.run_script('document.body.requestFullscreen()')
