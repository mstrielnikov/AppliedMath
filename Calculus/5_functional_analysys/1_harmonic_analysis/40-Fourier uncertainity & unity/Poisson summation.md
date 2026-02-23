# Poisson summation
$f \in \mathbb{S}(\mathbb {R}^{\alpha})$

$\sum_{n \in \mathbb{Z}^{\alpha}} f(n) = \sum_{m \in \mathbb{Z}^{\alpha}} \hat{f}(n)$
# Theta functions
$\Theta(t) := \sum_{m \in \mathbb{Z}}e^{\pi m^2 t}, t > 0$ 
$\lim_{t \to \infty} \Theta(t) = 1$

$\int_{\mathbb R} e^{-\pi t^{2} a^{2} } e^{-2 \pi \eta }dt = \frac{1}{a}e^{-\frac{\pi}{a^{2}}\eta^{2}}$

PSF: $\Theta(\frac{1}{t}) = \sqrt{t} \Theta(t)$
$\Theta(t) \sim \frac{1}{\sqrt{t}}, t \to 0^{+}$

$\Gamma(\xi) = \sum_{n \geq 1} \frac{1}{n^{s}}, Re(s) > 1$
# Sampling theorem

$f \in \mathbb{L}^2(\mathbb{R})$
$spt(\hat{f}) \in [ -\frac{1}{2}; \frac{1}{2} ]$

Then:
$f(x) = \sum_{k \in \mathbb {Z}} f(k) \frac{sc(\pi x + k )}{\pi(x-k)} = \frac{sin(\pi x)}{\pi} \sum_{k \in \mathbb{Z}} \frac{f(k)}{x-k}$
$\hat {f}(\xi) =$

$f(x) = \int_{\mathbb {R}} \hat (\xi)^{2 \pi i \xi x} d \xi = \int_{-\frac{1}{2}}^{\frac{1}{2}}(\sum_{m \in \mathbb{Z}} f(m)e^{-2 \pi  \xi i m} )e^{2 \pi \xi x} d \xi = \sum_{m \in \mathbb {Z}} f(m) \int_{-\frac{1}{2}}^{\frac{1}{2}} e^{2 \pi \xi (x - m)}$ 
# Wintingeives inequality

A) $f(0) = f(1), \int_{0}^{1}f=0 \Rightarrow \int_{0}^{1} |f|^2 \leq \frac{1}{2 \pi} \int_{0}^{1} |f'|^{2}$

B) $f(0) = f(1) = 0 \Rightarrow \int_{0}^{1}|f|^{2} \leq \frac{1}{\pi^2} \int_{0}^{1} |f'|^{2}$

# Persival formula