from manim import *
import numpy as np

# 全局告诉 Manim 在 LaTeX 导言区加载 ctex
from manim.utils.tex import TexTemplate

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{ctex}")  # 支持中文
config.tex_template = my_template


class Slicing_method(ThreeDScene):
    def construct(self):

        # LOGO
        ellipse = Ellipse(
            width=0.8, height=0.4, color=BLUE, fill_opacity=1, stroke_width=3
        )
        colors_ = [BLUE_B, PURPLE, GREEN, GOLD]
        ellipse.set_color(color_gradient(colors_, 100))  # 渐变色填充
        ellipse.to_corner(UR, buff=0.21)  # 右上角

        text = Text("CQU", font="Dancing Script", weight="BOLD", font_size=24)
        self.add_fixed_in_frame_mobjects(ellipse)
        self.add_fixed_in_frame_mobjects(text)
        text.set_color(BLACK)
        text.to_corner(UR, buff=0.3)
        self.add(ellipse, text)  # 直接添加，不做动画

        question = (
            VGroup(
                Text("例  计算三重积分", font_size=33),
                MathTex(
                    r"\iiint_{\Omega} z^2 \, dxdy dz \, , \, \text{其中} \, \Omega: \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} \leq 1",
                    font_size=38,
                ),
            )
            .arrange(RIGHT, buff=0.15)
            .set_color_by_gradient((YELLOW, BLUE))
            .to_corner(UL, buff=0.5)
        )
        self.play(Write(question), run_time=3)
        self.wait(4)
        self.play(FadeOut(question), run_time=3)

        # 绘制椭球三维图形
        def ellipse_surface(u, v):
            x = 1.5 * np.sin(u) * np.cos(v)  # a设为1.5，可根据需要调整
            y = 2.5 * np.sin(u) * np.sin(v)  # b设为2.5，可根据需要调整
            z = 2 * np.cos(u)  # c设为2，可根据需要调整
            return np.array([x, y, z])

        ellipsoid = Surface(
            ellipse_surface,
            u_range=[0, np.pi],
            v_range=[0, 2 * np.pi],
            fill_opacity=0.35,
            checkerboard_colors=[BLUE, BLUE_E],
            stroke_width=1,
            resolution=(30, 20),  # 降低曲面分辨率
        )
        # 添加三维坐标轴
        axes = ThreeDAxes(
            x_range=[-1.55, 1.55, 1],
            y_range=[-2.55, 2.55, 1],
            z_range=[-2.5, 2.5, 1],
            axis_config={"stroke_color": WHITE},
            tips=True,
        )
        labels = axes.get_axis_labels(
            MathTex(r"x", font_size=72, color=WHITE),
            MathTex(r"y", font_size=72, color=WHITE),
            MathTex(r"z", font_size=72, color=WHITE),
        )

        self.set_camera_orientation(phi=80 * DEGREES, theta=-30 * DEGREES)
        self.play(Create(VGroup(axes, labels)), run_time=1)
        self.play(Create(ellipsoid), run_time=4)

        # --- 新增截面椭圆代码 start ---
        # 1. 计算z=z0处截面椭圆的参数（长半轴a', 短半轴b'）
        a = 1.5
        b = 2.5
        c = 2
        z0 = 0.75
        a_prime = a * np.sqrt(1 - (z0**2) / (c**2))  # 截面椭圆x方向半轴
        b_prime = b * np.sqrt(1 - (z0**2) / (c**2))  # 截面椭圆y方向半轴

        # 2. 生成3D截面椭圆（参数方程：x=a'cosθ, y=b'sinθ, z=z0）
        def cross_section_ellipse(theta):
            x = a_prime * np.cos(theta)
            y = b_prime * np.sin(theta)
            z = z0  # 固定z坐标为z0
            return np.array([x, y, z])

        # 创建截面椭圆（红色高亮，与椭球区分）
        cross_ellipse = ParametricFunction(
            cross_section_ellipse,
            t_range=[0, 2 * np.pi],  # θ从0到2π
            stroke_color=RED,  # 红色醒目
            stroke_width=6,  # 线宽加粗
            stroke_opacity=1,  # 不透明
        )

        # # 3. 添加辅助线：z轴到截面椭圆的垂线（从(0,0,0)到(0,0,z0)）
        # z_line = Line(
        #     start=axes.c2p(0, 0, 0),    # 起点：z轴原点
        #     end=axes.c2p(0, 0, z0),     # 终点：截面椭圆中心
        #     color=ORANGE,               # 橙色辅助线
        #     stroke_width=2,
        #     stroke_opacity=0.8
        # )

        # # 4. 添加截面标签（标注"z=z0"和截面中心）
        # # 标签1：z=z0（放在截面椭圆旁，固定在3D场景中）
        # z_label = MathTex(f"z={z0}", font_size=40, color=RED)
        # z_label.move_to(axes.c2p(a_prime + 0.3, 0, z0))  # 放在椭圆右侧
        # z_label.rotate(theta=-30 * DEGREES, axis=UP)     # 旋转以适配相机视角
        # # 标签2：截面中心O'（放在辅助线顶端）
        # center_label = MathTex(r"O'", font_size=36, color=ORANGE)
        # center_label.move_to(axes.c2p(0, 0, z0) + np.array([0.2, 0.2, 0]))  # 偏移避免遮挡

        # 5. 动画显示截面相关元素（先线→再椭圆→最后标签）
        self.play(Create(cross_ellipse), run_time=2)  # 显示截面椭圆
        self.wait(2)  # 暂停观察截面
        # --- 新增截面椭圆代码 end ---

        all_3d_objects = VGroup(
            axes,
            labels,
            ellipsoid,
            cross_ellipse,
        )
        # 先缩放（1秒），再移动（1秒）
        self.play(all_3d_objects.animate.scale(0.3), run_time=2.5)
        self.play(Wait(2))
        self.play(
            all_3d_objects.animate.to_edge(DR).shift(RIGHT * 3.0 + IN * 0.05),
            run_time=1,
        )
        self.play(Wait(2))

        # 求解开始
        txt = Text(
            "解", font="STKaiti", font_size=34, weight="BOLD", color=BLUE
        ).next_to(question, DOWN, aligned_edge=LEFT, buff=0.4)
        jie_1 = (
            VGroup(
                Text("积分区域 Ω 如图, 竖坐标范围", font_size=26),
                MathTex(r"-c \leq z \leq c", font_size=30),
            )
            .arrange(RIGHT, buff=0.15)
            .set_color_by_gradient(BLUE)
            .next_to(txt, RIGHT, buff=0.25)
        )
        jie_2 = (
            VGroup(
                Text("任取", font_size=26),
                MathTex(r"[-c, c]", font_size=30),
                Text("上一点 z ,过该点作垂直于轴的平面，交Ω得椭圆截面", font_size=26),
                MathTex(r"D_z", font_size=30),
            )
            .arrange(RIGHT, buff=0.15)
            .set_color_by_gradient(BLUE)
            .next_to(jie_1, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        jie_3 = (
            VGroup(
                Text("其方程为", font_size=26),
                MathTex(
                    r"D_z: \frac{x^2}{a^2} + \frac{y^2}{b^2} \leq 1 - \frac{z^2}{c^2} \iff \frac{x^2}{\left(a\sqrt{1 - \frac{z^2}{c^2}}\right)^2} + \frac{y^2}{\left(b\sqrt{1 - \frac{z^2}{c^2}}\right)^2} \leq 1",
                    font_size=30,
                ),
            )
            .arrange(RIGHT, buff=0.15)
            .set_color_by_gradient(BLUE)
            .next_to(jie_2, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        self.add_fixed_in_frame_mobjects(question)
        self.add_fixed_in_frame_mobjects(txt)
        self.add_fixed_in_frame_mobjects(jie_1)
        self.add_fixed_in_frame_mobjects(jie_2)
        self.add_fixed_in_frame_mobjects(jie_3)
        self.play(FadeIn(question), run_time=3)
        self.play(Write(txt))
        self.play(Write(jie_1), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_2), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_3), run_time=2)
        self.play(Wait(4))

        # # 创建一个二维椭圆
        # ellipse = Ellipse(width=2.5, height=1.5, color=BLUE)
        # self.add_fixed_in_frame_mobjects(ellipse)
        # # 在3D场景中展示（默认在xy平面）
        # self.play(FadeIn(ellipse), run_time=2)
        # self.wait(2)

        # 创建 2D 坐标轴
        axes_1 = Axes(
            x_range=[-2.75, 2.75],
            y_range=[-1.75, 1.75],
            x_length=5.5,
            y_length=3.5,
            axis_config={
                "color": WHITE,
                "include_numbers": False,  # 不显示数字
                "include_ticks": False,  # 不显示刻度
            },
        )
        axes_1.scale(0.6)
        # # 添加坐标轴标签（默认是 MathTex）
        # labels_1 = axes.get_axis_labels(
        #     x_label=MathTex("x", font_size=72, color=WHITE),
        #     y_label=MathTex("y", font_size=72, color=WHITE),
        # )
        # 创建 2D 椭圆
        ellipse_1 = Ellipse(width=2.5, height=1.5, color=RED, stroke_width=6)
        # 为长短轴添加标签
        x_a = (
            MathTex(r"a\sqrt{1 - \frac{z^2}{c^2}}").next_to(axes_1.c2p(2, 0)).scale(0.4)
        )
        y_b = (
            MathTex(r"b\sqrt{1 - \frac{z^2}{c^2}}")
            .next_to(axes_1.c2p(0, 1.5))
            .scale(0.4)
        )
        all_2d_objects = (
            VGroup(
                axes_1,
                # labels_1,
                x_a,
                y_b,
                ellipse_1,
            )
            .scale(1.2)
            .next_to(jie_3, DOWN, buff=0.25)
            .shift(LEFT * 2)
        )
        x_a.shift(UP * 0.5 + LEFT * 1.0)
        y_b.shift(LEFT * 3.0)

        # 添加到场景

        self.add_fixed_in_frame_mobjects(axes_1)
        # self.add_fixed_in_frame_mobjects(labels_1)
        self.add_fixed_in_frame_mobjects(x_a)
        self.add_fixed_in_frame_mobjects(y_b)
        self.add_fixed_in_frame_mobjects(ellipse_1)
        self.play(Create(all_2d_objects), run_time=3)
        self.wait(4)

        # 移除前面的步骤文本，为后续内容腾出空间
        self.play(FadeOut(jie_1), FadeOut(jie_2), FadeOut(jie_3), run_time=3)
        # 2. 带动画的位置移动（可设置时间）
        all_2d_objects.generate_target()  # 创建目标状态
        all_2d_objects.target.next_to(
            question, DOWN, aligned_edge=RIGHT, buff=0.25
        ).shift(
            RIGHT * 1
        )  # 定义目标位置
        self.play(MoveToTarget(all_2d_objects), run_time=2)  # 2秒内移动到目标位置
        self.play(Wait(4))

        jie_4 = (
            (
                VGroup(
                    Text("从而积分区域Ω可表示为：", font_size=23),
                    MathTex(
                        r"\Omega: \begin{cases} -c \leq z \leq c \\ D_z: \frac{x^2}{\left(a\sqrt{1 - \frac{z^2}{c^2}}\right)^2} + \frac{y^2}{\left(b\sqrt{1 - \frac{z^2}{c^2}}\right)^2} \leq 1 \end{cases}",
                        font_size=27,
                    ),
                ).arrange(DOWN, buff=0.25)
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .set_color_by_gradient(BLUE)
            .next_to(txt, RIGHT, aligned_edge=UP, buff=0.25)
        )
        jie_5 = (
            VGroup(
                MathTex(r"D_z", font_size=27),
                Text("的面积为: ", font_size=23),
                MathTex(
                    r"A_{D_z} = \pi \left(a\sqrt{1 - \frac{z^2}{c^2}}\right) \left(b\sqrt{1 - \frac{z^2}{c^2}}\right)",
                    font_size=27,
                ),
            )
            .arrange(RIGHT, buff=0.15)
            .set_color_by_gradient(BLUE)
            .next_to(jie_4, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # jie_6_1 = (
        #     MathTex(
        #         r"\therefore \iiint_{\Omega} z^2 \, dx \, dy \, dz \,", font_size=30
        #     )
        #     .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        #     .set_color_by_gradient(BLUE)
        #     .next_to(jie_4, DOWN, aligned_edge=LEFT, buff=0.35)
        # )
        jie_6_1 = MathTex(
            r"\therefore \iiint_{\Omega} z^2 \, dx \, dy \, dz \,", font_size=27
        )
        jie_6_2 = MathTex(
            r"= \, \int_{-c}^{c} z^2 \, dz \iint_{D_z} dxdy", font_size=27
        )
        jie_6 = (
            VGroup(
                jie_6_1,
                jie_6_2,
            )
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(jie_5, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        jie_7 = MathTex(
            r"= \, 2 \int_{0}^{c} z^2 \cdot \pi ab \left(1 - \frac{z^2}{c^2}\right) dz",
            font_size=27,
            color=BLUE,
        ).next_to(jie_6_2, DOWN, aligned_edge=LEFT, buff=0.25)
        jie_8 = MathTex(
            r"= \, \frac{4}{15} \pi abc^3",
            font_size=27,
            color=BLUE,
        ).next_to(jie_7, DOWN, aligned_edge=LEFT, buff=0.25)
        self.add_fixed_in_frame_mobjects(jie_4)
        self.add_fixed_in_frame_mobjects(jie_5)
        self.add_fixed_in_frame_mobjects(jie_6)
        self.add_fixed_in_frame_mobjects(jie_7)
        self.add_fixed_in_frame_mobjects(jie_8)
        self.play(Write(jie_4), run_time=3)
        self.play(Wait(4))
        self.play(Write(jie_5), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_6), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_7), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_8), run_time=2)
        self.play(Wait(4))


# # 480p 15
# if __name__ == "__main__":
#     from manim import config

#     config.media_dir = "./media"
#     config.quality = "low_quality"
#     scene = Slicing_method()
#     scene.render()

Slicing_method().render()
