# Integrals and the Area Under a Curve

## Introduction

**Topic:** Integrals and the area under a graph  
**Goal:** Understand what an integral is, how it is related to the area under a curve, and how it is used in real life.

This section should motivate the topic using simple, relatable questions such as:
- "How can we find the distance a car travels if we know its speed at every moment?"
- "What does it mean to find the area under a wiggly line?"

## What is an Integral?

**Definition:** An *integral* is a mathematical tool used to find the area under a curve on a graph.  
- Explain in plain language what an integral is.
- Compare it with simpler ideas (like adding up rectangles).
- Introduce the concept of area accumulation.

**Example:**  
If a car's speed over time is shown on a graph, the total area under the curve represents the total distance travelled.

Include:
- A visual diagram with a curve and shaded area.
- Clear mention that this is an approximation that becomes exact using integration.

## Basic Concepts

Explain and define:
- **Function**: A rule that assigns one output to each input, e.g. $y = f(x)$.
- **Interval**: The range $[a, b]$ over which we calculate the area.
- **Area under the graph**: The region between the curve $f(x)$ and the $x$-axis from $x = a$ to $x = b$.

Include:
- A simple graph with a function over a small interval.

## Formulas

Introduce and define:
- **Definite Integral**:
  $$
  \int_a^b f(x) \, dx
  $$
  This gives the exact area under the function $f(x)$ between $x = a$ and $x = b$.

- **Antiderivative (Indefinite Integral)**:
  $$
  \int f(x) \, dx = F(x) + C
  $$
  where $F(x)$ is a function whose derivative is $f(x)$, and $C$ is a constant.

- **Fundamental Theorem of Calculus**:
  $$
  \int_a^b f(x) \, dx = F(b) - F(a)
  $$
  Explain that this connects the process of finding the area to the process of finding antiderivatives.

Use clear, step-by-step examples:
- Calculate $\int_0^2 (2x) \, dx$

## Real-Life Applications of Integrals

Show how integrals are used in various fields:

- **Physics**: Calculating work done by a variable force, or distance from speed over time.
- **Economics**: Calculating total cost, profit, or revenue over time.
- **Biology/Medicine**: Calculating volume of fluid flow in arteries.
- **Engineering**: Computing material used in construction (volumes and areas).

Make sure to link the integral to real graphs in these disciplines.

## Real-Life Example

**Scenario**: Estimating fuel usage of a car over a route.  
If fuel consumption rate changes over time and is represented as a function, the total amount used can be found using an integral.

Explain with:
- A fuel consumption graph.
- Step-by-step use of an integral to get total usage.
- Use simple numbers for clarity.

## Python Implementation Example

Include a simple Python script using `scipy.integrate` and `matplotlib`:
- Define a speed function (e.g. $3t^2 + 2t + 1$).
- Integrate over time interval [0, 5].
- Plot the function and shaded area.
- Explain the code line-by-line, including `def`, `integrate.quad`, and `fill_between`.

## Conclusion

Summarise key points:
- Integrals help us calculate areas, volumes, and many other quantities.
- They are useful in everyday applications, not just abstract maths.
- The idea of “area under a curve” is central to understanding integrals.

Include:
- A brief note that students will encounter integrals again in advanced mathematics.
- Encourage curiosity about how integration connects with differentiation.
