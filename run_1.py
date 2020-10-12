# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# 黎曼球面和球极射影

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


# python -m manim run_1.py OpeningManimExample -pl
class OpeningManimExample(Scene):
    # 二维画面下的球极摄影
    def construct(self):
        # cube = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)

        grid = NumberPlane()
        axis = Axes()
        self.add(axis, grid)  # Make sure title is on top of grid
        self.play(
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        # self.wait()

        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: np.array([
                (2/(np.linalg.norm(p))) * p[0],
                (2/(np.linalg.norm(p))) * p[1],
                -(2/(np.linalg.norm(p))) + 1]),
            run_time=3,
        )
        self.wait(3)



