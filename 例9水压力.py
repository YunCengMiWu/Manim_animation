from manim import *
from manim.opengl import *
from manim import MarkupText


class le9_Water_pressure(Scene):
    """
    这是一个演示水压相关概念的场景类
    主要展示了坐标系、椭圆、矩形和一些线段，用于解释水压相关的物理概念
    """

    def construct(self):
        # 1. 创建坐标系
        axes = Axes(
            x_range=[-1.25, 1.25],  # x轴范围
            y_range=[-1, 1],  # y轴范围
            axis_config={"include_numbers": True},  # 显示坐标轴刻度数字
            x_axis_config={"include_tip": False},  # 不显示x轴默认箭头
            y_axis_config={"include_tip": False},  # 不显示y轴默认箭头
        )

        # 自定义x轴箭头（方向向右）
        x_tip = Arrow(
            start=LEFT,  # 箭头起点方向
            end=RIGHT,  # 箭头终点方向（向右）
            tip_length=0.2,  # 箭头尖端长度
            color=axes.x_axis.get_color(),  # 与x轴同色
            stroke_width=2,  # 箭头线宽
        ).move_to(
            axes.x_axis.get_end()
        )  # 将箭头移动到x轴起点位置

        # 自定义y轴箭头（方向向上）
        y_tip = Arrow(
            start=DOWN,  # 箭头起点方向
            end=UP,  # 箭头终点方向（向上）
            tip_length=0.2,  # 箭头尖端长度
            color=axes.y_axis.get_color(),  # 与y轴同色
            stroke_width=2,  # 箭头线宽
        ).move_to(
            axes.y_axis.get_end()
        )  # 将箭头移动到y轴终点位置

        # 创建坐标轴标签
        o1 = Text("O").next_to(axes.c2p(0, 0), LEFT + UP).scale(0.5)  # 原点标签
        y_1 = Text("y").next_to(y_tip, RIGHT).scale(0.5)  # y轴标签
        x_1 = (
            Text("x").next_to(x_tip, UP).scale(0.5).shift(0.5 * RIGHT)
        )  # x轴标签，稍向右偏移

        # 2. 定义椭圆（参数方程）
        a = 1.0  # 半长轴 (长轴总长=2a=2m)
        b = 0.75  # 半短轴 (短轴总长=2b=1.5m)

        ellipse = ParametricFunction(
            # 参数方程：x = a*cos(t), y = b*sin(t)
            # 转换为坐标系实际位置
            lambda t: axes.coords_to_point(a * np.cos(t), b * np.sin(t)),
            t_range=[0, 2 * PI],  # 参数t范围：0到2π（完整椭圆）
            color=BLUE,  # 椭圆颜色
            stroke_width=6,  # 椭圆线宽
        )

        # 3. 生成椭圆内的水平平行线（用于演示水压相关概念）
        # 计算平行线位置（示例取y=-0.3和y=-0.4）
        y_values = [-0.4, -0.3]  # 间隔0.1m的两个y坐标

        # 生成平行线段组
        lines = VGroup()
        for y in y_values:
            # 根据椭圆方程 x²/a² + y²/b² = 1 计算对应y值的x坐标
            x = a * np.sqrt(1 - (y / b) ** 2)  # 解椭圆方程得到x值

            # 创建水平线段（从-x到x，同一y值）
            line = Line(
                start=axes.coords_to_point(-x, y),  # 线段起点
                end=axes.coords_to_point(x, y),  # 线段终点
                color=RED,  # 线段颜色
                stroke_width=6,  # 线段宽度
            )
            lines.add(line)  # 将线段添加到线段组

        # 5. 手动生成y轴方向的黎曼矩形（宽度对应y=-0.3处）
        y_min, y_max = -0.4, -0.3  # 积分区间（y从-0.4到-0.3）
        iterations = 1  # 矩形数量
        dy = (y_max - y_min) / iterations  # 矩形高度（0.1）
        colors = color_gradient([PURPLE, GREEN], 20)  # 矩形渐变颜色

        riemann_rects = VGroup()  # 存储所有矩形
        for i in range(iterations):
            # 当前区间的起始y值（此处为-0.4）
            y = y_min + i * dy
            # 区间的结束y值（此处为-0.3，即目标y值）
            y_target = y + dy  # 关键：用y+dy（-0.3）计算宽度

            # 根据椭圆方程计算y_target（-0.3）处的x值（椭圆宽度）
            x = a * np.sqrt(1 - (y_target / b) ** 2)  # 右半椭圆的x值

            # 矩形的左下角（-x, y）和右上角（x, y_target）
            left_bottom = axes.coords_to_point(0, y)
            right_top = axes.coords_to_point(x, y_target)

            # 创建矩形
            rect = Rectangle(
                width=right_top[0] - left_bottom[0],  # 宽度=2x（y=-0.3处的宽度）
                height=right_top[1] - left_bottom[1],  # 高度=dy（0.1）
                fill_opacity=0.75,
                color=colors[i * len(colors) // iterations],
                stroke_width=1,
                stroke_color=WHITE,
            )
            # 移动到矩形中心位置
            rect.move_to(
                [
                    (left_bottom[0] + right_top[0]) / 2,
                    (left_bottom[1] + right_top[1]) / 2,
                    0,
                ]
            )
            riemann_rects.add(rect)

        # 为线段添加标签
        x_d = Text("y+dy").next_to(axes.c2p(0, -0.3), 0.5 * RIGHT + 0.5 * UP).scale(0.5)
        x_dx = Text("y").next_to(axes.c2p(0, -0.4), 0.5 * RIGHT + 0.5 * DOWN).scale(0.5)

        # 4. 组合所有元素并调整位置
        # 将所有元素组合成一个组，缩小并移动到右下角
        p = (
            VGroup(
                x_d,
                x_dx,
                x_1,
                y_1,
                o1,
                axes,
                x_tip,
                y_tip,
                ellipse,
                riemann_rects,
                lines,
            )
            .scale(0.55)  # 整体缩小到0.5倍
            .to_edge(RIGHT + DOWN)  # 移动到右下角
        )

        problem = VGroup(
            Text(
                "例  有一椭圆形闸门，长轴为2m，短轴为1.5m，短轴与水平面垂直，阀门顶",
                font_size=27,
            ),
            Text("与水面相齐，试求闸门所受的压力（ɡ＝9.8m/s²）", font_size=27),
        ).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        )  # buff 就是行距
        problem.set_color_by_gradient(BLUE, RED).to_edge(LEFT + UP)

        solution1_1 = (
            Text("解：")
            .set_color_by_gradient((BLUE))
            .scale(0.45)
            .next_to(problem, DOWN)
            .to_edge(LEFT)
        )
        solution1_2 = (
            Text("选取如图所示坐标系，取y为积分变量，变化区间为[-0.75, 0.75]\n")
            .set_color_by_gradient((BLUE))
            .scale(0.45)
            .next_to(solution1_1, RIGHT)
        )
        solution1 = (
            VGroup(solution1_1, solution1_2)
            .arrange(RIGHT, buff=0.2)
            .set_color_by_gradient(BLUE)
            .next_to(problem, DOWN, aligned_edge=LEFT)
        )
        s2 = (
            Text("右半椭圆的方程为")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.45)
            .next_to(solution1, DOWN)
            .to_edge(LEFT)
        )

        s3 = (
            MathTex(r"x = \frac{1}{0.75} \sqrt{0.75^2 - y^2}")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.5)
            .next_to(s2, RIGHT)
        )

        s4 = (
            Text(",闸门是关于y轴对称，两侧压力相等.")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.45)
            .next_to(s3, RIGHT)
        )

        s5 = (
            Text("右半闸门在水深y+0.75处，高为dy的右半横条面积为")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.45)
            .next_to(s2, DOWN, buff=0.35)
            .to_edge(LEFT)
        )

        s6 = (
            MathTex(r"\frac{\sqrt{0.75^2 - y^2}}{0.75}dy")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.5)
            .next_to(s5, RIGHT)
        )

        s7 = (
            Text("则右半横条所受压力(压力元素)为")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.45)
            .next_to(s5, DOWN, buff=0.25)
            .to_edge(LEFT)
        )

        s8 = (
            MathTex(
                r"dP_{1} = \rho g(y + 0.75) \cdot \frac{\sqrt{0.75^2 - y^2}}{0.75}\,dy"
            )
            .set_color_by_gradient((BLUE, RED))
            .scale(0.5)
            .next_to(s7, DOWN)
            .to_edge(LEFT)
        )

        s9 = (
            Text("故闸门所受的压力元素为:")
            .set_color_by_gradient((BLUE, RED))
            .scale(0.45)
            # .next_to(s8, DOWN)
            .to_edge(LEFT)
        )

        # 多行公式
        line1_1 = MathTex(r"dP").scale(0.5)
        line1_2 = (
            MathTex(r"&= 2dP_1").scale(0.5).next_to(line1_1, RIGHT, aligned_edge=LEFT)
        )
        line1 = (
            VGroup(line1_1, line1_2)
            .next_to(s9, DOWN, aligned_edge=LEFT)
            .set_color_by_gradient(RED)
        )
        line2 = (
            MathTex(
                r"&= 2 \cdot \rho g (y + 0.75) \cdot \frac{\sqrt{0.75^2 - y^2}}{0.75}\,dy",
                color=RED,
            )
            .scale(0.5)
            .next_to(line1_2, DOWN, aligned_edge=LEFT)
        )

        line3_2 = (
            MathTex(
                r"&= \frac{2 \times 1 \times 9.8 \times 1000}{0.75} \int_{-0.75}^{0.75} (y + 0.75) \cdot \sqrt{0.75^2 - y^2} \, dy"
            )
            .scale(0.5)
            .next_to(line2, DOWN, aligned_edge=LEFT)
        )
        line3_1 = MathTex(r"p ").scale(0.5).next_to(line3_2, LEFT)
        line3 = VGroup(line3_1, line3_2)
        line4 = (
            MathTex(
                r"&= 39.2 \times 1000 \cdot \int_{0}^{0.75} \sqrt{0.75^2 - y^2} \, dy"
            )
            .scale(0.5)
            .next_to(line3_2, DOWN, aligned_edge=LEFT)
        )
        line5 = (
            MathTex(r"&\approx 17.31 \, \mathrm{(kN)}")
            .scale(0.5)
            .next_to(line4, DOWN, aligned_edge=LEFT)
        )

        self.play(Write(problem), run_time=2)

        self.wait(3)

        self.play(Create(p), run_time=5)  # 作图

        self.wait(2.5)

        self.play(Write(solution1), run_time=3.5)
        self.wait(5)
        self.play(Write(VGroup(s2, s3, s4)), run_time=4)
        self.wait(9)
        self.play(Write(VGroup(s5, s6)), run_time=4)
        self.wait(7)
        self.play(Write(VGroup(s7, s8)), run_time=3.5)
        self.wait(4)

        self.play(FadeOut(solution1_2, s2, s3, s4, s5, s6))
        # 2. 带动画的位置移动（可设置时间）
        group1 = VGroup(s7, s8)
        group1.generate_target()  # 创建目标状态
        group1.target.next_to(
            solution1_1, RIGHT, aligned_edge=UP, buff=0.35
        )  # 定义目标位置
        self.play(MoveToTarget(group1), run_time=2)  # 2秒内移动到目标位置
        self.wait(0.5)

        s9.next_to(s8, DOWN, aligned_edge=LEFT)
        line1.next_to(s9, DOWN, aligned_edge=LEFT)
        line2.next_to(line1_2, DOWN, aligned_edge=LEFT)
        line3_2.next_to(line2, DOWN, aligned_edge=LEFT)
        line3_1.next_to(line3_2, LEFT)
        line3 = VGroup(line3_1, line3_2)
        line4.next_to(line3_2, DOWN, aligned_edge=LEFT)
        line5.next_to(line4, DOWN, aligned_edge=LEFT)

        self.play(Write(s9), run_time=1.5)
        self.play(Write(line1), run_time=3)
        self.play(Write(line2), run_time=2)
        self.wait(6)
        self.play(Write(line3), run_time=3)
        self.wait(12)
        self.play(Write(line4), run_time=3)
        self.wait(4.5)
        self.play(Write(line5), run_time=3)
        self.wait(4.5)


le9_Water_pressure().render()
