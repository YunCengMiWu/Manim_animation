# -*- coding: utf-8 -*-
from manim import *


class Improper_integral(Scene):
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

        # 题目
        txt1 = Text("例 ", font="STKaiti", font_size=34, weight="BOLD")
        txt2 = Text("证明：反常积分 ", font="STKaiti", font_size=30)
        txt3 = MathTex(r"\int_{a}^{b} \frac{dx}{(x - a)^q}", font_size=30)
        txt4 = Text("当", font_size=26)
        txt4_1 = MathTex(r"q < 1", font_size=30)
        txt4_2 = Text("时 收敛; ", font_size=26)
        txt4_3 = Text("当", font_size=26)
        txt4_4 = MathTex(r"q \geq 1", font_size=30)
        txt4_5 = Text("时 发散.", font_size=26)
        group = (
            VGroup(txt1, txt2, txt3, txt4, txt4_1, txt4_2, txt4_3, txt4_4, txt4_5)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .to_corner(UL, buff=0.5)  # 左上角，与角落边缘距离0.5个单位
        )

        txt5 = Text(
            "证明：", font="STKaiti", font_size=30, weight="BOLD", color=BLUE
        ).next_to(group, DOWN, aligned_edge=LEFT, buff=0.4)

        txt6 = Text("当", font_size=26)
        txt6_1 = MathTex(r"q = 1", font_size=30)
        txt6_2 = Text("时, ", font_size=26)
        txt7 = MathTex(
            r" \int_{a}^{b} \frac{dx}{x - a} = \left[ \ln \vert x - a \vert \right]_{a^+}^{b} = +\infty \text{.}",
            font_size=30,
        )
        group1 = (
            VGroup(txt6, txt6_1, txt6_2, txt7)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE)  # 组内对象应用渐变色
            .next_to(txt5, RIGHT, buff=0.25)
        )

        txt8 = Text("当", font_size=26)
        txt8_1 = MathTex(r"q \neq 1", font_size=30)
        txt8_2 = Text("时, ", font_size=26)
        group4 = (
            VGroup(txt8, txt8_1, txt8_2)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE)  # 组内对象应用渐变色
            .next_to(txt6, DOWN, aligned_edge=LEFT, buff=0.55)
        )

        txt9 = MathTex(
            r"""
        \int_{a}^{b} \frac{dx}{(x - a)^q} 
        = \left. \left[ \frac{(x - a)^{1 - q}}{1 - q} \right] \right|_{a^+}^{b} 
        = 
        \begin{cases} 
            \frac{(b - a)^{1 - q}}{1 - q}, & q < 1 \\
            +\infty, & q > 1 
        \end{cases}
        """,
            color=BLUE,
            font_size=30,
        ).next_to(txt8, DOWN, aligned_edge=LEFT, buff=0.45)

        txt10 = Text("综上", font_size=26, color=BLUE)
        txt11 = Text("所述", font_size=26, color=BLUE)
        group2 = (
            VGroup(txt10, txt11)
            .arrange(DOWN, buff=0.25)
            .set_color_by_gradient(BLUE)
            .next_to(txt5, DOWN, aligned_edge=ORIGIN, buff=2.85)
        )

        txt12 = Text("当", font_size=26)
        txt12_1 = MathTex(r"q < 1", font_size=30)
        txt12_2 = Text("时, 该广义积分收敛, 其值为", font_size=26)
        txt13 = MathTex(r"\frac{(b - a)^{1 - q}}{1 - q};", font_size=30)
        group3 = (
            VGroup(txt12, txt12_1, txt12_2, txt13)
            .arrange(RIGHT, buff=0.25)
            .set_color_by_gradient(BLUE)
            .next_to(txt10, RIGHT, aligned_edge=ORIGIN, buff=0.35)
        )

        txt14 = Text("当", font_size=26)
        txt14_1 = MathTex(r"q \geq 1", font_size=30)
        txt14_2 = Text("时, 该广义积分发散.", font_size=26)
        group5 = (
            VGroup(txt14, txt14_1, txt14_2)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE)  # 组内对象应用渐变色
            .next_to(txt12, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        # ----------------------------------------------------------
        # 4. 右侧补充框：记牢此结论！
        # ----------------------------------------------------------
        txt15 = Text("记牢此结论！ ", font="STKaiti", font_size=28).next_to(
            group, DOWN, aligned_edge=RIGHT, buff=0.5
        )
        # 金色框
        box1 = SurroundingRectangle(
            txt15,
            color=ORANGE,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3,
            fill_opacity=0.2,
        )
        box1.next_to(txt15, ORIGIN)

        # 动画编排
        # 第一行
        self.play(Write(group), run_time=3)  # 题目
        self.wait(8)
        # 第二行
        self.play(Write(txt5))  # 解
        self.play(Write(group1), run_time=2)
        self.wait(6)
        # 第三第四行
        self.play(Write(group4))
        self.play(Write(txt9), run_time=3)
        self.wait(14)
        # 综上所述
        self.play(Write(group2))
        self.wait(0.5)
        # 结论一
        self.play(Write(group3), run_time=2)
        self.wait(6)
        # 结论二
        self.play(Write(group5), run_time=1)
        self.wait(3)
        # 框及文字
        self.play(Create(box1))  # 先画框
        self.play(Create(txt15), run_time=2.5)
        self.wait(4)


Improper_integral().render()  # 通常不建议在代码中直接调用render()，而是通过命令行运行
