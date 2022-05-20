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

        self.play(*eqs_in, run_time = 0.5)
        self.wait(0.5)
        self.play(*eqs_scale, run_time = 4.5)
        self.wait(0.5)

def font_size():
    return np.random.uniform(6, 7)**2

def scale_size():
    return np.random.uniform(1.0, 1.5)**2

def get_coordinate():
    return np.random.uniform(-3, 3)

def opacity():
    return np.random.uniform(0.5, 1.0)**2