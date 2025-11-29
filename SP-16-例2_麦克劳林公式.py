# -*- coding: utf-8 -*-
from manim import *


class SP_16(Scene):
    def construct(self):  # 所有动画内容都在 construct() 方法中定义
        # ----------------------------------------------------------
        # 1. LOGO：椭圆+作者署名
        # ----------------------------------------------------------
        ellipse = Ellipse(
            width=0.8, height=0.4, color=BLUE, fill_opacity=1, stroke_width=3
        )
        colors_ = [BLUE_B, PURPLE, GREEN, GOLD]
        ellipse.set_color(color_gradient(colors_, 100))  # 渐变色填充
        ellipse.to_corner(UR, buff=0.21)  # 右上角

        text = Text("CQU", font="Dancing Script", weight="BOLD", font_size=24)
        text.set_color(BLACK)
        text.to_corner(UR, buff=0.3)
        self.add(ellipse, text)  # 直接添加，不做动画

        # 题目 - 修正了缺少的"n"
        txt1 = Text("例 ", font="STKaiti", font_size=34, weight="BOLD")
        txt2 = Text("求 ", font="STKaiti", font_size=30)
        txt3 = MathTex(r"f(x) = \sin x", font_size=30)
        txt4 = Text("的带有拉格朗日余项的n阶麦克劳林公式 .", font_size=26)
        group = (
            VGroup(txt1, txt2, txt3, txt4)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .to_corner(UL, buff=0.5)  # 左上角，与角落边缘距离0.5个单位
        )

        txt5 = Text(
            "解", font="STKaiti", font_size=30, weight="BOLD", color=BLUE
        ).next_to(group, DOWN, aligned_edge=LEFT, buff=0.4)

        # 修正了这里的错误：\f 改为 f
        txt6 = MathTex(
            r"\because f^{(n)}(x) = \sin\left(x + \frac{n\pi}{2}\right), \, \ f^{(n)}(0) = \sin\left(\frac{n\pi}{2}\right), \,",
            color=(BLUE, GREEN),
            font_size=30,
        ).next_to(
            txt5, RIGHT, buff=0.25
        )  # ∵……

        # 修正了这里的错误：\f 改为 f，以及 f'(1) 改为 f'(0)
        txt7 = MathTex(
            r"\therefore f(0) = 0, \, f'(0) = 1, \, f''(0) = 0, \, f'''(0) = -1, \, f^{(4)}(0) = 0, \, \cdots",
            color=BLUE,
            font_size=30,
        ).next_to(
            txt6, DOWN, aligned_edge=LEFT, buff=0.25
        )  # ∴……

        txt8 = Text("它们", font_size=26, color=BLUE).next_to(
            txt7, DOWN, aligned_edge=LEFT, buff=0.25
        )
        txt9 = Text(
            "依次循环地取四个数0 , 1 , 0 , -1 . 于是按公式 (",
            font_size=26,
            color=BLUE,
        ).next_to(txt8, RIGHT, aligned_edge=LEFT, buff=0.35)
        txt9_1 = MathTex(r"3-6", font_size=30, color=BLUE).next_to(
            txt9, RIGHT, buff=0.1
        )
        txt9_2 = Text(") 得", font_size=26, color=BLUE).next_to(txt9_1, RIGHT, buff=0.1)

        txt10 = MathTex(
            r" \sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 + \cdots + (-1)^{m - 1}\frac{1}{(2m - 1)!}x^{2m - 1} + R_{2m}(x) , \,",
            color=(BLUE, GREEN),
            font_size=26,
        ).next_to(txt9, DOWN, aligned_edge=LEFT, buff=0.25)

        txt11 = Text("其中", font_size=26, color=BLUE).next_to(
            txt8, DOWN, aligned_edge=LEFT, buff=1.25
        )
        txt12 = MathTex(
            r" R_{2m}(x) = \frac{\sin\left[\theta x + (2m + 1)\pi / 2\right]}{(2m + 1)!} x^{2m + 1} \quad (0 < \theta < 1) ",
            color=(BLUE, GREEN),
            font_size=30,
        ).next_to(txt11, RIGHT, aligned_edge=LEFT, buff=0.45)

        txt13 = Text("取", font_size=26)
        txt14 = MathTex(r"m = 1, \ ", font_size=30)
        txt15 = Text("得近似公式", font_size=26)
        txt16 = MathTex(r"\sin x \approx x \,", font_size=30)
        txt17 = Text("误差", font_size=26)
        txt18 = MathTex(
            r"\vert R_{2}(x) \vert \leq \frac{1}{3!} \vert x \vert^3 \text{.}",
            font_size=30,
        )
        group1 = (
            VGroup(txt13, txt14, txt15, txt16, txt17, txt18)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE, PURPLE)
            .next_to(txt12, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        txt19 = Text("取", font_size=26)
        txt20 = MathTex(r"m = 2, \ ", font_size=30)
        txt21 = Text("得近似公式", font_size=26)
        txt22 = MathTex(r"\sin x \approx x - \frac{1}{3!}x^3 \,", font_size=30)
        txt23 = Text("误差", font_size=26)
        txt24 = MathTex(
            r"\vert R_{4}(x) \vert \leq \frac{1}{5!} \vert x \vert^5 \text{.}",
            font_size=30,
        )
        group2 = (
            VGroup(txt19, txt20, txt21, txt22, txt23, txt24)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE, PURPLE)
            .next_to(group1, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        txt25 = Text("取", font_size=26)
        txt26 = MathTex(r"m = 3, \ ", font_size=30)
        txt27 = Text("得近似公式", font_size=26)
        txt28 = MathTex(
            r"\sin x \approx x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 \,", font_size=30
        )
        txt29 = Text("误差", font_size=26)
        txt30 = MathTex(
            r"\vert R_{6}(x) \vert \leq \frac{1}{7!} \vert x \vert^7 \text{.}",
            font_size=30,
        )
        group3 = (
            VGroup(txt25, txt26, txt27, txt28, txt29, txt30)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE, PURPLE)
            .next_to(group2, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        # 动画编排
        # 第一行
        self.play(Write(group), run_time=3)  # 题目
        self.wait(3)
        # 第二行
        self.play(Write(txt5))  # 解
        self.play(Write(txt6), run_time=2)
        self.wait(10)
        # 第三行
        self.play(Write(txt7), run_time=3)
        self.wait(8)
        # 第四第五行
        self.play(Write(txt8))
        self.play(Write(txt9))
        self.play(Write(txt9_1))
        self.play(Write(txt9_2))
        self.play(Write(txt10), run_time=2)
        self.wait(9)
        # 第六行
        self.play(Write(txt11))
        self.play(Write(txt12), run_time=2)
        self.wait(8.5)
        # m = 1 行
        self.play(Write(group1), run_time=3)
        self.wait(8)
        # m = 2 行
        self.play(Write(group2), run_time=3)
        self.wait(11.5)
        # m = 3 行
        self.play(Write(group3), run_time=3)
        self.wait(16)


SP_16().render()  # 通常不建议在代码中直接调用render()，而是通过命令行运行
