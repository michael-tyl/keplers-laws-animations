from manim import *

class Conics(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=30,
            radius_config={"font_size": 30},
        ).add_coordinates()
        self.add(polarplane_pi)

        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=RED,
        )

        # self.play(Create(cos_func))
        # cos_func.animate.init_points()