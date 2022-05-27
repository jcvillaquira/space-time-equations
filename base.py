from cProfile import run
from manim import *
import numpy as np

eqs = dict(
    spectral_theorem = r"$f(A) = \int_{m^-}^M f(\lambda)\,\text dE_\lambda$",
    schrodinger_equation = r"$i\hbar\frac{\text d}{\text dt}\ket{\Psi(t)} = \hat H\ket{\Psi(t)}$",
    field_equation = r"$G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu}$",
    metric_tensor = r"$g = g_{ij}\,\text dx^i \otimes \text dx^j$",
    quadratic_functional = r"$\Phi(u) = \frac12a(u,u)-Fu$",
    stokes_theorem = r"$\int_{\partial \Omega} \omega = \int_\Omega \text d\omega$"
)

eqs = list(eqs.values())

class Test(Scene):
    def construct(self):
        eqs_tex = [Tex(eq, font_size = font_size()).set_x(get_coordinate()).set_y(get_coordinate()).set_opacity(opacity()) for eq in eqs]
        eqs_in = [FadeIn(eq) for eq in eqs_tex]
        eqs_scale = [eq.animate.scale(scale_size()) for eq in eqs_tex]

        coords_star = [coord_star() for n in range(250)]
        stars = [Dot(radius=radius_star(), color=color_star(), fill_opacity=opacity_star()) for n in range(1, 250)]
        stars = [star.shift(c[0]*RIGHT+c[1]*UP) for c, star in zip(coords_star, stars)]
        stars = [FadeIn(star) for star in stars]

        self.play(*stars, *eqs_in, run_time = 0.5)
        self.wait(0.5)
        self.play(*eqs_scale, run_time = 4.5)
        self.wait(0.5)

def font_size():
    return np.random.uniform(6, 7)**2

def scale_size():
    return np.random.uniform(1.0, 1.5)**2

def get_coordinate(max=3):
    return np.random.uniform(-max, max)

def opacity():
    return np.random.uniform(0.5, 1.0)**2

def coord_star():
    x = get_coordinate(8)
    y = get_coordinate(6)
    return (x, y)

def radius_star():
    return np.sqrt(np.random.uniform(0.001, 0.0025))

def color_star():
    r = np.random.uniform(0.65, 1)
    g = np.random.uniform(0.65, 1)
    b = np.random.uniform(0.8, 1)
    return rgb_to_color([r, g, b])

def opacity_star():
    return np.random.uniform(0.05, 0.35)