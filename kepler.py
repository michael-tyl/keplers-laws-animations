from manim import *

factor = 1.0

class One(Scene):
    def construct(self):
        self.wait(5*factor)

        sun = Circle()
        sun.set_fill(YELLOW,opacity=0.8)
        self.play(Create(sun))
        self.wait(2*factor)
        self.play(sun.animate.scale(0.2))
        sun_label = Text("Sun",font_size=24)
        sun_label.next_to(sun,DOWN,0.2)
        self.play(Write(sun_label))
        self.wait(4*factor)


        planet = Circle(radius = 3.0, color=BLUE)
        self.play(Create(planet))

        self.wait(2*factor)
        cir_label = Text("Circular?",font_size=24)
        cir_label.next_to(planet,RIGHT,0.2)
        self.play(Write(cir_label))
        self.wait(12*factor)
        self.play(FadeOut(cir_label))

        p_ellipse = Ellipse(width=8.0, height=6.0, color=GREEN)
        p_ellipse.shift(LEFT)
        self.play(Transform(planet,p_ellipse))
        self.wait(6*factor)
        e_label = Text("Elliptical!",font_size=24)
        e_label.next_to(p_ellipse,RIGHT,0.2)
        self.play(Write(e_label))
        self.wait(7*factor)

        sun_label2 = Text("Focus",font_size=24)
        sun_label2.next_to(sun,DOWN,0.2)
        self.play(Transform(sun_label,sun_label2))
        self.wait(8*factor)

        klaw1 = Text("1. A planet revolves around the sun in an elliptical orbit\n with the sun at one focus.",
                        t2c={"elliptical orbit":RED,"sun at one focus":YELLOW},
                        line_spacing=1.5,
                        font_size=36)
        klaw1.next_to(sun,DOWN,2.0)
        self.play(Write(klaw1))

        self.wait(20)

class Diagram1(Scene):
    def construct(self):
        self.wait(5*factor)

        sun = Circle()
        sun.set_fill(YELLOW,opacity=0.8)
        self.play(Create(sun))

        self.play(sun.animate.scale(0.2))
        sun_label = Text("Sun",font_size=24)
        sun_label.next_to(sun,DOWN,0.2)
        self.play(Write(sun_label))

        p_ellipse = Ellipse(width=8.0, height=6.0, color=BLUE)
        p_ellipse.shift(RIGHT)
        self.play(Create(p_ellipse))
        self.wait(4*factor)

        maxis = Line(p_ellipse.point_from_proportion(0),p_ellipse.point_from_proportion(0.5))
        self.add(maxis)

        planet = Dot(color=BLUE)
        planet.move_to(p_ellipse.point_from_proportion(0.35))

        rline = Line(sun.get_center(),planet.get_center(),color=RED)
        fs = 28
        lplanet = Text("Planet",font_size=fs)
        lplanet.next_to(planet,UP)
        lrline = Text("r",font_size=fs,color=RED)
        lrline.next_to(rline,LEFT)
        laphe = Text("Aphelion",font_size=fs)
        laphe.next_to(p_ellipse,RIGHT)
        lperi = Text("Perihelion",font_size=fs)
        lperi.next_to(p_ellipse,LEFT)

        self.add(rline,lplanet,lrline,laphe,lperi)
        self.add(planet,sun)

