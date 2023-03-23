



# Envelope Theorem

## One choice variable and one constraint

Let $F$ and $G$ be econtinuously differentiable functions of $x$ and
$\theta$. For any given $\theta$, let $x^\ast(\theta)$ maximize
$F(x,\theta)$ subject to $c \ge G(x,\theta)$, and let
$\lambda^\ast(\theta)$ be the associated value of the Lagrange multipliesr.
Suppose that $x^\ast(\theta)$ and $\lambda^\ast(\theta)$ are also continuously
differentiable functions, and that the constraint qualification
$G_1(x^\ast(\theta), \theta) \ne 0$ holds for all values of $\theta$. Then,
the maximum value function defined by

$$
V(\theta) = \max_x F(x,\theta) \text{ subject to }c \ge G(x,\theta)
$$

satisfies

$$
V'(\theta) = F_2(x^\ast(\theta),\theta) - \lambda^\ast(\theta) G_2(x^\ast(\theta), \theta).
$$
