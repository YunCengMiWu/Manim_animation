from manim import *


class li5(Scene):
    def construct(self):

        question = (
            Paragraph(
                "定理 (凹凸性判定定理)设f(x)在[a,b]上连续，在(a,b)内具有一阶、二阶导数，",
                "                                                                  ",
                '则   (1)若在(a,b)内f"(x)>0，则f(x)在[a,b]上的图形是凹的；',
                '     (2)若在(a,b)内f"(x)<0，则f(x)在[a,b]上的图形是凸的；',
                font="SimHei",
                gradient=(YELLOW, BLUE),
            )
            .scale(0.6)
            .to_edge(UP)
        )

        proof0 = (
            Text("证", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(question, DOWN)
            .to_edge(LEFT)
            .shift(LEFT * 0.3)
            .shift(DOWN * 0.25)
        )

        proof1 = (
            MathTex(
                r"\forall x_{1} ,x_{2}\in (a,b),x_{1} <x_{2},x_{0}=\frac{x_{1} +x_{2}}{2} ,h=x_{2} -x_{0}=x_{0} -x_{1}"
            )
            .scale(0.9)
            .next_to(question, DOWN)
        )

        # proof2 = Text(
        #     '作一阶泰勒展开，得',
        #     font = "SimHei",
        #     gradient=(YELLOW, BLUE)
        # ).scale(0.6).next_to(proof1,DOWN).to_edge(LEFT).shift(RIGHT*0.6)

        proof3 = (
            MathTex(
                r"\begin{aligned}f\left(x_{1}\right) & =f\left(x_{0}\right)+f^{\prime}\left(x_{0}\right)\left(x_{1}-x_{0}\right)+\frac{f^{\prime \prime}\left(\xi_{1}\right)}{2!}\left(x_{1}-x_{0}\right)^{2}  \\& =f\left(x_{0}\right)-f^{\prime}\left(x_{0}\right) h+\frac{f^{\prime \prime}\left(\xi_{1}\right)}{2!} h^{2} \quad\left(a<x_{1}<\xi_{1}<x_{0}<b\right)\\f\left(x_{2}\right) & =f\left(x_{0}\right)+f^{\prime}\left(x_{0}\right)\left(x_{2}-x_{0}\right)+\frac{f^{\prime \prime}\left(\xi_{2}\right)}{2!}\left(x_{2}-x_{0}\right)^{2} \\& =f\left(x_{0}\right)+f^{\prime}\left(x_{0}\right) h+\frac{f^{\prime \prime}\left(\xi_{2}\right)}{2!} h^{2}\quad\left(a<x_{0}<\xi_{2}<x_{2}<b\right)\end{aligned}"
            )
            .scale(0.9)
            .next_to(proof1, DOWN)
            .shift(RIGHT * 0.3)
        )

        proof4 = (
            Text("两式相加得 ", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(proof0, RIGHT)
            .shift(RIGHT * 0.6)
        )

        p5 = (
            MathTex(
                r"f\left(x_{1}\right)+f\left(x_{2}\right)=2 f\left(x_{0}\right)+\frac{h^{2}}{2!}\left(f^{\prime \prime}\left(\xi_{1}\right)+f^{\prime \prime}\left(\xi_{2}\right)\right)"
            )
            .scale(0.9)
            .next_to(proof4, RIGHT)
        )

        p6 = (
            Text(
                '对情形(1)，因为在(a,b)内f"(x)>0，则',
                font="SimHei",
                gradient=(YELLOW, BLUE),
            )
            .scale(0.6)
            .next_to(proof4, DOWN)
            .shift(RIGHT * 2.52)
            .shift(DOWN * 0.5)
        )

        p7 = (
            MathTex(r"f\left(x_{1}\right)+f\left(x_{2}\right)>2 f\left(x_{0}\right),")
            .scale(0.9)
            .next_to(p6, RIGHT)
        )

        p8 = (
            Text("从而", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(p6, DOWN)
            .shift(LEFT * 3.1)
            .shift(DOWN * 0.5)
        )

        p9 = (
            MathTex(
                r"f\left(\frac{x_{1}+x_{2}}{2}\right)<\frac{f\left(x_{1}\right)+f\left(x_{2}\right)}{2},"
            )
            .scale(0.9)
            .next_to(p8, RIGHT)
        )

        p10 = (
            Text("所以f(x)的图形是凹的;", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(p9, RIGHT)
        )

        p11 = (
            Text(
                '对情形(2)，因为在(a,b)内f"(x)<0，则',
                font="SimHei",
                gradient=(YELLOW, BLUE),
            )
            .scale(0.6)
            .next_to(p8, DOWN)
            .shift(DOWN * 0.5)
            .shift(RIGHT * 3.1)
        )

        p12 = (
            MathTex(r"f\left(x_{1}\right)+f\left(x_{2}\right)<2 f\left(x_{0}\right),")
            .scale(0.9)
            .next_to(p11, RIGHT)
        )

        p13 = (
            Text("从而", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(p11, DOWN)
            .shift(LEFT * 3.1)
            .shift(DOWN * 0.5)
        )

        p14 = (
            MathTex(
                r"f\left(\frac{x_{1}+x_{2}}{2}\right)>\frac{f\left(x_{1}\right)+f\left(x_{2}\right)}{2},"
            )
            .scale(0.9)
            .next_to(p13, RIGHT)
        )

        p15 = (
            Text("所以f(x)的图形是凸的;", font="SimHei", gradient=(YELLOW, BLUE))
            .scale(0.6)
            .next_to(p14, RIGHT)
        )
        # self.add(question,proof0,proof4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15)

        self.play(Write(question), run_time=5)
        self.wait(25)
        self.play(Write(VGroup(proof0, proof1)), run_time=2)
        self.wait(12)
        self.play(Write(proof3), run_time=10)
        self.wait(46)
        self.play(FadeOut(VGroup(proof1, proof3)))

        self.play(Write(VGroup(proof4, p5)), run_time=2),
        self.wait(9.5)
        pp1 = VGroup(p6, p7, p8, p9, p10)
        pp2 = VGroup(p11, p12, p13, p14, p15)
        self.play(Write(pp1), run_time=3.5)
        self.wait(18)
        self.play(Write(pp2), run_time=3.5)
        self.wait(22.5)


li5().render()
