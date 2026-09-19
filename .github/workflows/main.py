import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from google import genai

kivy.require('2.0.0')

class GimiApp(App):
    def build(self):
        self.client = genai.Client(api_key="AIzaSyD8rxWed2TUnWJaiTUXR3bEe4s8u7INT74")

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.title_label = Label(text="Gimi AI Assistant", font_size='24sp', size_hint_y=0.2)
        layout.add_widget(self.title_label)

        self.response_label = Label(text="Tap button to test Gimi AI...", font_size='16sp', text_size=(300, None), size_hint_y=0.6)
        layout.add_widget(self.response_label)

        btn = Button(text="Ask Gimi", font_size='20sp', size_hint_y=0.2, background_color=(0.3, 0.7, 0.3, 1))
        btn.bind(on_press=self.ask_gimi)
        layout.add_widget(btn)

        return layout

    def ask_gimi(self, instance):
        self.response_label.text = "Gimi is thinking..."
        Clock.schedule_once(lambda dt: self.fetch_ai_response(), 0.1)

    def fetch_ai_response(self):
        try:
            res = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents='Say Hello to user!'
            )
            self.response_label.text = res.text
        except Exception as e:
            self.response_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    GimiApp().run()
  
