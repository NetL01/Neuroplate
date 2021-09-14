import gmaps
from kivy.app import App

class HelloGmaps(App):
    def build(self):
        self.map_widget = GMap()
        self.map_widget.bind(on_ready=self.create_some_markers)
        return self.map_widget

    def create_some_markers(self, map_widget):
        # get the google map interface
        sydney = map_widget.create_latlng(-33.867, 151.206)
        marker = map_widget.create_marker(
            title='Sydney',
            snippet='The most populous city in Autralia',
            position=sydney)
        map_widget.map.addMarker(marker)

if __name__ == '__main__':
    HelloGmaps().run()
