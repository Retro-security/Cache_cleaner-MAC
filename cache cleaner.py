from kivy.config import Config
Config.set('graphics', 'resizable', False)

import subprocess
from timeout_decorator import timeout
import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (180, 300)

class cyber_sec(App):
    def build(self):
 
        layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        layout.size_hint = (1,1)
        layout.size = Window.size

        
        image = Image(source='theme.png')  
        layout.add_widget(image)
        button = Button(text='Clear cache')
        button.bind(on_press=self.on_button_click)
        button.size_hint = (1, 0.1)  
        button.size = (0, 0)
            
        layout.add_widget(button)
        return layout
    
    @timeout(4)
    def on_button_click(self, instance):
        import notification
        
        name = socket.gethostname()
        part = name.split("s-")
        username = part[0]
        command = f"rm -r /Users/{username}/Library/Caches"

        # Run the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Capture the output
        stdout, stderr = process.communicate()
        # Check if there were any errors
        if stderr:
            print("Error:", stderr.decode())
        else:
            # Print the output
            print("Output:", stdout.decode())
        
        


if __name__ == '__main__':
    cyber_sec().run()


