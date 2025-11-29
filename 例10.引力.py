from manim import *
import numpy as np


class Gravity_li_10_Copy(Scene):
    def construct(self):
        # LOGO开始
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
        # LOGO结束

        # ------------------------------
        # 2. 创建坐标系和几何图形元素
        #    用于展示细棒、质点及引力分解
        # ------------------------------
        # 创建坐标轴，设置x和y的范围
        ax = Axes(x_range=(-4, 4), y_range=(0, 5))

        # 创建红色细棒（主棒），设置线宽和颜色
        line1 = Line(start=ax.c2p(-3, 0), end=ax.c2p(3, 0), stroke_width=30, color=RED)
        # 创建黄色小段（代表微元dx）
        line2 = Line(
            start=ax.c2p(1.5, 0), end=ax.c2p(2, 0), stroke_width=30, color=YELLOW
        )
        # 细棒左端标记（-l/2）
        line1_start_text = MathTex(r"-\frac{l}{2}").next_to(ax.c2p(-3, 0), UP, buff=0.5)
        # 细棒右端标记（l/2）
        line1_end_text = MathTex(r"\frac{l}{2}").next_to(ax.c2p(3, 0), UP, buff=0.5)
        # 微元左端标记x
        line2_start_text = (
            MathTex("x").next_to(ax.c2p(1.5, 0), DOWN, buff=0.5).scale(0.8)
        )
        # 微元右端标记x+dx
        line2_end_text = (
            MathTex("x+dx").next_to(ax.c2p(2, 0), DOWN, buff=0.4).scale(0.8)
        ).shift(RIGHT * 0.45)
        # 质点到微元的距离线
        line3 = Line(start=ax.c2p(0, 4), end=ax.c2p(1.5, 0))
        # 水平虚线（用于分解引力的x分量）
        dashedline1 = DashedLine(start=ax.c2p(0.75, 4), end=ax.c2p(0.75, 2))
        # 垂直虚线（用于分解引力的y分量）
        dashedline2 = DashedLine(start=ax.c2p(0, 2), end=ax.c2p(0.75, 2))

        # 创建质点M（红色圆点）
        dot_a = Dot(color=RED, radius=0.15).move_to(ax.c2p(0, 4))
        # 标记质点到细棒的距离a
        dot_a_text1 = MathTex("a").next_to(ax.c2p(0, 4), LEFT).shift(LEFT * 0.1)
        # 标记质点质量M
        dot_a_text2 = MathTex("M").next_to(ax.c2p(0, 4), RIGHT + UP)

        # 引力矢量dF（从质点指向微元）
        arrow_dF = Arrow(start=ax.c2p(0, 4), end=ax.c2p(0.75, 2), color=BLUE, buff=0)
        # 标记dF
        arrow_dF_text = MathTex(r"dF").next_to(ax.c2p(0.75, 2), RIGHT)
        # x方向分力dFx
        arrow_dFx = Arrow(start=ax.c2p(0, 4), end=ax.c2p(0.75, 4), color=BLUE, buff=0)
        # 标记dFx
        arrow_dFx_text = MathTex(r"dF_x").next_to(ax.c2p(0.75, 4), RIGHT)
        # y方向分力dFy
        arrow_dFy = Arrow(start=ax.c2p(0, 4), end=ax.c2p(0, 2), color=BLUE, buff=0)
        # 标记dFy
        arrow_dFy_text = MathTex(r"dF_y").next_to(ax.c2p(0, 2), LEFT)
        # 角度标注弧线
        angle_arc = Angle(
            arrow_dFy, arrow_dF, radius=1.4, color=WHITE, stroke_width=2  # 弧线半径
        )
        # 角度微分标签α
        angle = (
            MathTex(r"\alpha", font_size=60)  # \alpha
            .next_to(
                angle_arc.point_from_proportion(0.5), DOWN, buff=0.1
            )  # 弧线中点位置
            .set_color(WHITE)
        )
        # 将所有几何元素组合并调整位置和大小
        graph1 = (
            VGroup(
                ax,
                line1,
                line2,
                line3,
                dashedline1,
                dashedline2,
                line1_start_text,
                line1_end_text,
                line2_start_text,
                line2_end_text,
                dot_a,
                dot_a_text1,
                dot_a_text2,
                arrow_dF,
                arrow_dFx,
                arrow_dFy,
                arrow_dF_text,
                arrow_dFx_text,
                arrow_dFy_text,
                angle_arc,
                angle,
            )
            .scale(0.6)  # 整体缩小为原来的60%
            .to_edge(RIGHT + DOWN)  # 放置在右下角
        )

        # ------------------------------
        # 3. 创建文本说明元素
        #    包含题目描述、求解步骤和公式
        # ------------------------------
        # 题目描述
        question = (
            VGroup(
                Text(
                    "例  有一根长度为l、线密度为μ的均匀细直棒，在其中垂线上距棒a",
                    font_size=30,
                ),
                Text(
                    "单位处有一质量为m的质点M，试计算该棒对质点M的引力。", font_size=30
                ),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .to_corner(UL, buff=0.5)
        )

        answer1 = Text(
            "解: 建立坐标系如图，使棒位于x轴上，棒的中点为原点，质点M在y轴上。",
            font="SimHei",
            gradient=(YELLOW, BLUE),
            font_size=26,
        ).next_to(
            question, DOWN, aligned_edge=LEFT, buff=0.25
        )  # 位于题目下方
        # 解题步骤2：积分变量说明
        answer2 = (
            VGroup(
                Text(
                    "取x为积分变量，其变化区间为[-l/2,l/2],设[x,x+dx]是[-l/2,l/2]上任一小段,",
                    font_size=26,
                ),
                Text("其质量是μdx,该小段与质点M的距离近似为", font_size=26),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(answer1, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # 距离公式：r=√(a²+x²)
        answer3 = (
            MathTex(
                r"r = \sqrt{a^{2} + x^{2}}",
                font_size=30,
            )
            .next_to(answer2, DOWN)
            .to_edge(RIGHT)
            .shift(LEFT * 4.5)
            .shift(UP * 0.65)
        )
        # 解题步骤3：引力微元公式说明
        answer4 = (
            VGroup(
                Text(
                    "由两质点间的引力公式得，该小段细直棒对质点M的",
                    font_size=26,
                ),
                Text("引力dF的大小为", font_size=26),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(answer2, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # 引力微元公式：ΔF≈G(mμdx)/(a²+x²)
        answer5 = (
            MathTex(r"dF = G \frac{m\mu \, dx}{a^2 + x^2}", font_size=30)
            .next_to(answer4, RIGHT)
            .shift(LEFT * 5.55)
            .shift(DOWN * 0.3)
        )
        # 解题步骤4：y方向分力说明
        answer6 = (
            Text(
                "dF在铅直方向上的分力dFy的近似值为",
                font="SimHei",
                gradient=(YELLOW, BLUE),
                font_size=26,
            )
            .next_to(answer4, DOWN, buff=0.25)
            .to_edge(LEFT)
        )
        # y方向分力公式（含余弦分解）
        answer7 = (
            MathTex(
                r"dF_y = -dF \cdot \cos\alpha = -G\frac{m\mu \, dx}{a^2+x^2} \cdot \frac{a}{\sqrt{a^2+x^2}}",
                font_size=30,
            )
            .next_to(answer6, DOWN, buff=0.25)
            .to_edge(LEFT)
        )
        # 解题步骤5：力元素说明
        answer8 = (
            VGroup(
                Text(
                    "此即是小段细直棒对质点的引力在铅直方向",
                    font_size=24,
                ),
                Text("分力的力元素，即:", font_size=24),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(answer7, DOWN, aligned_edge=LEFT, buff=0.25)
        )

        # 步骤5的副本（用于后续位置变换）
        answer8_copy = (
            VGroup(
                Text(
                    "此即是小段细直棒对质点的引力在铅直方向",
                    font_size=26,
                ),
                Text("分力的力元素，即:", font_size=26),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(question, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # 力元素公式：dFy = -G(amμdx)/(a²+x²)^(3/2)
        answer9 = (
            MathTex(r"dF_y = -G\frac{a m \mu \, dx}{(a^2+x^2)^{3/2}}", font_size=26)
            .next_to(answer8, DOWN, aligned_edge=LEFT, buff=0.25)
            .shift(RIGHT * 3.1)
            .shift(UP * 0.75)
        )
        # 力元素公式副本（用于后续位置变换）
        answer9_COPY = MathTex(
            r"dF_y = -G\frac{a m \mu \, dx}{(a^2+x^2)^{3/2}}", font_size=30
        ).next_to(answer8_copy, DOWN, aligned_edge=LEFT, buff=0.25)
        # 解题步骤6：总引力y分量说明
        answer10 = (
            Text(
                "于是得，引力在铅直方向分力为:",
                font="SimHei",
                font_size=26,
                gradient=(YELLOW, BLUE),
            )
            .next_to(answer9_COPY, DOWN, buff=0.25)
            .to_edge(LEFT)
        )
        # 积分计算结果：Fy = ∫(...)dx = -2Gμl/(a√(4a²+l²))
        answer11 = (
            MathTex(
                r"F_y = \int_{-l/2}^{l/2} -G\frac{a m \mu}{(a^2+x^2)^{3/2}} \, dx = -\frac{2G\mu l}{a\sqrt{4a^2 + l^2}}",
                font_size=30,
            )
            .next_to(answer10, DOWN, buff=0.25)
            .to_edge(LEFT)
        )
        # 解题步骤7：对称性分析（x方向分力为0）
        answer12 = (
            VGroup(
                Text(
                    "由对称性，引力在水平方向分力为:",
                    font_size=26,
                ),
                MathTex(r"F_x = 0", font_size=30),
            )
            .set_color_by_gradient((YELLOW, BLUE))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            .next_to(answer11, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # 解题步骤8：合力F
        answer13 = (
            VGroup(
                Text(
                    "所以, 引力为:",
                    font_size=26,
                ),
                MathTex(
                    r"F = -\frac{2G\mu l}{a\sqrt{4a^2 + l^2}}",
                    font_size=28,
                ),
            )
            .arrange(RIGHT, buff=0.2)
            .next_to(answer12, DOWN, aligned_edge=LEFT, buff=0.25)
        )
        # ------------------------------
        # 4. 动画序列定义
        #    按逻辑顺序展示解题步骤和图形
        # ------------------------------
        # 显示题目，播放8秒
        self.play(Write(question), run_time=4)
        self.wait(7)  # 暂停7秒供阅读

        # 显示坐标系建立说明
        self.play(Write(answer1), run_time=4)
        line1_start_text.shift(RIGHT * 0.3)
        line1_end_text.shift(LEFT * 0.3)
        # 创建基本几何元素（坐标轴、细棒、质点及标记）
        self.play(
            Create(
                VGroup(
                    ax,
                    line1,
                    line1_start_text,
                    line1_end_text,
                    dot_a,
                    dot_a_text1,
                    dot_a_text2,
                )
            ),
            run_time=5,
        )
        self.wait(4)

        # 显示积分变量和距离公式
        self.play(Write(answer2), Write(answer3), run_time=4)
        self.wait(4)

        # 创建微元线段和距离线
        self.play(
            Create(VGroup(line2, line2_start_text, line2_end_text, line3)), run_time=5
        )
        self.wait(4)

        # 显示引力微元公式
        self.play(Write(answer4), Write(answer5), run_time=4)
        self.wait(4)

        # 创建引力分解矢量和辅助虚线
        self.play(
            Create(
                VGroup(
                    arrow_dF,
                    arrow_dF_text,
                    arrow_dFx,
                    arrow_dFx_text,
                    arrow_dFy,
                    arrow_dFy_text,
                    dashedline1,
                    dashedline2,
                    angle_arc,
                    angle,
                )
            ),
            run_time=5,
        )
        self.wait(4)

        # 显示y方向分力说明
        self.play(Write(answer6), run_time=2)
        self.wait(4)
        # 显示分力分解公式
        self.play(Write(answer7), run_time=2)
        self.wait(4)

        # 显示力元素公式
        self.play(Write(answer8), FadeIn(answer9), run_time=4)
        self.wait(4)

        # 移除前面的步骤文本，为后续内容腾出空间
        self.play(
            FadeOut(answer7),
            FadeOut(answer6),
            FadeOut(answer5),
            FadeOut(answer4),
            FadeOut(answer3),
            FadeOut(answer2),
            FadeOut(answer1),
        )
        self.wait(4)

        # 将力元素说明文本移动到上方
        self.play(
            Transform(VGroup(answer8, answer9), VGroup(answer9_COPY, answer8_copy))
        )
        self.wait(4)

        # 显示最终计算结果和对称性分析
        self.play(Write(VGroup(answer10, answer11)), run_time=6)
        self.wait(4)

        self.play(Write(answer12), run_time=3)
        self.wait(4)

        # self.play(Write(answer13), run_time=3)
        # self.wait(5)  # 最后暂停5秒展示最终结果


Gravity_li_10_Copy().render()
