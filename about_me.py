from nicegui import ui, Tailwind

ui.add_head_html('''
                 <link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />
                 <style>body {background-color: #D3D3D3; }</style>
                 ''')

@ui.page('/aboutme')
def about_me():
    # with ui.left_drawer(top_corner=True, bottom_corner=False).classes('w-1/4 bg-white'):
    with ui.card(align_items='center').classes('bg-gray-50 w-1/4 fixed-left'):
        with ui.avatar(size='14rem', color='blue-2').props('radius: 10%'):
            # ui.image('assets/Profile Pic.jpeg')
            ui.image('https://robohash.org/robot?bgset=bg2')
    
        ui.restructured_text('''Raphael **Clifton**''').classes('text-2xl')
        with ui.element('div').classes('p-2 bg-blue-100 rounded-lg'):
            ui.label('Data Engineer').classes('text-l')

        with ui.row():
            with ui.link(target='https://github.com/RaphCodec'):
                ui.icon('eva-github-outline', color='black').classes('text-2xl')
            with ui.link(target='https://www.linkedin.com/in/raphael-clifton/'):
                ui.icon('eva-linkedin-outline', color='black').classes('text-2xl')
            with ui.link(target='https://github.com/RaphCodec'):
                ui.icon('eva-email-outline ', color='black').classes('text-2xl')
    with ui.card().classes('w-3/4 fixed-right'):
        ui.markdown('''
        # About Me
        
        ## Hi. I'm Raphael Clifton, a Data Engineer with a passion for data and technology, based in New York City, New York.
                    
        ##### My primary expertise is in Python and SQL
        ##### to improve the every day fuctions of my home city
        ''')
                

