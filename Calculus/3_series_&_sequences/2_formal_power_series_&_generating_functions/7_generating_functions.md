# Generating functions

# Definitions

## Generating function

Generating function (polynomial) is a representation of an infinite number sequence as the coefficients $\{a_{n}\}$ ($n \in \mathbb{N}$) of a formal power series $G(x)$:
$$G(x) = \sum_{n=0}^{\infty} a_{n}x^{n}$$

The value of function $G(x)$ represents the number of objects of size $n$
for a corresponding enumeration problem.

## Generating function (polynomial) representation as a reccurent series

## Enumeration problem

## Designation
Generating functions are rarely used as functions in the formal sense of a mapping from a domain to a codomain. So, concrete domain or value of $x$ does not always matter and left undefinite. Generating functions are stand for encoding information about infinite multi-dimensional arrays of numbers in form of symbolic expression.

Not all expressions that are meaningful as functions of $x$ are meaningful as expressions designating formal series. For example, negative and fractional powers of x are examples of functions that do not have a corresponding formal power series. 

# Examples
## Example 1.
Put $a_{n} = 1^{n}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} x^{n} = \frac{1}{1 - x}$$

If $n$ is fixed, then value of $G(x)$ is geometrics series.

## Example 2.
Put $a_{n} = c^{n}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} (cx)^{n} = \frac{1}{1 - cx}$$

If $n$ is fixed, then value of $G(x)$ is geometrics series. This generating function corresponds geometrics sequence of $\{ 1, c, c^{2}, c^{3},...,c^{n} \}$

## Example 3.
Put $a_{n} = (-1)^{n}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} (-x)^{n} = \frac{1}{1 + x}$$

If $n$ is fixed, then value of $G(x)$ is geometrics series. This generating function corresponds series of odd powers $\{ x, x^{3}, x^{5},...,c^{n} \}$ with corresponding coeficients $\{ a_{n} \}=\{ 1,0,1,0... \}$

## Example 4.
Put $a_{n} = n+1$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} (n+1)x^{n} = \sum_{n=0}^{\infty} \frac{d}{dx}(x^{n}) = \frac{1}{1 - x^{2}}$$

If $n$ is fixed, then value of $G(x)$ is geometrics series. Coefficients of this generating function corresponds to sequence of natural numbers $\{ a_{n} \}=\{ 1,2,3,4,5... \}$

## Example 5. Generating function for binary sequences (binary numbers)
Put $a_{n} = 2^{n}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} 2^{n}x^{n}$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.

## Example 6. Binomial sequence
Put $a_{n} = \begin{pmatrix} k \\ n\end{pmatrix} = \frac{n!}{k!(n-k)}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} \begin{pmatrix} k \\ n\end{pmatrix} x^{n} = (1 + k)^{n}$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.

## Example 7. Sequence of triangular numbers
Put $a_{n} = \begin{pmatrix} n+2 \\ 2\end{pmatrix}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} \begin{pmatrix} n+2 \\ 2\end{pmatrix} x^{n} = \frac{1}{(1 - x)^{3}}$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.
Coefficients of this generating function corresponds to sequence of triangular numbers $\{ a_{n} \}=\{ 1,3,6,10,15... \}$

## Example 8. Exponential generating functions
Put $a_{n} = \frac{a_{n}}{n!}$, then associated generating function is:
$$EG(a_{n}) = \sum_{n=0}^{\infty} a_{n} \frac{x^{n}}{n!}$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.
Coefficients of this generating function corresponds to sequence of triangular numbers $\{ a_{n} \}=\{ 1,3,6,10,15... \}$

## Example 9. Poisson generating function
Put $a_{n} = \frac{a_{n} e^{-x}}{n!}$, then associated generating function is:
$$PG(a_{n}) = \sum_{n=0}^{\infty} a_{n} \frac{e^{-x}x^{n}}{n!} = e^{-x} EG(a_{n})$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.
Coefficients of this generating function corresponds to sequence of triangular numbers $\{ a_{n} \}=\{ 1,3,6,10,15... \}$

## Example 10. Bernouli series
Put $a_{n} = \begin{pmatrix} n \\ k\end{pmatrix} q^{k-n}p^{n}$, then associated generating function is:
$$G(x) = \sum_{n=0}^{\infty} \begin{pmatrix} n \\ k \end{pmatrix} q^{k-n}p^{n} x^{n} = (q+px)^{k}$$

If $n$ is fixed, then value of $G(x)$ is number of binary sequences of size $n$.
Coefficients of this generating function corresponds to sequence of triangular numbers $\{ a_{n} \}=\{ 1,3,6,10,15... \}$

## Example 11. Lambert series
Put $a_{n} = \frac{a_{n}}{1-x^{n}}$ and $n > 0$, then associated generating function is:
$$LG(a_{n}) = \sum_{n=1}^{\infty} a_{n} \frac{x^{n}}{1-x^{n}}$$

## Example 12. Bell series

## Example 13. Dirichlet series

## Example 14. Convolution polynomials

# Operations on generating functions and properties

# Resources
1. Goeman, M. (2015, March 1). Generating functions \[Lecture notes\]. 18.310 Lecture, Massachusetts Institute of Technology. Retrieved from https://math.mit.edu/~goemans/18310S15/generating-function-notes.pdf.
2. Sum of First n Natural Numbers, 3 Ways. Retrieved from https://www.youtube.com/watch?v=IuH8ZI0i74w
3. Generating function, Wikipedia. Retrieved from https://en.wikipedia.org/wiki/Generating_function
4. Ellinor, A., Vee, H. Z., Jain, M., Lin, C., Khim, J., & Ross, E. Generating functions. Retrieved from https://brilliant.org/wiki/generating-functions-solving-recurrence-relations/