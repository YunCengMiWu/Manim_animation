from manim import *
import numpy as np


class CQU_logo(ThreeDScene):
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
                VGroup(
                    Text("例  求球体", font_size=33),
                    MathTex(r"x^2 + y^2 + z^2 \leq 4a^2", font_size=38),
                    Text("被圆柱面", font_size=32),
                    MathTex(r"x^2 + y^2 = 2ax \ (a > 0)", font_size=38),
                ).arrange(RIGHT, buff=0.15),
                Text("所截得的(含在柱面内的)立体的体积.", font_size=30),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .set_color_by_gradient((YELLOW, BLUE))
            .to_corner(UL, buff=0.5)
        )
        self.play(Write(question), run_time=4)
        self.wait(4)
        self.play(FadeOut(question), run_time=3)

        # 设置3D视角
        # phi是摄像机与z轴的夹角（75度），theta是摄像机在xy平面上的旋转角度（-55度）
        self.set_camera_orientation(phi=75 * DEGREES, theta=-55 * DEGREES)

        # 创建三维坐标系
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],  # x轴范围从-2到2，刻度间隔1
            y_range=[-1.5, 1.5, 1],  # y轴范围从-2到2，刻度间隔1
            z_range=[-1.5, 1.5, 1],  # z轴范围从-2到2，刻度间隔1
            axis_config={"color": WHITE},  # 坐标轴颜色为白色
            # x_length=3,  # x轴长度
            # y_length=3,  # y轴长度
            # z_length=3,  # z轴长度
        )
        labels = axes.get_axis_labels(
            MathTex(r"x", font_size=62, color=WHITE),
            MathTex(r"y", font_size=62, color=WHITE),
            MathTex(r"z", font_size=62, color=WHITE),
        )

        # 创建一个参数曲面（这里创建的是球面）
        sphere = Surface(
            # 使用lambda函数定义参数曲面的坐标
            # u和v是参数，u对应经度，v对应纬度
            lambda u, v: np.array(
                [
                    2 * np.cos(u) * np.sin(v),  # x坐标 = cos(u)*sin(v)
                    2 * np.sin(u) * np.sin(v),  # y坐标 = sin(u)*sin(v)
                    2 * np.cos(v),  # z坐标 = cos(v)
                ]
            ),
            fill_opacity=0.3,
            u_range=[0, 2 * PI],  # u参数范围：0到2π（完整的经度范围）
            v_range=[0, PI],  # v参数范围：0到π（从北极到南极）
            resolution=(15, 30),  # 曲面网格的分辨率（u方向15份，v方向30份）
            color=BLUE,  # 曲面颜色为蓝色
        )

        # 2. 绘制圆柱面：x² + y² = 2ax → (x-1)² + y² = 1（a=1）
        cylinder = Surface(
            lambda u, v: np.array(
                [
                    1 + np.cos(u),  # x = a + a cosu（a=1）
                    np.sin(u),  # y = a sinu
                    v,  # z 从 -2 到 2（球体半径 2）
                ]
            ),
            stroke_color=YELLOW,
            u_range=[0, 2 * np.pi],
            v_range=[-2.75, 2.75],
            fill_opacity=0.3,
        )

        self.begin_ambient_camera_rotation(rate=0.5)
        self.play(Create(VGroup(axes, labels)), run_time=1.6)
        self.play(Create(sphere), run_time=3)  # 将球面添加到场景中
        self.play(Create(cylinder), run_time=3)  # 将柱面添加到场景中
        self.wait(4)

        self.stop_ambient_camera_rotation()

        self.wait(4)

        # 将所有3D元素组合成一个组
        all_3d_objects = VGroup(
            axes,
            labels,
            sphere,
            cylinder,
        )

        self.play(FadeOut(all_3d_objects))

        # 设置3D视角
        # phi是摄像机与z轴的夹角（75度），theta是摄像机在xy平面上的旋转角度（-55度）
        self.set_camera_orientation(phi=75 * DEGREES, theta=-55 * DEGREES)

        # 创建三维坐标系
        axes_1 = ThreeDAxes(
            x_range=[-2, 2, 1],  # x轴范围从-2到2，刻度间隔1
            y_range=[-1.5, 1.5, 1],  # y轴范围从-2到2，刻度间隔1
            z_range=[-1.5, 1.5, 1],  # z轴范围从-2到2，刻度间隔1
            axis_config={"color": WHITE},  # 坐标轴颜色为白色
        )
        labels_1 = axes_1.get_axis_labels(
            MathTex(r"x", font_size=62, color=WHITE),
            MathTex(r"y", font_size=62, color=WHITE),
            MathTex(r"z", font_size=62, color=WHITE),
        )

        sphere_1 = Surface(
            lambda u, v: np.array(
                [
                    2 * np.cos(u) * np.sin(v),
                    2 * np.sin(u) * np.sin(v),
                    2 * np.cos(v),
                ]
            ),
            fill_opacity=0.3,
            u_range=[0, PI / 2],  # 扩展边界
            v_range=[0, PI / 2],  # 扩展边界
            resolution=(67, 60),  # 更高分辨率
            color=BLUE,
        )

        cylinder_1 = Surface(
            lambda u, v: np.array(
                [  # 参数方程定义曲面
                    1 + np.cos(u),  # x = 1 + cos(u)
                    np.sin(u),  # y = sin(u)
                    v,  # z = v (高度)
                ]
            ),
            stroke_color=YELLOW,  # 网格线颜色为黄色
            u_range=[0, PI],  # u参数范围：0到π（前半圆柱）
            v_range=[0, 2.75],  # v参数范围：0到2.75（高度）
            fill_opacity=0.3,  # 填充透明度30%
            resolution=(67, 70),
        )
        self.play(Create(VGroup(axes_1, labels_1)), run_time=1.6)
        self.play(Create(sphere_1), run_time=3)  # 将球面添加到场景中
        self.play(Create(cylinder_1), run_time=3)  # 将柱面添加到场景中

        # 投影区域D------------------
        # 定义圆柱体的底面半圆面（z=0处）
        # 使用参数方程创建一个填充的半圆面
        cylinder_1_base_surface = Surface(
            lambda u, v: np.array(
                [
                    1 + v * np.cos(u),  # x坐标：从圆心(1,0,0)向外扩展的半圆
                    v * np.sin(u),  # y坐标
                    0,  # z=0，底面
                ]
            ),
            u_range=[0, PI],  # u范围0到π，形成半圆
            v_range=[0, 1],  # v范围0到1，从圆心扩展到半径1
            color=RED,  # 用醒目的红色突出显示
            fill_opacity=0.7,  # 较高的不透明度使其突出
            stroke_color=WHITE,  # 白色边界线增加对比度
            stroke_width=2,  # 稍粗的边界线
        )

        # 创建半圆面的强调边框（可选，增强视觉效果）
        base_border = ParametricFunction(
            lambda u: np.array(
                [
                    1 + np.cos(u),  # x坐标
                    np.sin(u),  # y坐标
                    0,  # z=0
                ]
            ),
            t_range=[0, PI],
            color=YELLOW,
            stroke_width=4,
        )

        # 先显示底面半圆面，使用淡入效果
        self.play(
            Create(cylinder_1_base_surface),
            run_time=2,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # 然后显示边框，使用从一点扩展的动画
        self.play(
            GrowFromPoint(base_border, point=[1, 0, 0]), run_time=1.5  # 从圆心开始生长
        )

        # 添加脉动效果进一步强调
        for _ in range(2):
            self.play(
                cylinder_1_base_surface.animate.set_fill_opacity(0.9),
                cylinder_1_base_surface.animate.scale(1.02),
                run_time=0.5,
            )
            self.play(
                cylinder_1_base_surface.animate.set_fill_opacity(0.7),
                cylinder_1_base_surface.animate.scale(1 / 1.02),
                run_time=0.5,
            )

        # --------------
        # 相交区域可视化
        # --------------
        # 1. 计算交线方程（联立球体和圆柱体方程推导）
        # 球体：x² + y² + z² = 4
        # 圆柱体：(x-1)² + y² = 1 → x² + y² = 2x
        # 联立得：z² = 4 - 2x → z = 2sin(u/2)（第一卦限内取正值）
        intersection_1_curve = ParametricFunction(
            lambda u: np.array(
                [
                    1 + np.cos(u),  # x坐标（来自圆柱体参数）
                    np.sin(u),  # y坐标（来自圆柱体参数）
                    2 * np.sin(u / 2),  # z坐标（联立方程推导结果）
                ]
            ),
            t_range=[0, PI],  # u∈[0,π]（第一卦限内）
            color=GREEN,  # 交线用绿色突出
            stroke_width=4,
        )

        # 2. 相交区域曲面（圆柱体在球体内的部分）
        # 圆柱体高度被球体截断，z上限为2sin(u/2)
        intersection_1_surface = Surface(
            lambda u, v: np.array(
                [
                    1 + np.cos(u),  # x坐标
                    np.sin(u),  # y坐标
                    v * 2 * np.sin(u / 2),  # z坐标（0到交线高度）
                ]
            ),
            u_range=[0, PI],  # 同圆柱体u范围
            v_range=[0, 1],  # v∈[0,1]控制z方向高度
            stroke_color=GREEN,  # 相交区域用绿色
            fill_opacity=0.6,  # 较高不透明度突出显示
            stroke_width=1,
            resolution=(67, 40),
        )

        self.play(Create(intersection_1_curve), run_time=2)  # 先显示交线
        self.play(Create(intersection_1_surface), run_time=2)  # 再显示相交区域
        self.wait(2)

        # 将所有3D元素组合成一个组
        all_3d_objects_1 = VGroup(
            axes_1,
            labels_1,
            sphere_1,
            cylinder_1,
            cylinder_1_base_surface,
            base_border,
            intersection_1_curve,
            intersection_1_surface,
        )

        # 先缩放（1秒），再移动（1秒）
        self.play(all_3d_objects_1.animate.scale(0.5), run_time=1)
        self.play(
            all_3d_objects_1.animate.to_edge(RIGHT + DOWN, buff=0.25).shift(
                DOWN + RIGHT * 0.1
            ),
            run_time=1,
        )
        # # 2. 缩放+移动动画（核心修改：添加带时间的移动效果）
        # self.play(
        #     all_3d_objects.animate.scale(0.5).to_edge(RIGHT + DOWN, buff=1),
        #     run_time=2  # 这里设置移动和缩放的总时间（单位：秒）
        # )
        # 相机旋转
        self.move_camera(theta=self.camera.theta - PI / 6, run_time=3)
        self.play(Wait(4))

        # 解题步骤---------
        jie_1 = VGroup(
            Text("解: 设", font_size=26),
            MathTex(
                r"\begin{cases} x^2 + y^2 + z^2 \leq 4a^2 \\ x^2 + y^2 = 2ax \end{cases} \Rightarrow D = \left\{ (x,y) \ \middle| \ \begin{array}{l} x^2 + y^2 \leq 2ax \\ y \geq 0 \end{array} \right\}",
                font_size=30,
            ),
        )

        jie_2 = MathTex(
            r"\Rightarrow D = D' = \left\{ (\rho, \theta) \ \middle| \ 0 \leq \theta \leq \frac{\pi}{2}, \ 0 \leq \rho \leq 2a \cos\theta \right\}",
            font_size=30,
            color=((YELLOW, BLUE)),
        )

        # 公式6
        jie_3_txt = Text("由对称性可知:", color=WHITE, font_size=26)

        # 计算积分
        jie_4 = MathTex(
            r"V &= 4 \iint_D \sqrt{4a^2 - x^2 - y^2} \, dx \, dy \\"
            r"&= 4 \iint_D \sqrt{4a^2 - \rho^2} \, \rho \, d\rho \, d\theta \\"  # 增加 10pt 间距
            r"&= 4 \int_0^{\frac{\pi}{2}} d\theta \int_0^{2a \cos\theta} \rho \sqrt{4a^2 - \rho^2} \, d\rho \\"  # 默认间距
            r"&= \frac{32}{3} a^3 \int_0^{\frac{\pi}{2}} (1 - \sin^3\theta) \, d\theta = \frac{32}{3} a^3 \left( \frac{\pi}{2} - \frac{2}{3} \right) \\",
            font_size=28,
            color=((YELLOW, BLUE)),
        )

        # 添加动画
        self.add_fixed_in_frame_mobjects(question)

        self.add_fixed_in_frame_mobjects(jie_1)
        jie_1.arrange(RIGHT, buff=0.15).set_color_by_gradient((YELLOW, BLUE)).next_to(
            question, DOWN, aligned_edge=LEFT, buff=0.35
        )
        self.add_fixed_in_frame_mobjects(jie_2)
        jie_2.next_to(jie_1, DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 0.6)
        self.add_fixed_in_frame_mobjects(jie_3_txt)
        jie_3_txt.next_to(jie_2, DOWN, aligned_edge=LEFT, buff=0.15).shift(LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(jie_4)
        jie_4.next_to(jie_3_txt, DOWN, aligned_edge=LEFT, buff=0.25)

        self.play(FadeIn(question), run_time=3.5)
        self.wait(3)
        self.play(Write(jie_1), run_time=4)
        self.wait(4)
        self.play(Write(jie_2), run_time=3)
        self.wait(4)
        self.play(Write(jie_3_txt), run_time=1.5)
        self.wait(4)
        self.play(Write(jie_4), run_time=12)
        self.wait(4)


CQU_logo().render()

# # 720p 30
# if __name__ == "__main__":
#     from manim import config

#     # 720p分辨率配置（1280×720）
#     config.pixel_width = 1280
#     config.pixel_height = 720
#     # 30帧/秒帧率
#     config.frame_rate = 30
#     # 输出目录和质量
#     config.media_dir = "./media"
#     config.quality = "medium_quality"  # 匹配720p的中等质量

#     scene = CQU_logo()
#     scene.render()
