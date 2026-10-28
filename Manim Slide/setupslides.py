from manim import *

from manim_slides import Slide


class Setup(Slide):

    def construct(self):

        title = MathTex(r"(a+b)^2")

        equation = MathTex(r"= a^2+2ab+b^2")


        self.play(Write(title))

        self.next_slide()


        self.play(title.animate.shift(UP * 3))

        self.play(title.animate.shift(LEFT * 2))

        equation.next_to(title, RIGHT, buff=0.3)

        self.next_slide()


        self.play(Write(equation))

        self.next_slide()


        #Variable

        db = ValueTracker(2.5)  #Changable Variable

        da = ValueTracker(1.5)  #Changable Variable Too

        separate = ValueTracker(0)  #Controls separation


        #Function

        def a():
            return da.get_value()


        def b():
            return db.get_value()


        def side():
            return a() + b()


        def left():
            return -side()/2  #x-coordinates of left edge


        def bottom():
            return -side()/2  #y-coordinates of left edge


        def cut():
            return left() + a()


        # LERP
        def move(start, end):
            t = separate.get_value()
            return start * (1 - t) + end * t
        
        # Vertex LERP
        def vertex(start, end, x_offset, y_offset):
            return move(start(), end()) + x_offset() + y_offset()


        #Square

        # Big outer square = BLUE
        square = always_redraw(
            lambda: Square(
                side_length=side(),
                color=BLUE
            )
        )


        #Line

                # Vertices


        # b^2 = BLUE

        b2_top_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + UP * a()/2,
                    lambda: LEFT * (side() - b()/2),
                    lambda: LEFT * b()/2,
                    lambda: UP * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        b2_top_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + UP * a()/2,
                    lambda: LEFT * (side() - b()/2),
                    lambda: RIGHT * b()/2,
                    lambda: UP * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        b2_bottom_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + UP * a()/2,
                    lambda: LEFT * (side() - b()/2),
                    lambda: LEFT * b()/2,
                    lambda: DOWN * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        b2_bottom_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + UP * a()/2,
                    lambda: LEFT * (side() - b()/2),
                    lambda: RIGHT * b()/2,
                    lambda: DOWN * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )


        # ab = PURPLE

        ab1_top_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + UP * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: UP * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab1_top_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + UP * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: RIGHT * a()/2,
                    lambda: UP * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab1_bottom_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + UP * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: DOWN * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab1_bottom_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + UP * a()/2,
                    lambda: LEFT * a()/2,
                    lambda: RIGHT * a()/2,
                    lambda: DOWN * b()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )


        # ab = PURPLE

        ab2_top_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + DOWN * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: LEFT * b()/2,
                    lambda: UP * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab2_top_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + DOWN * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: UP * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab2_bottom_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + DOWN * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: LEFT * b()/2,
                    lambda: DOWN * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        ab2_bottom_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: RIGHT * a()/2 + DOWN * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: RIGHT * b()/2,
                    lambda: DOWN * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )


        # a^2 = RED

        a2_top_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + DOWN * b()/2,
                    lambda: RIGHT * (side() - a()/2),
                    lambda: LEFT * a()/2,
                    lambda: UP * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        a2_top_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + DOWN * b()/2,
                    lambda: RIGHT * (side() - a()/2),
                    lambda: RIGHT * a()/2,
                    lambda: UP * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        a2_bottom_left = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + DOWN * b()/2,
                    lambda: RIGHT * (side() - a()/2),
                    lambda: LEFT * a()/2,
                    lambda: DOWN * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )

        a2_bottom_right = always_redraw(
            lambda: Dot(
                vertex(
                    lambda: LEFT * b()/2 + DOWN * b()/2,
                    lambda: RIGHT * (side() - a()/2),
                    lambda: RIGHT * a()/2,
                    lambda: DOWN * a()/2
                ),
                radius=0.06,
                color=WHITE
            )
        )


        vertices = VGroup(
            b2_top_left,
            b2_top_right,
            b2_bottom_left,
            b2_bottom_right,

            ab1_top_left,
            ab1_top_right,
            ab1_bottom_left,
            ab1_bottom_right,

            ab2_top_left,
            ab2_top_right,
            ab2_bottom_left,
            ab2_bottom_right,

            a2_top_left,
            a2_top_right,
            a2_bottom_left,
            a2_bottom_right
        )
        
                # Moving Lines
        #
        # These lines are attached to the moving vertices.
        # Therefore, when separate changes, the lines move
        # exactly with each colored shape.


        # b^2 = BLUE

        b2_top_line = always_redraw(
            lambda: Line(
                b2_top_left.get_center(),
                b2_top_right.get_center(),
                color=BLUE
            )
        )

        b2_right_line = always_redraw(
            lambda: Line(
                b2_top_right.get_center(),
                b2_bottom_right.get_center(),
                color=BLUE
            )
        )

        b2_bottom_line = always_redraw(
            lambda: Line(
                b2_bottom_right.get_center(),
                b2_bottom_left.get_center(),
                color=BLUE
            )
        )

        b2_left_line = always_redraw(
            lambda: Line(
                b2_bottom_left.get_center(),
                b2_top_left.get_center(),
                color=BLUE
            )
        )


        # ab = PURPLE

        ab1_top_line = always_redraw(
            lambda: Line(
                ab1_top_left.get_center(),
                ab1_top_right.get_center(),
                color=PURPLE
            )
        )

        ab1_right_line = always_redraw(
            lambda: Line(
                ab1_top_right.get_center(),
                ab1_bottom_right.get_center(),
                color=PURPLE
            )
        )

        ab1_bottom_line = always_redraw(
            lambda: Line(
                ab1_bottom_right.get_center(),
                ab1_bottom_left.get_center(),
                color=PURPLE
            )
        )

        ab1_left_line = always_redraw(
            lambda: Line(
                ab1_bottom_left.get_center(),
                ab1_top_left.get_center(),
                color=PURPLE
            )
        )


        # ab = PURPLE

        ab2_top_line = always_redraw(
            lambda: Line(
                ab2_top_left.get_center(),
                ab2_top_right.get_center(),
                color=PURPLE
            )
        )

        ab2_right_line = always_redraw(
            lambda: Line(
                ab2_top_right.get_center(),
                ab2_bottom_right.get_center(),
                color=PURPLE
            )
        )

        ab2_bottom_line = always_redraw(
            lambda: Line(
                ab2_bottom_right.get_center(),
                ab2_bottom_left.get_center(),
                color=PURPLE
            )
        )

        ab2_left_line = always_redraw(
            lambda: Line(
                ab2_bottom_left.get_center(),
                ab2_top_left.get_center(),
                color=PURPLE
            )
        )


        # a^2 = RED

        a2_top_line = always_redraw(
            lambda: Line(
                a2_top_left.get_center(),
                a2_top_right.get_center(),
                color=RED
            )
        )

        a2_right_line = always_redraw(
            lambda: Line(
                a2_top_right.get_center(),
                a2_bottom_right.get_center(),
                color=RED
            )
        )

        a2_bottom_line = always_redraw(
            lambda: Line(
                a2_bottom_right.get_center(),
                a2_bottom_left.get_center(),
                color=RED
            )
        )

        a2_left_line = always_redraw(
            lambda: Line(
                a2_bottom_left.get_center(),
                a2_top_left.get_center(),
                color=RED
            )
        )


        moving_lines = VGroup(

            # b^2
            b2_top_line,
            b2_right_line,
            b2_bottom_line,
            b2_left_line,

            # ab 1
            ab1_top_line,
            ab1_right_line,
            ab1_bottom_line,
            ab1_left_line,

            # ab 2
            ab2_top_line,
            ab2_right_line,
            ab2_bottom_line,
            ab2_left_line,

            # a^2
            a2_top_line,
            a2_right_line,
            a2_bottom_line,
            a2_left_line
        )
        
                # Moving Labels
               # Moving Labels
        #
        # Each label follows the side of its shape.
        # b^2 gets b and b.
        # a^2 gets a and a.


        # b^2 = BLUE

        a2_bottom_label = always_redraw(
            lambda: MathTex("a").move_to(
                (b2_top_left.get_center() + b2_top_right.get_center()) / 2
                + UP * 0.25
            )
        )

        a2_right_label = always_redraw(
            lambda: MathTex("a").move_to(
                (b2_top_left.get_center() + b2_bottom_left.get_center()) / 2
                + LEFT * 0.25
            )
        )


        # ab = PURPLE

        ab1_top_label = always_redraw(
            lambda: MathTex("b").move_to(
                (ab1_top_left.get_center() + ab1_top_right.get_center()) / 2
                + UP * 0.25
            )
        )

        ab1_left_label = always_redraw(
            lambda: MathTex("a").move_to(
                (ab1_top_left.get_center() + ab1_bottom_left.get_center()) / 2
                + LEFT * 0.25
            )
        )


        # ab = PURPLE

        ab2_bottom_label = always_redraw(
            lambda: MathTex("a").move_to(
                (ab2_bottom_left.get_center() + ab2_bottom_right.get_center()) / 2
                + DOWN * 0.25
            )
        )

        ab2_right_label = always_redraw(
            lambda: MathTex("b").move_to(
                (ab2_top_right.get_center() + ab2_bottom_right.get_center()) / 2
                + RIGHT * 0.25
            )
        )


        # a^2 = RED

        b2_top_label = always_redraw(
            lambda: MathTex("b").move_to(
                (a2_bottom_left.get_center() + a2_bottom_right.get_center()) / 2
                + DOWN * 0.25
            )
        )

        b2_left_label = always_redraw(
            lambda: MathTex("b").move_to(
                (a2_top_right.get_center() + a2_bottom_right.get_center()) / 2
                + RIGHT * 0.25
            )
        )


        moving_labels = VGroup(

            # b^2
            b2_top_label,
            b2_left_label,

            # ab 1
            ab1_top_label,
            ab1_left_label,

            # ab 2
            ab2_bottom_label,
            ab2_right_label,

            # a^2
            a2_bottom_label,
            a2_right_label
        )

        self.play(Create(square))


        

        
        self.next_slide()


        #Filled Areas


        # b^2 = BLUE

        b_square = always_redraw(
            lambda: Square(
                side_length=a(),
                fill_color=BLUE,
                fill_opacity=0.5,
                stroke_opacity=0
            ).move_to(
                move(

                    # Original position = bottom-left
                    LEFT * b()/2 + DOWN * b()/2,

                    # Final position = RIGHT
                    RIGHT * (b() + a()/2)

                )
            )
        )


        # ab = PURPLE

        ab_top = always_redraw(
            lambda: Rectangle(
                width=a(),
                height=b(),
                fill_color=PURPLE,
                fill_opacity=0.5,
                stroke_opacity=0
            ).move_to(
                move(

                    # Original position = top-left
                    LEFT * b()/2 + UP * a()/2,

                    # Final position = second from LEFT
                    LEFT * (side() - b() - a()/2)

                )
            )
        )


        # ab = PURPLE

        ab_bottom = always_redraw(
            lambda: Rectangle(
                width=b(),
                height=a(),
                fill_color=PURPLE,
                fill_opacity=0.5,
                stroke_opacity=0
            ).move_to(
                move(

                    # Original position = bottom-right
                    RIGHT * a()/2 + DOWN * b()/2,

                    # Final position = third from LEFT
                    RIGHT * b()/2

                )
            )
        )


        # a^2 = RED

        a_square = always_redraw(
            lambda: Square(
                side_length=b(),
                fill_color=RED,
                fill_opacity=0.5,
                stroke_opacity=0
            ).move_to(
                move(

                    # Original position = top-right
                    RIGHT * a()/2 + UP * a()/2,

                    # Final position = LEFT
                    LEFT * (side() - b()/2)

                )
            )
        )




        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6
        )


        #self.add(plane)


        self.next_slide()


        self.play(Create(vertices))


        self.play(
            Create(a_square),
            Create(b_square),
            Create(ab_top),
            Create(ab_bottom)
        )


        self.play(
            Write(moving_labels),
            Create(moving_lines)
        )


        self.next_slide()


        self.play(
            da.animate.set_value(1.5),
            db.animate.set_value(2.5),
            run_time=2
        )


        self.play(
            da.animate.set_value(1),
            db.animate.set_value(3),
            run_time=2
        )


        self.play(
            da.animate.set_value(3),
            db.animate.set_value(1),
            run_time=2
        )


        self.play(
            da.animate.set_value(0.5),
            db.animate.set_value(3.5),
            run_time=2
        )


        self.play(
            da.animate.set_value(3.5),
            db.animate.set_value(0.5),
            run_time=2
        )


        self.play(
            da.animate.set_value(2.5),
            db.animate.set_value(1.5),
            run_time=2
        )


        self.next_slide()


        self.next_slide()
        self.play(Uncreate(square))


        # Separate the four areas into a horizontal line

        self.play(
            separate.animate.set_value(1),
            run_time=2
        )
        

        self.next_slide()
        
                # Separate the four areas into a horizontal line

        self.play(
            separate.animate.set_value(1),
            run_time=2
        )

        self.next_slide()


        # Combine the two side labels into the center

        for label in moving_labels:
            label.clear_updaters()


        self.play(
            b2_top_label.animate.move_to(b_square.get_center()),
            b2_left_label.animate.move_to(b_square.get_center()),

            ab1_top_label.animate.move_to(ab_top.get_center()),
            ab1_left_label.animate.move_to(ab_top.get_center()),

            ab2_bottom_label.animate.move_to(ab_bottom.get_center()),
            ab2_right_label.animate.move_to(ab_bottom.get_center()),

            a2_bottom_label.animate.move_to(a_square.get_center()),
            a2_right_label.animate.move_to(a_square.get_center()),

            run_time=1.5
        )

        self.next_slide()


        # Transform the two labels into the area

        b2_result = MathTex("b^2").move_to(b_square.get_center())
        ab1_result = MathTex("ab").move_to(ab_top.get_center())
        ab2_result = MathTex("ab").move_to(ab_bottom.get_center())
        a2_result = MathTex("a^2").move_to(a_square.get_center())


        self.play(
            ReplacementTransform(
                VGroup(b2_top_label, b2_left_label),
                b2_result
            ),

            ReplacementTransform(
                VGroup(ab1_top_label, ab1_left_label),
                ab1_result
            ),

            ReplacementTransform(
                VGroup(ab2_bottom_label, ab2_right_label),
                ab2_result
            ),

            ReplacementTransform(
                VGroup(a2_bottom_label, a2_right_label),
                a2_result
            ),

            run_time=1.5
        )

        self.next_slide()


# First Ctrl + S

# manim-slides render -ql "C:\Users\quanh\Downloads\FreedomPython\Manim Slide\setupslides.py" Setup

# manim-slides present Setup