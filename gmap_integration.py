import gmaps
from kivy.app import App
from android.runnable import run_on_ui_thread


@run_on_ui_thread
def set_position(self, lat, lng):
    pos = self.map_widget.create_latlng(lat, lng)
    self.map_widget.map.moveCamera(
        self.map_widget.camera_update_factory.newLatLngZoom(
        pos, 13))

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

def my_func(**kwargs):
    pass


if __name__ == '__main__':
    HelloGmaps().run()
    map = GMap()
    map.execute(my_func)
