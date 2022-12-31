from manim import *

class Eq(Scene):
    def construct(self):
        subtitle = Text("Solving for r:", line_spacing=1).shift(4*LEFT).shift(2.5*UP)
        eq1 = MathTex(
            r"r=e(d-r\cos\theta)",
            substrings_to_isolate=["r",r"\theta"]
        )
        eq2 = MathTex(
            r"r=(ed-er\cos\theta)",
            substrings_to_isolate=["r",r"\theta"]
        )
        eq3 = MathTex(
            r"r+er\cos\theta=ed",
            substrings_to_isolate=["r",r"\theta"]
        )
        eq4 = MathTex(
            r"r(1+e\cos\theta)=ed",
            substrings_to_isolate=["r",r"\theta"]
        )
        eq5 = MathTex(
            r"r", r"=\frac{ed}{1+e\cos{\theta}}",
            # r"e^x = x^0 + x^1 +  x^2 + x^3 + \cdots +  x^n + \cdots",
            substrings_to_isolate=[r"\theta"]
        )
        eqs = [eq1,eq2,eq3,eq4,eq5]

        eq1.next_to(subtitle,DOWN,buff=1)
        eq1.shift(RIGHT)
        eq2.next_to(eq1,DOWN,buff=0.4)
        eq3.next_to(eq2,DOWN,buff=0.4)
        eq4.next_to(eq3,DOWN,buff=0.4)
        eq5.next_to(eq4,DOWN,buff=0.4)

        self.wait(5)
        self.play(Write(subtitle))

        wait_time = 3

        self.wait(wait_time)
        self.next_section()

        for i in range(0,len(eqs)):
            eq = eqs[i]
            if i != 4:
                eq.set_color_by_tex("r",YELLOW)
            else:
                eq[0].set_color(YELLOW)
            eq.set_color_by_tex(r"\theta",RED)
            if i > 0:
                prev = eqs[i-1].copy()
                prev.generate_target()
                prev.target.next_to(eqs[i-1],DOWN,buff=0.4)
                self.play(MoveToTarget(prev))
                # prev.next_to(eqs[i-1],DOWN,buff=0.4)
                # prev
                self.wait(wait_time)
                self.play(TransformMatchingTex(prev,eqs[i]))
            else:
                self.play(Write(eq))
                self.wait(wait_time)
            if i == len(eqs) - 1:
                framebox = SurroundingRectangle(eqs[i],buff=0.2)
                self.play(Create(framebox))
            self.wait()
            self.next_section()

        self.wait(20)

        
class Eq2(Scene):
    def construct(self):
        subtitle = Text("Converting to cartesian form:", line_spacing=1).shift(2*LEFT).shift(2.75*UP)
        fsize = 34
        eq1 = MathTex(
            r"r=e(d-r\cos\theta)",
            font_size=fsize
        )
        eq2 = MathTex(
            r"r^2=e^2(d-r\cos\theta)^2",
            font_size=fsize
        )
        eq2b = MathTex(
            r"\text{Recall: }r^2=x^2+y^2\\x=r\cos\theta\\y=r\sin\theta",
            font_size=fsize
        )
        eq3 = MathTex(
            r"x^2+y^2=e^2(d-x)^2",
            font_size=fsize
        )
        eq4 = MathTex(
            r"x^2+y^2=e^2(d^2-2dx+x^2)",
            font_size=fsize
        )
        eq4b = MathTex(
            r"x^2+y^2=e^2d^2-2de^2x+e^2x^2",
            font_size=fsize
        )
        eq5 = MathTex(
            r"x^2-e^2x^2+2de^2x+y^2=e^2d^2",
            font_size=fsize
        )
        eq5b = MathTex(
            r"(1-e^2)x^2+2de^2x+y^2=e^2d^2",
            font_size=fsize
        )
        eq6 = MathTex(
            r"x^2+\frac{2de^2x}{1-e^2}+\frac{y^2}{1-e^2}=\frac{e^2d^2}{1-e^2}",
            font_size=fsize
        )
        eq6b = MathTex(
            r"x^2+\frac{2de^2x}{1-e^2}+(\frac{de^2}{1-e^2})^2+\frac{y^2}{1-e^2}=\frac{e^2d^2}{1-e^2}+(\frac{de^2}{1-e^2})^2",
            font_size=fsize
        )
        eq7 = MathTex(
            r"(x+\frac{e^2d}{1-e^2})^2+\frac{y^2}{1-e^2}=\frac{(e^2d^2)(1-e^2)+d^2e^4}{(1-e^2)^2}",
            font_size=fsize
        )
        eq7b = MathTex(
            r"(x+\frac{e^2d}{1-e^2})^2+\frac{y^2}{1-e^2}=\frac{e^2d^2}{(1-e^2)^2}",
            font_size=fsize
        )
        eqs = [eq1,eq2,eq3,eq4,eq5,eq6,eq7]
        nocop = [3]

        eq1.next_to(subtitle,DOWN,buff=0.5)
        eq1.shift(RIGHT*1.5)
        for i in range(1,len(eqs)):
            eqs[i].next_to(eqs[i-1],DOWN,buff=0.3)
        eq4b.next_to(eq3,DOWN,buff=0.3)
        eq5b.next_to(eq4,DOWN,buff=0.3)
        eq6b.next_to(eq5,DOWN,buff=0.3)
        eq7b.next_to(eq6,DOWN,buff=0.3)

        self.wait(5)
        self.play(Write(subtitle))

        wait_time = 3

        self.wait(wait_time)
        self.next_section()

        for i in range(0,len(eqs)):
            eq = eqs[i]
            if i > 0:
                prev = eqs[i-1].copy()
                if i == 4:
                    prev = eq4b.copy()
                elif i == 5:
                    prev = eq5b.copy()
                elif i == 6:
                    prev = eq6b.copy()
                prev.generate_target()
                prev.target.next_to(eqs[i-1],DOWN,buff=0.3)
                self.play(MoveToTarget(prev))
                # prev.next_to(eqs[i-1],DOWN,buff=0.4)
                # prev
                self.wait(wait_time)
                self.play(TransformMatchingTex(prev,eqs[i]))
            else:
                self.play(Write(eq))
                self.wait(wait_time)
            self.wait(wait_time)
            if i == 1:
                eq2b.next_to(eq2,RIGHT,buff=1.25)
                self.play(Write(eq2b))
                self.wait(wait_time)
            elif i == 3:
                self.play(TransformMatchingTex(eq,eq4b))
            elif i == 4:
                self.play(TransformMatchingTex(eq,eq5b))
            elif i == 5:
                self.wait(5)
                self.play(TransformMatchingTex(eq,eq6b))
            elif i == 6:
                self.wait(5)
                self.play(TransformMatchingTex(eq,eq7b))
            self.next_section()
            if i == len(eqs) - 1:
                framebox = SurroundingRectangle(eqs[i],buff=0.2)
                self.play(Create(framebox))
            self.wait(wait_time)

        self.wait(20)