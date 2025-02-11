from nicegui import ui, Tailwind
from about_me import about_me

ui.add_head_html('''
                 <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
                 <style>body {background-color: #D3D3D3; }</style>
                 ''')


# ui.add_head_html('<style>body {background-color: #D3D3D3; }</style>')
# ui.colors(dark_page='#4e5061')
# dark = ui.dark_mode(value=True)

def my_links():
    return

# with ui.header(elevated=True).style('background-color: #01041f').classes('items-center justify-between'):
#         # ui.label('Label').classes('bg-red-400 dark:bg-blue-400')
#         ui.label('Raphael Clifton').classes('items-center justify-between')
#         ui.switch('Dark mode', on_change=dark.toggle, value=True)


about_me()

# ui.link('show page with fancy layout', page_layout)
# ui.icon('thumb_up')
# ui.markdown('This is **Markdown**.')
# ui.html('This is <strong>HTML</strong>.')
# with ui.row():
#     ui.label('CSS').style('color: #888; font-weight: bold')
#     ui.label('Tailwind').classes('font-serif')
#     ui.label('Quasar').classes('q-ml-xl')

ui.run()