class Two(Scene):
    def construct(self):
        self.wait(5*factor)

        sun = Dot(color=YELLOW,radius=0.1)
        self.play(Create(sun))
        self.wait(2*factor)

        p_ellipse = Ellipse(width=8.0, height=6.0, color=BLUE)
        p_ellipse.shift(RIGHT)
        self.play(Create(p_ellipse))
        self.wait(4*factor)

        dyn_ell = Ellipse(width=8.0,height=6.0,color=GREEN)
        dyn_ell.shift(RIGHT)

        planet = Dot().set_color(GREEN)
        self.play(p_ellipse.animate.set_color(BLUE_E))
        self.wait(5*factor)

        for i in range(11):
            self.play(MoveAlongPath(planet,dyn_ell),rate_func=rate_functions.ease_in_out_quart,run_time=2)

        gr = Group(sun,p_ellipse,planet)
        self.play(*[gr.animate.shift(LEFT*0.75),planet.animate.shift(LEFT*0.75)])
        grs = [gr]
        self.wait(6*factor)

        klaw1 = Text("2. The line joining the sun to a planet sweeps out\nequal areas in equal times.",
                        t2c={"equal areas":RED,"equal times":YELLOW},
                        t2w={"sweeps out":BOLD},
                        line_spacing=1.5,
                        font_size=36)
        self.play(Write(klaw1))
        self.wait(7*factor)

        # rad = VMobject()
        # rad.add_updater(lambda x: x.become(Line(sun,planet)))

        trace = TracedPath(planet.get_center,stroke_width=4)
        traces = [trace]

        pls = [planet]
        els = [p_ellipse]
        sus = [sun]
        trac = ValueTracker(0)
        # tras = [trac]
        # traces = [trace]
        # lis = [rad]

        for i in range(7):
            # grt = gr.copy()
            # tracker = ValueTracker(0)
            # tracker = trac.copy()
            # tras.append(tracker)
            pt = planet.copy()
            et = p_ellipse.copy()
            # pt.clear_updaters()
            pls.append(pt)
            els.append(et)
            st = sun.copy()
            sus.append(st)
            trt = TracedPath(pt.get_center,stroke_width=4)
            traces.append(trt)

            # lit = rad.copy()
            # lit.add_updater(lambda x: x.become(Line(st,pt)))
            grt = Group(et,st,pt)
            self.add(grt)
            grs.append(grt)

        
        # planet.add_updater(
        #     lambda m: m.move_to(p_ellipse.point_from_proportion(trac.get_value()))
        #     )


        hs = 0.35
        lm = [0,0,hs,hs*3,hs*3,hs,0,0]
        rm = [hs*3,hs,0,0,0,0,hs,hs*3]
        um = [0.5,0.5,0.5,0.5,0,0,0,0]
        dm = [0,0,0,0,0.5,0.5,0.5,0.5]
        fa = 4
        # for i in range(8):
        #     grcur = grs[i]
        #     self.play(grcur.animate.scale(0.3))
        #     self.play(grcur.animate.shift((LEFT*lm[i]+RIGHT*rm[i]+UP*um[i]+DOWN*dm[i])*fa))
        #     # self.play(grcur.animate.shift(RIGHT*rm[i]))
        #     # self.play(grcur.animate.shift(UP*um[i]))
        #     # self.play(grcur.animate.shift(DOWN*lm[i]))
        self.play(*[grcur.animate.scale(0.3) for grcur in grs])
        self.play(*[pcur.animate.scale(2) for pcur in pls])
        self.play(*[grs[i].animate.shift((LEFT*lm[i]+RIGHT*rm[i]+UP*um[i]+DOWN*dm[i])*fa) for i in range(len(grs))])
        # self.add(*[trt for trt in traces])

        
        for i in range(len(pls)):
            pls[i].add_updater(
                lambda m: m.move_to(els[i].point_from_proportion(trac.get_value()))
                )
        self.wait(12*factor)

        # stops = [(i+1)/len(grs) for i in range(len(grs))]
        # stops = [0.2,0.35,0.45,0.5,0.55,0.65,0.8,1]
        stops = [0.075,0.175,0.325,0.5,0.675,0.825,0.925,1]
        moves = []
        # for i in range(len(grs)):
        #     curm = MoveAlongPath(pls[i],els[i],rate_func=rate_functions.ease_in_out_cubic,run_time=8)
        #     curm.interpolate_mobject(0.125*i)
        #     moves.append(curm)
        # self.play(*moves)
        for i in range(len(grs)):
            self.add(traces[i])
            if i > 0:
                traces[i-1].clear_updaters()
            li1 = Line(sus[i],els[i].point_from_proportion(trac.get_value()))
            self.play(Create(li1))
            self.play(trac.animate.set_value(stops[i]))
            li2 = Line(sus[i],pls[i])
            self.play(Create(li2))

        self.wait(20)

class Three(Scene):
    def construct(self):
        self.wait(5*factor)

        klaw1 = Text("3. The square of the period of revolution\nof a planet is proportional to\nthe cube of the length of the major axis of its orbit.",
                        t2c={"square":RED,"period":YELLOW,"cube":RED,"major axis":YELLOW},
                        t2w={"proportional":BOLD},
                        line_spacing=1.5,
                        font_size=36)
        # klaw1.shift(DOWN*2)
        self.play(Write(klaw1))
        self.wait(10*factor)
        self.play(klaw1.animate.shift(UP*1.75))

        eq1 = MathTex(r"T^2=ka^3")
        eq2 = MathTex(r"\frac{a^3}{T^2}=k")
        vars = Text("T is the period, a is the major axis, k is a constant", font_size=24)
        eq1.next_to(klaw1,DOWN,buff=1)
        self.play(Write(eq1))
        self.wait(5*factor)
        eq2.next_to(eq1,DOWN,buff=0.3)
        self.play(Write(eq2))
        self.wait()
        vars.next_to(eq2,DOWN,buff=0.5)
        self.play(Write(vars))

        self.wait(20)