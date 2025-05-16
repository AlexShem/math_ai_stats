# Math AI Stats

This repository is a comprehensive collection of educational materials, tutorials, code examples, and resources on **Mathematics**, **Artificial Intelligence**, and **Statistics**.

## Repository Structure

The repository is organized into the following main directories:

### Mathematics (`/math`)

- **Complex Numbers**: Materials on scalar products and complex number operations
- **Derivatives**: Explanations and implementations of derivatives
- **Integrals**: Comprehensive guide to integration, from basic concepts to applications
- **Newton's Method**: Code implementations and explanations of Newton's method and related algorithms
- **Series**: Collection of tutorials on various mathematical topics:
  - Wave functions
  - Python basics
  - Functions and dictionaries
  - Random number generation
  - Derivatives and integrals
  - Mathematical expectation

### Probability (`/probability`)

- **Coin Flip Simulations**: Code and explanations for coin flip experiments, demonstrating probability concepts

### Tutorials (`/tutorials`)

- **Git Installation Guide**: Step-by-step tutorial for installing and configuring Git
- **Python for Quarto**: Guide on setting up Python for use with Quarto documentation

## Getting Started

### Prerequisites

- Git
- Python (3.6 or higher recommended)
- Jupyter (for notebook files)
- Quarto (for rendering .qmd files)

### Cloning the Repository

To clone this repository to your local machine, follow these steps:

#### Using HTTPS

```bash
git clone https://github.com/AlexShem/math_ai_stats.git
cd math_ai_stats
```

#### Using SSH (if you have SSH keys set up)

```bash
git clone git@github.com:AlexShem/math_ai_stats.git
cd math_ai_stats
```

### Running Python Examples

Many examples in this repository are written in Python. To run them:

```bash
python probability/coin_flip/coin_flipping_experiment.py
```

### Setting Up a Python Virtual Environment

It's recommended to use a virtual environment to manage Python dependencies. This keeps your project dependencies isolated from your system Python installation.

#### Creating a Virtual Environment

To create and activate a virtual environment:

```bash
# Navigate to the repository root
cd math_ai_stats

# Create the virtual environment
python -m venv .venv

# Activate the virtual environment (Windows)
.\.venv\Scripts\Activate

# Activate the virtual environment (Linux/macOS)
# source .venv/bin/activate
```

#### Installing Dependencies

Once the virtual environment is activated, you can install required packages:

```bash
pip install -r requirements.txt  # If a requirements.txt file exists
# Or install specific packages as needed
pip install jupyter numpy matplotlib pandas
```

When you're done working with the virtual environment, you can deactivate it:

```bash
deactivate
```

### Viewing Documentation

The repository contains HTML files rendered from Quarto (`.qmd`) documents. You can:

1. Open the HTML files directly in your browser
2. Re-render the Quarto files with `quarto render filename.qmd`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
