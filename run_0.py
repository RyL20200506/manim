# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# 简陋的演示如何求解一个积分

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


class OpeningManimExample(Scene):
    def construct(self):
        example_text = TextMobject(
            r"Ry.L's first Manim practice - 2020年10月10日",
            tex_to_color_map={"Ry.L": YELLOW}
        )
        example_tex = TexMobject(
            r"\lim_{x\rightarrow\infty}(\frac{x-1}{x+1})^x=\frac{1}{e^2}",
        )
        group = VGroup(example_text, example_tex).arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait(2)

        title_2 = TextMobject("Proof:").to_corner(UP+LEFT)
        example_tex_1 = TexMobject(
            r"\begin{aligned}&\lim_{x\rightarrow\infty}(\frac{x-1}{x+1})^x\\&=\lim_{x\rightarrow\infty}e^{\ln(\frac{x-1}{x+1})^x}\\&=\lim_{x\rightarrow\infty}e^{x\ln(\frac{x-1}{x+1})}\\&=\lim_{x\rightarrow\infty}e^{\frac{\ln(x-1)-\ln(x+1)}{1/x}}\\&=\lim_{x\rightarrow\infty}e^{\frac{\frac{1}{x-1}-\frac{1}{x+1}}{-x^{-2}}}\\&=\lim_{x\rightarrow\infty}e^{\frac{-2x^2}{x^2-1}}\\&=\lim_{x\rightarrow\infty}e^{-2}\end{aligned}"
        )
        self.play(Transform(example_text, title_2),
                  LaggedStart(*map(FadeOutAndShiftDown, example_tex))
                  )
        self.play(Write(example_tex_1), run_time=5)
        self.wait(1.5)