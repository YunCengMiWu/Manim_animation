# -*- coding: utf-8 -*-
from manim import *


class demonstrate(Scene):
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

        txt1 = Text("例 ", font="STKaiti", font_size=40, weight="BOLD")
        txt2 = Text("求极限", font="STKaiti", font_size=36)
        txt3 = MathTex(
            r"\lim_{x \to 0} \frac{e^{x^2} + \cos x - \frac{x^2}{2} - 2}{x^4}.",
            font_size=45,
        )
        # txt4 = Text(".", font="STKaiti", font_size=36)

        group = (
            VGroup(txt1, txt2, txt3)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色，BLUE 过渡 GREEN
            .to_corner(
                UL, buff=0.5
            )  # 将整个组移动到场景的角落，UL指左上角，与角落边缘距离0.5个单位
        )  # 链式调用 UL UR DL DR

        # 求解开始
        txt5 = Text(
            "解", font="STKaiti", font_size=34, weight="BOLD", color=BLUE
        ).next_to(group, DOWN, aligned_edge=LEFT, buff=0.4)

        # 3.1 泰勒公式
        txt6 = MathTex(
            r"\because \mathrm{e}^{x^2} = 1 + x^2 + \frac{1}{2!}x^4 + o(x^4),",
            font_size=40,
        )
        # txt7 = Text(", ", font="STKaiti", font_size=33)
        txt8 = MathTex(
            r"\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^5)", font_size=40
        )
        group1 = (
            VGroup(txt6, txt8)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色，BLUE 过渡 GREEN
            .next_to(
                txt5, RIGHT, buff=0.25
            )  # 将当前组（group1）定位到指定对象（txt5）的特定方向，并保持指定距离。
        )  # 链式调用 UL UR DL DR

        # 3.2 结论
        txt9 = MathTex(r"\therefore")
        txt10 = Text("原式", font="STKaiti", font_size=36, color=BLUE)
        group2 = (
            VGroup(txt9, txt10)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(group1, DOWN, aligned_edge=LEFT, buff=0.7)
        )
        # txt10 = Text(
        #     "原式", font="STKaiti", font_size=34, color=BLUE
        # ).next_to(group2, RIGHT, aligned_edge=LEFT, buff=0.25)

        txt11 = MathTex(
            r"=",
            font_size=33,
            color=BLUE,
        ).next_to(group2, RIGHT, aligned_edge=ORIGIN, buff=0.25)
        # group3 = (
        #     VGroup(txt11)
        #     .arrange(RIGHT, buff=0.2)
        #     .set_color_by_gradient(BLUE, GREEN, PURPLE)
        #     .next_to(group2, RIGHT, aligned_edge=ORIGIN, buff=0.25)
        # )
        txt14 = MathTex(
            r" \lim_{x \to 0} \frac{\left[1 + x^2 + \frac{1}{2!}x^4 + o(x^4)\right] + \left[1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^5)\right] - \frac{x^2}{2} - 2}{x^4}",
            font_size=33,
            color=BLUE,
        ).next_to(txt11, RIGHT, aligned_edge=ORIGIN, buff=0.2)

        txt12 = (
            MathTex(
                r"= \lim_{x \to 0} \frac{\left( \frac{1}{2!} + \frac{1}{4!} \right) x^4 + o(x^4)}{x^4}"
            )
            .set_color_by_gradient(BLUE)
            .next_to(txt11, DOWN, aligned_edge=LEFT, buff=0.7)
        )
        txt13 = (
            MathTex(r"= \frac{13}{24}")
            .set_color_by_gradient(BLUE)
            .next_to(txt12, DOWN, aligned_edge=LEFT, buff=0.35)
        )

        # 动画编排
        self.play(Write(group), run_time=7)  # 题目
        self.wait(4)

        self.play(Write(txt5))  # 解
        self.play(Write(group1), run_time=2)  # 泰勒展开
        self.wait(14)  # 14

        self.play(Write(group2), run_time=1)  # ∴ 原式

        self.play(Write(txt11))  # = 代入
        self.play(Write(txt14), run_time=2)  # = 代入
        self.wait(18.5)  # 20
        # 50
        self.play(Write(txt12), run_time=2)  # = 化简
        self.wait(9.5)

        self.play(Write(txt13), run_time=2)  # = 结果
        self.wait(4)


demonstrate().render()
