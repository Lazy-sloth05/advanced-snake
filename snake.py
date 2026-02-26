from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self._colors=["darkblue","gray"]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    @property
    def _colors(self):
        return self.__colors
    @_colors.setter
    def _colors(self, color_tuple):
        self.__colors = color_tuple
        if isinstance(color_tuple, tuple):
            for index, segment in enumerate(self.segments) and len(color_tuple)==2:
                self.__colors=color_tuple
                self._alternate_colors()
            else:
                raise ValueError("colors must be provided in a pair of color strings")
    def _alternate_colors(self):
        for index, segment in enumerate(self.segments):
            color_index = index % len(self.__colors)
            segment.color(self.__colors[color_index])
    