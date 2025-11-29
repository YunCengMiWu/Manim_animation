# -*- coding: utf-8 -*-
from manim import *

# 全局告诉 Manim 在 LaTeX 导言区加载 ctex
from manim.utils.tex import TexTemplate

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{ctex}")  # 支持中文
config.tex_template = my_template


class sin_cos_integral(Scene):
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
        txt2 = Text("证明定积分公式：", font="STKaiti", font_size=30)
        # txt3 = Text("积分公式：", font="STKaiti", font_size=30)
        group = (
            VGroup(txt1, txt2)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE, GREEN)  # 组内对象应用渐变色
            .to_corner(UL, buff=0.5)  # 左上角，与角落边缘距离0.5个单位
        )
        txt4 = MathTex(r"I_n", font_size=30)
        txt5 = MathTex(
            r"= \int_{0}^{\frac{\pi}{2}} \sin^n x \, dx = \int_{0}^{\frac{\pi}{2}} \cos^n x \, dx",
            font_size=30,
        )
        group1 = (
            VGroup(txt4, txt5)
            .arrange(RIGHT, buff=0.2)  # 组内对象按水平排列，对象之间间距0.2个单位
            .set_color_by_gradient(BLUE)  # 组内对象应用渐变色
            .next_to(group, RIGHT, buff=0.45)
        )
        txt6 = MathTex(
            r"""
        = \begin{cases} 
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2}, & \text{当 } n \text{ 为偶数时} \\
            \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{4}{5} \cdot \frac{2}{3}, & \text{当 } n \text{ 为奇数时}
        \end{cases}""",
            font_size=30,
            color=BLUE,
        ).next_to(
            txt5, DOWN, aligned_edge=LEFT, buff=0.25
        )  # 题目结束

        txt7 = Text("证明：", font_size=26, color=BLUE).next_to(
            txt1, DOWN, aligned_edge=LEFT, buff=2.25
        )

        txt8 = Text("令", font_size=26, color=BLUE)
        txt9 = MathTex(r"t = \frac{\pi}{2} - x, ", font_size=30)
        txt10 = Text("则", font_size=26, color=BLUE)
        txt11 = MathTex(
            r"\int_{0}^{\frac{\pi}{2}} \sin^n x \, dx = -\int_{\frac{\pi}{2}}^{0} \sin^n \left( \frac{\pi}{2} - t \right) dt = \int_{0}^{\frac{\pi}{2}} \cos^n x \, dx",
            font_size=30,
            color=BLUE,
        )
        group2 = (
            VGroup(txt8, txt9, txt10, txt11)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(txt7, RIGHT, buff=0.25)
        )

        txt12 = Text("令", font_size=26, color=BLUE)
        txt13 = MathTex(
            r"u = \sin^{n-1} x, \quad v' = \sin x, ",
            font_size=30,
            color=BLUE,
        )
        txt14 = Text("则", font_size=26, color=BLUE)
        txt15 = MathTex(
            r"u' = (n-1) \sin^{n-2} x \cos x, \quad v = -\cos x",
            font_size=30,
            color=BLUE,
        )
        group3 = (
            VGroup(txt12, txt13, txt14, txt15)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(group2, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        txt16 = Text("由定积分的分部积分法，有", font_size=24, color=BLUE).next_to(
            group3, DOWN, aligned_edge=LEFT, buff=0.4
        )

        txt17 = MathTex(r"\therefore I_n", font_size=30)
        txt18 = MathTex(
            r"= \int_{0}^{\frac{\pi}{2}} \sin^n x \, dx = \int_{0}^{\frac{\pi}{2}} \sin^{n-1} x \cdot \sin x \, dx = -\int_{0}^{\frac{\pi}{2}} \sin^{n-1} x \, d(\cos x)",
            font_size=30,
        )
        group4 = (
            VGroup(txt17, txt18)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(txt16, DOWN, aligned_edge=LEFT, buff=0.4)
        )

        txt19 = MathTex(
            r"= \left. \left[ \cos x \cdot \sin^{n-1} x \right] \right|_{0}^{\frac{\pi}{2}} + (n-1) \int_{0}^{\frac{\pi}{2}} \sin^{n-2} x \cos^2 x \, dx",
            font_size=30,
            color=BLUE,
        ).next_to(txt18, DOWN, aligned_edge=LEFT, buff=0.25)
        # 以上生成后清除，腾出空间

        txt20 = Text("上式化简得：", font_size=24, color=BLUE).next_to(
            txt7, RIGHT, buff=0.35
        )
        txt21 = MathTex(
            r"I_n",
            font_size=30,
            color=BLUE,
        )
        txt22 = MathTex(
            r"= (n-1) \int_{0}^{\frac{\pi}{2}} \sin^{n-2} x \cos^2 x \, dx",
            font_size=30,
            color=BLUE,
        )
        group5 = (
            VGroup(txt20, txt21, txt22)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(txt7, RIGHT, buff=0.35)
        )

        txt23 = MathTex(
            r"= (n-1) \int_{0}^{\frac{\pi}{2}} \sin^{n-2} x \left(1 - \sin^2 x\right) dx = (n-1) I_{n-2} - (n-1) I_n",
            font_size=30,
            color=BLUE,
        ).next_to(txt22, DOWN, aligned_edge=LEFT, buff=0.25)

        txt24 = Text("由此得递推公式：", font_size=24, color=BLUE)
        txt25 = MathTex(
            r"I_n = \frac{n - 1}{n} I_{n - 2}",
            font_size=30,
            color=BLUE,
        )
        group6 = (
            VGroup(txt24, txt25)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(group5, DOWN, aligned_edge=LEFT, buff=1.35)
        )

        txt26 = Text("于是，", font_size=24, color=BLUE).next_to(
            group6, DOWN, aligned_edge=LEFT, buff=0.5
        )

        txt27 = MathTex(
            r"I_{2m} = \frac{2m - 1}{2m} \cdot \frac{2m - 3}{2m - 2} \cdots \frac{3}{4} \cdot \frac{1}{2} \cdot I_0",
            font_size=30,
            color=BLUE,
        ).next_to(txt26, RIGHT, buff=0.35)
        txt28 = MathTex(
            r"I_{2m+1} = \frac{2m}{2m + 1} \cdot \frac{2m - 2}{2m - 1} \cdots \frac{4}{5} \cdot \frac{2}{3} \cdot I_1",
            font_size=30,
            color=BLUE,
        ).next_to(txt27, DOWN, aligned_edge=LEFT, buff=0.35)

        txt29 = Text("而", font_size=24, color=BLUE)
        txt30 = MathTex(
            r"I_0 = \int_{0}^{\frac{\pi}{2}} dx = \frac{\pi}{2}, \quad I_1 = \int_{0}^{\frac{\pi}{2}} \sin x \, dx = 1",
            font_size=30,
            color=BLUE,
        )

        txt31 = Text("故所证结论成立.", font_size=24, color=BLUE)

        # 动画编排
        self.play(Write(group), run_time=2)
        self.play(Write(group1), run_time=2)
        self.wait(7)
        self.play(Write(txt6), run_time=3)
        self.wait(17)

        # 解题过程

        self.play(Write(txt7), run_time=1)  # 证明二字
        self.play(Write(group2), run_time=2)
        self.wait(15)

        self.play(Write(group3), run_time=2)
        self.wait(12)

        self.play(Write(txt16), run_time=2)
        self.play(Write(group4), run_time=2)
        self.wait(15)

        self.play(Write(txt19), run_time=2)
        self.wait(11)
        self.play(FadeOut(group2, group3, txt16, group4, txt19))

        self.play(Write(group5), run_time=2)
        self.play(Write(txt23), run_time=2)
        self.wait(17.5)

        self.play(Write(group6), run_time=2)
        self.wait(3)

        self.play(Write(txt26))  # 于是,
        self.play(Write(txt27), run_time=2)
        self.play(Write(txt28), run_time=2)
        self.wait(6)

        self.play(FadeOut(group5, txt23, group6))
        group8 = VGroup(txt26, txt27, txt28)

        # 2. 带动画的位置移动（可设置时间）
        group8.generate_target()  # 创建目标状态
        group8.target.next_to(txt7, RIGHT, aligned_edge=UP, buff=0.5)  # 定义目标位置
        self.play(MoveToTarget(group8), run_time=2)  # 2秒内移动到目标位置
        self.wait(9.5)

        group7 = (
            VGroup(txt29, txt30)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(txt26, DOWN, aligned_edge=LEFT, buff=1.45)
        )

        txt31.next_to(group7, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(Write(group7), run_time=2)
        self.wait(8)

        self.play(Write(txt31), run_time=1.5)
        self.wait(3.5)


sin_cos_integral().render()
