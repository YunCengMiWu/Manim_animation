from manim import *
import numpy as np


class Spherical_Coordinate_System(ThreeDScene):
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

        question_1 = VGroup(
            Text("例  计算三重积分", font_size=33),
            MathTex(
                r"\iiint_{\Omega} (x^2 + y^2 + z^2) \, dx \, dy \, dz",
                font_size=38,
            ),
            Text(", 其中", font_size=33),
        ).arrange(RIGHT, buff=0.15)
        question_2 = VGroup(
            Text("Ω为锥面", font_size=33),
            MathTex(
                r"z = \sqrt{x^2 + y^2}",
                font_size=38,
            ),
            Text("与球面", font_size=33),
            MathTex(
                r"x^2 + y^2 + z^2 = R^2",
                font_size=38,
            ),
            Text("所围立体", font_size=33),
        ).arrange(RIGHT, buff=0.15)
        question = (
            VGroup(question_1, question_2)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .set_color_by_gradient((YELLOW, BLUE))
            .to_corner(UL, buff=0.5)
        )
        self.play(Write(question), run_time=3)
        self.wait(4)
        self.play(FadeOut(question), run_time=3)

        # ------------------------------------------------------------------

        # 定义参数范围，u对应极角相关，v对应方位角
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi / 4, 100)  # 球面部分到圆锥面交线（φ=π/4）

        # 球面方程参数化：x = r*sinφ*cosθ, y = r*sinφ*sinθ, z = r*cosφ ，这里r=1
        def sphere_surface(u, v):
            x = 2.75 * np.sin(v) * np.cos(u)
            y = 2.75 * np.sin(v) * np.sin(u)
            z = 2.75 * np.cos(v)
            return np.array([x, y, z])

        # 圆锥面方程参数化：z = sqrt(x² + y²) ，转换为极坐标形式 x = r*cosθ, y = r*sinθ, z = r ，r从0到sin(π/4)=√2/2（交线处r范围 ）
        def cone_surface(u, v):
            r = np.sin(
                v
            )  # 利用v范围，让r在交线内合理变化，也可直接用固定r范围结合条件，这里简化
            x = 2.75 * r * np.cos(u)
            y = 2.75 * r * np.sin(u)
            z = 2.75 * r
            return np.array([x, y, z])

        # 创建球面Surface对象
        sphere = Surface(
            lambda u, v: sphere_surface(u, v),
            u_range=[0, 2 * np.pi],
            v_range=[0, np.pi / 4],
            stroke_color=GREEN,
            resolution=(10, 10),
            fill_opacity=0.2,
        )

        # 创建圆锥面Surface对象
        cone = Surface(
            lambda u, v: cone_surface(u, v),
            u_range=[0, 2 * np.pi],
            v_range=[0, np.pi / 4],
            checkerboard_colors=[WHITE],
            resolution=(10, 10),
            fill_opacity=0.2,
        )

        # 添加三维坐标轴
        axes = ThreeDAxes(
            x_range=[-1.55, 1.55, 1],
            y_range=[-0.55, 0.55, 1],
            z_range=[-2.5, 2.5, 1],
            x_length=8,
            y_length=6,
            axis_config={"stroke_color": WHITE},
            tips=True,
        )
        labels = axes.get_axis_labels(
            MathTex(r"x", font_size=72, color=WHITE),
            MathTex(r"y", font_size=72, color=WHITE),
            MathTex(r"z", font_size=72, color=WHITE),
        )

        # 设置三维场景视角
        self.set_camera_orientation(phi=80 * DEGREES, theta=-30 * DEGREES)
        # 添加坐标轴
        self.play(Create(VGroup(axes, labels)), run_time=1)
        # 将两个曲面添加到场景
        self.play(Create(sphere), run_time=2)
        self.play(Create(cone), run_time=2)
        self.play(Wait(3))

        # 在xy平面上创建一个圆来显示θ的范围
        theta_circle_radius = 1  # 圆的半径
        theta_circle = Circle(
            radius=theta_circle_radius, color=BLUE, stroke_width=4, fill_opacity=0.1
        ).shift(
            Z_AXIS * 0.01
        )  # 轻微上移避免与坐标轴完全重合

        # 在x轴正半轴和y轴正半轴的平分线处（θ=π/4）添加θ标签
        theta_angle = PI / 4  # 平分线角度
        label_radius = theta_circle_radius * 1.1  # 标签位置半径（稍大于圆）

        # 计算标签位置（平分线方向）
        label_x = label_radius * np.cos(theta_angle)
        label_y = label_radius * np.sin(theta_angle)

        # 创建θ标签
        theta_label = MathTex(r"\theta", font_size=62, color=BLUE)
        theta_label.move_to(np.array([label_x, label_y, 0.01]))  # 放置在平分线上
        self.add_fixed_in_frame_mobjects(theta_label)
        theta_label.shift(RIGHT * 0.75 + DOWN * 0.9)

        theta_label_copy = MathTex(r"\theta", font_size=40, color=BLUE)
        theta_label_copy.move_to(np.array([label_x, label_y, 0.01]))
        theta_label_copy.shift(RIGHT * 0.75 + DOWN * 0.9)  # θ副本

        # 显示圆和标签
        self.play(Create(VGroup(theta_circle, theta_label)), run_time=1.5)
        self.play(Wait(4))
        # self.play(Write(theta_label), run_time=1.5)
        # self.play(Wait(2))

        # 使用ParametricFunction手动创建3D角度弧线（替代Arc3D), 这将创建一个位于y-z平面负y侧的弧线
        arc_radius = 0.75  # 弧线半径
        phi_angle = np.pi / 4  # 角度大小

        # 定义3D弧线的参数方程：从z轴到锥面的角度φ
        def phi_arc_func(t):
            # t从0到1变化，对应角度从0到phi_angle
            angle = t * phi_angle
            # 球面坐标到笛卡尔坐标的转换
            x = 0  # 位于y-z平面，x=0
            y = -arc_radius * np.sin(angle)  # 负y方向确保投影在y轴负半轴
            z = arc_radius * np.cos(angle)
            return np.array([x, y, z])

        # 创建参数化弧线
        phi_arc = ParametricFunction(
            phi_arc_func,
            t_range=[0, 1],
            stroke_color=YELLOW,
            stroke_width=3,
        )

        # 创建φ标签
        phi_label = MathTex(r"\phi", font_size=62, color=YELLOW_C)
        # 计算标签位置（弧线中点略微向外）
        mid_point = phi_arc_func(0.5)
        phi_label.move_to(mid_point + 0.3 * normalize(mid_point))
        phi_label.shift(UP * 1.2 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(phi_label)

        phi_label_copy = MathTex(r"\phi", font_size=40, color=YELLOW_C)
        phi_label_copy.move_to(mid_point + 0.3 * normalize(mid_point))
        phi_label_copy.shift(UP * 1.2 + LEFT * 0.5)  # φ副本

        # 计算弧线末端的切线方向
        t_end = 1.0  # 弧线末端参数
        dt = 0.001  # 微小变化量用于数值求导

        # 计算末端点坐标
        end_point = phi_arc_func(t_end)

        # 数值计算切线向量（导数）
        tangent_vector = (phi_arc_func(t_end) - phi_arc_func(t_end - dt)) / dt
        tangent_normalized = tangent_vector / np.linalg.norm(tangent_vector)  # 归一化

        # 创建3D箭头 (使用Cone)
        arrow_cone = Cone(
            direction=tangent_normalized,
            base_radius=0.1,
            height=0.3,
            fill_color=YELLOW,
            fill_opacity=1,
            stroke_color=YELLOW,
        ).move_to(end_point)

        self.play(Wait(2))
        # self.play(Create(VGroup(phi_arc, arrow_cone)), run_time=2)
        self.play(Create(phi_arc), run_time=1)
        self.play(Create(arrow_cone), run_time=1)
        self.play(Create(phi_label), run_time=1)
        self.play(Wait(2))
        # self.play(Write(phi_label), run_time=1.5)
        # self.play(Wait(2))

        # 选择一个角度创建射线（例如在x-z平面上）
        angle = PI / 2  # 沿x轴方向
        # 定义球半径
        radius = 2.75
        # 定义超出球面的长度比例
        excess_ratio = 1.25  # 超出

        # 计算球面上的点（到达球面的部分）
        x_base = radius * np.sin(np.pi / 4) * np.cos(angle)
        y_base = radius * np.sin(np.pi / 4) * np.sin(angle)
        z_base = radius * np.cos(np.pi / 4)

        # 计算超出球面的点
        x_excess = x_base * excess_ratio
        y_excess = y_base * excess_ratio
        z_excess = z_base * excess_ratio

        # 创建射线的两部分
        # 到达球面的部分（红色）
        ray_to_sphere = Line(
            start=np.array([0, 0, 0]),
            end=np.array([x_base, y_base, z_base]),
            color=RED,
            stroke_width=3,
        )

        # 超过球面的部分（黄色）
        ray_beyond_sphere = DashedLine(
            start=np.array([x_base, y_base, z_base]),
            end=np.array([x_excess, y_excess, z_excess]),
            color=YELLOW,
            stroke_width=3,
            dash_length=0.1,  # 使用虚线区分
        )
        # 计算实线末端的方向向量
        r_direction_vector = np.array([x_base, y_base, z_base]) - np.array([0, 0, 0])
        r_normalized_direction = r_direction_vector / np.linalg.norm(r_direction_vector)
        # 在实线末端添加箭头 (使用Cone)
        r_arrow_cone = Cone(
            direction=r_normalized_direction,
            base_radius=0.15,
            height=0.3,
            fill_color=RED,
            fill_opacity=1,
            stroke_color=RED,
        ).move_to(np.array([x_base, y_base, z_base]))

        r_label = MathTex(r"r", font_size=62, color=RED)
        r_label.next_to(ray_beyond_sphere, RIGHT).shift(RIGHT * 2)
        # r_label.fix_in_frame()
        self.add_fixed_in_frame_mobjects(r_label)

        r_label_copy = MathTex(r"r", font_size=40, color=RED)
        r_label_copy.next_to(ray_beyond_sphere, RIGHT).shift(RIGHT * 2)  # r副本

        # 将两部分组合成一条完整射线
        full_ray = VGroup(ray_to_sphere, ray_beyond_sphere)
        self.play(Wait(2))
        self.play(Create(full_ray), run_time=2)
        self.play(Create(r_arrow_cone), run_time=1)
        self.play(Create(r_label), run_time=2)
        self.play(Wait(2))

        # theta_label_copy = MathTex(r"\theta", font_size=62, color=BLUE)
        # theta_label_copy.move_to(np.array([label_x, label_y, 0.01]))  # 放置在平分线上
        # theta_label_copy.shift(RIGHT * 0.75 + DOWN * 0.9)

        all_3d_objects = VGroup(
            axes,
            labels,
            sphere,
            cone,
            theta_circle,
            arrow_cone,
            theta_label,
            phi_arc,
            phi_label,
            ray_to_sphere,
            ray_beyond_sphere,
            r_arrow_cone,
            r_label,
        )
        # 先缩放（1秒），再移动（1秒）
        self.play(all_3d_objects.animate.scale(0.3), run_time=2.5)
        self.play(Wait(2))
        self.play(
            all_3d_objects.animate.to_edge(DR)
            .shift(RIGHT * 3.0 + IN * 0.05)
            .shift(X_AXIS * 0.75 + Y_AXIS * 0.75),
            run_time=2,
        )
        self.play(Wait(2))
        # self.add_fixed_in_frame_mobjects(theta_label_copy)
        self.add_fixed_in_frame_mobjects(theta_label_copy)
        self.add_fixed_in_frame_mobjects(phi_label_copy)
        self.add_fixed_in_frame_mobjects(r_label_copy)

        theta_label_copy.shift(RIGHT * 4.5 + DOWN * 2.6)
        phi_label_copy.shift(RIGHT * 5.4 + DOWN * 2.85)
        r_label_copy.shift(RIGHT * 4 + DOWN * 3.65)
        self.play(
            Write(VGroup(theta_label_copy, phi_label_copy, r_label_copy)), run_time=2
        )

        # ---------------------------------------------------------------

        txt = Text(
            "解", font="STKaiti", font_size=34, weight="BOLD", color=BLUE
        ).next_to(question, DOWN, aligned_edge=LEFT, buff=0.25)

        # jie_1 = Paragraph(
        #     "如图，上球面和下锥面围成“冰淇淋”型区域Ω. ",
        #     "采用球坐标积分，化重积分为先𝑟次𝜑后𝜃的三次积分",
        #     "按“后积先定限”，依次定𝜃,𝜑,𝑟的上下限。",
        #     # font="SimHei",  # 使用黑体显示中文
        #     gradient=(YELLOW, BLUE),  # 文字渐变色
        #     font_size=26,
        # ).next_to(txt, RIGHT, buff=0.25)

        jie_1_2 = VGroup(
            Text("采用球坐标积分，化重积分为先", font_size=23),
            MathTex(
                r"r",
                font_size=27,
            ),
            Text("次", font_size=23),
            MathTex(
                r"\varphi",
                font_size=27,
            ),
            Text("后", font_size=23),
            MathTex(
                r"\theta",
                font_size=27,
            ),
            Text("的三次积分", font_size=23),
        ).arrange(RIGHT, buff=0.15)
        jie_1_3 = VGroup(
            Text("按“后积先定限”，依次定", font_size=23),
            MathTex(
                r"\theta , \,",
                font_size=27,
            ),
            MathTex(
                r"\varphi , \,",
                font_size=27,
            ),
            MathTex(
                r"r \,",
                font_size=27,
            ),
            Text("的上下限。", font_size=23),
        ).arrange(RIGHT, buff=0.15)
        jie_1 = (
            VGroup(
                Text("如图，上球面和下锥面围成“冰淇淋”型区域Ω.", font_size=23),
                jie_1_2,
                jie_1_3,
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            .next_to(txt, RIGHT, aligned_edge=UP, buff=0.25)
        )

        jie_2 = MathTex(
            r"\Omega' = \Omega = \left\{ (r, \theta, \varphi) \,\big|\, \begin{cases} 0 \leq \theta \leq 2\pi \\ 0 \leq \varphi \leq \frac{\pi}{4} \\ 0 \leq r \leq R \end{cases} \right\}",
            font_size=26,
            color=BLUE,
        ).next_to(jie_1, DOWN, aligned_edge=LEFT, buff=0.2)
        jie_3 = MathTex(
            r"\therefore \, \iiint_{\Omega} (x^2 + y^2 + z^2) \, dx \, dy \, dz",
            font_size=26,
            color=BLUE,
        ).next_to(jie_2, DOWN, aligned_edge=LEFT, buff=0.15)
        jie_4 = (
            MathTex(
                r"= \iiint_{\Omega} \left[ (r\sin\varphi \cos\theta)^2 + (r\sin\varphi \sin\theta)^2 + (r\cos\varphi)^2 \right] \, r^2 \sin\varphi \, dr \, d\varphi \, d\theta",
                font_size=26,
                color=BLUE,
            )
            .next_to(jie_3, DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(RIGHT * 0.2)
        )
        jie_5 = MathTex(
            r"= \int_{0}^{2\pi} d\theta \cdot \int_{0}^{\frac{\pi}{4}} \sin\varphi \, d\varphi \cdot \int_{0}^{R} r^4 \, dr",
            font_size=26,
            color=BLUE,
        ).next_to(jie_4, DOWN, aligned_edge=LEFT, buff=0.25)
        jie_6 = MathTex(
            r"= \frac{1}{5} \pi R^5 (2 - \sqrt{2})",
            font_size=26,
            color=BLUE,
        ).next_to(jie_5, RIGHT, buff=0.15)
        self.add_fixed_in_frame_mobjects(question)
        self.add_fixed_in_frame_mobjects(txt)
        self.add_fixed_in_frame_mobjects(jie_1)
        self.add_fixed_in_frame_mobjects(jie_2)
        self.add_fixed_in_frame_mobjects(jie_3)
        self.add_fixed_in_frame_mobjects(jie_4)
        self.add_fixed_in_frame_mobjects(jie_5)
        self.add_fixed_in_frame_mobjects(jie_6)
        VGroup(question, txt, jie_1, jie_2, jie_3, jie_4, jie_5, jie_6)

        self.play(FadeIn(question), run_time=2)
        self.play(Write(txt), run_time=1)
        self.play(FadeIn(jie_1), run_time=2)
        self.play(Wait(4))
        self.play(Write(jie_2), run_time=3)
        self.play(Wait(4))
        self.play(Write(jie_3), run_time=3)
        self.play(Wait(4))
        self.play(Write(jie_4), run_time=3)
        self.play(Wait(4))
        self.play(Write(jie_5), run_time=3)
        self.play(Wait(4))
        self.play(Write(jie_6), run_time=3)
        self.play(Wait(4))


# # 480p 15
# if __name__ == "__main__":
#     from manim import config

#     config.media_dir = "./media"
#     config.quality = "low_quality"
#     scene = Spherical_Coordinate_System()
#     scene.render()
Spherical_Coordinate_System().render()
