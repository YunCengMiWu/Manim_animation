# -*- coding: utf-8 -*-
from manim import *


class Infinite_integral(Scene):
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
        txt2 = Text("证明： ", font="STKaiti", font_size=30)
        txt3 = MathTex(
            r"\int_{0}^{+\infty} \frac{dx}{1 + x^4} = \int_{0}^{+\infty} \frac{x^2}{1 + x^4} \, dx",
            font_size=30,
        )
        txt4 = Text(", 并求其值.", font_size=26)
        group = (
            VGroup(txt1, txt2, txt3, txt4)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .to_corner(UL, buff=0.5)  # 左上角，与角落边缘距离0.5个单位
        )

        # 解
        txt5_0 = Text(
            "解：", font="STKaiti", font_size=30, weight="BOLD", color=BLUE
        ).next_to(group, DOWN, aligned_edge=LEFT, buff=0.6)

        # 补充框：
        txt17_0 = Text(
            "在被积函数为分式且分母阶次较高时可考虑倒代换",
            font_size=22,
        ).next_to(txt5_0, DOWN, aligned_edge=LEFT, buff=1.85)
        # 金色框
        box1_0 = SurroundingRectangle(
            txt17_0,
            color=ORANGE,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3,
            fill_opacity=0.2,
        )
        box1_0.next_to(txt17_0, ORIGIN)

        txt5 = Text("利用倒代换有", font_size=26)
        txt6 = MathTex(r" \int_{0}^{+\infty} \frac{dx}{1 + x^4} ", font_size=30)
        txt7 = MathTex(
            r" \stackrel{t = \frac{1}{x}}{=} ",
            font_size=36,
        )
        txt7_1 = MathTex(
            r" \int_{+\infty}^{0} \frac{1}{1 + \frac{1}{t^4}} \left( -\frac{1}{t^2} \right) dt ",
            font_size=30,
        )
        group1 = (
            VGroup(txt5, txt6, txt7, txt7_1)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .next_to(txt5_0, RIGHT, buff=0.25)
        )

        txt8 = MathTex(
            r"= \int_{0}^{+\infty} \frac{t^2}{1 + t^4} \, dt", color=BLUE, font_size=30
        )
        txt9 = MathTex(
            r"= \int_{0}^{+\infty} \frac{x^2}{1 + x^4} \, dx",
            color=PURPLE,
            font_size=30,
        )
        # group2 = (
        #     VGroup(txt5, txt6, txt7)
        #     .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
        #     .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
        #     .next_to(txt7, DOWN, aligned_edge=LEFT, buff=0.25)
        # )
        group2 = (
            VGroup(txt8, txt9)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .next_to(txt7, DOWN, aligned_edge=LEFT, buff=0.45)
        )

        txt10 = MathTex(
            r"\therefore \int_{0}^{+\infty}",
            font_size=30,
        )
        txt11 = MathTex(
            r"\frac{dx}{1 + x^4} = \frac{1}{2} \left[ \int_{0}^{+\infty} \frac{dx}{1 + x^4} + \int_{0}^{+\infty} \frac{x^2}{1 + x^4} \, dx \right] = \frac{1}{2} \int_{0}^{+\infty} \frac{1 + x^2}{1 + x^4} \, dx ",
            font_size=30,
        )
        group3 = (
            VGroup(txt10, txt11)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE)
            .next_to(txt5_0, DOWN, aligned_edge=LEFT, buff=2.6)
        )

        txt12 = MathTex(
            r"= \frac{1}{2} \int_{0}^{+\infty} \frac{\frac{1}{x^2} + 1}{\frac{1}{x^2} + x^2} \, dx",
            color=(BLUE, PURPLE),
            font_size=30,
        ).next_to(txt11, DOWN, aligned_edge=LEFT, buff=0.45)
        # 以上生成后清除，腾出空间

        txt13 = MathTex(
            r"= \frac{1}{2} \int_{0}^{+\infty} \frac{1}{\left(x - \frac{1}{x}\right)^2 + 2} \, d\left(x - \frac{1}{x}\right)",
            font_size=30,
            color=BLUE,
        )

        txt14 = MathTex(
            r"= \left. \frac{1}{2\sqrt{2}} \arctan \frac{x - \frac{1}{x}}{\sqrt{2}} \right|_{0^+}^{+\infty}",
            font_size=30,
            color=BLUE,
        )

        txt15 = MathTex(
            r"= \lim_{x \to +\infty} \frac{1}{2\sqrt{2}} \arctan \frac{x - \frac{1}{x}}{\sqrt{2}} - \lim_{x \to 0^+} \frac{1}{2\sqrt{2}} \arctan \frac{x - \frac{1}{x}}{\sqrt{2}}",
            font_size=30,
            color=BLUE,
        )

        txt16 = MathTex(
            r"= \frac{1}{2\sqrt{2}} \cdot \frac{\pi}{2} - \frac{1}{2\sqrt{2}} \cdot \left(-\frac{\pi}{2}\right) = \frac{\pi}{2\sqrt{2}}",
            font_size=30,
            color=BLUE,
        )
        # ----------------------------------------------------------
        # 4. 右侧补充框：
        # ----------------------------------------------------------
        txt17 = MathTex(
            r"\int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a} \arctan \frac{x}{a} + C",
            font_size=30,
        )
        # 金色框
        box1 = SurroundingRectangle(
            txt17,
            color=ORANGE,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3,
            fill_opacity=0.2,
        )

        # 动画编排
        self.play(Write(group), run_time=2)
        self.wait(11)

        self.play(Write(txt5_0))

        # 框及文字
        self.play(Create(box1_0))  # 先画框
        self.play(Create(txt17_0), run_time=0.5)  # 再写文字
        self.wait(3.5)

        self.play(Write(group1), run_time=2)
        self.wait(14)

        self.play(Write(group2), run_time=2)
        self.wait(8)

        self.play(Write(group3), run_time=3)
        self.wait(20)

        self.play(Write(txt12), run_time=1)
        self.wait(1)

        self.play(FadeOut(group1, group2, group3, txt17_0, box1_0))

        # 2. 带动画的位置移动（可设置时间）
        txt12.generate_target()  # 创建目标状态
        txt12.target.next_to(txt5_0, RIGHT, aligned_edge=UP, buff=0.5)  # 定义目标位置
        self.play(MoveToTarget(txt12), run_time=2)  # 2秒内移动到目标位置

        # txt12.next_to(txt5_0, RIGHT, aligned_edge=UP, buff=0.5)
        txt13.next_to(txt12, DOWN, aligned_edge=LEFT, buff=0.35)
        txt14.next_to(txt13, DOWN, aligned_edge=LEFT, buff=0.35)
        txt15.next_to(txt14, DOWN, aligned_edge=LEFT, buff=0.35)
        txt16.next_to(txt15, DOWN, aligned_edge=LEFT, buff=0.35)

        txt17.next_to(txt13, RIGHT, buff=1.0)
        box1.next_to(txt17, ORIGIN)

        # self.play(Write(txt12), run_time=1)
        # self.wait(1.5)

        self.play(Write(txt13), run_time=2)
        self.wait(8.5)

        # 框及文字
        self.play(Create(box1))  # 先画框
        self.play(Create(txt17), run_time=2)  # 再写文字
        self.wait(1.5)

        self.play(Write(txt14), run_time=2)
        self.wait(6)

        self.play(Write(txt15), run_time=3)
        self.wait(8)

        self.play(Write(txt16), run_time=2)
        self.wait(9.5)


Infinite_integral().render()  # 通常不建议在代码中直接调用render()，而是通过命令行运行
