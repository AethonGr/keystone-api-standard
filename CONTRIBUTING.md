# Contributing to the KEYSTONE API Standard

Thank you for your interest in contributing to the KEYSTONE API Standard! Contributions are essential to the success of this open-source project, and we appreciate your efforts to improve and extend the framework.

This document outlines the guidelines for contributing to the project, ensuring a smooth and collaborative process for everyone involved.

---

## Table of Contents

1. [How Can I Contribute?](#how-can-i-contribute)
   - [Reporting Issues](#reporting-issues)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Contributing Code](#contributing-code)
2. [Development Workflow](#development-workflow)
3. [Coding Standards](#coding-standards)
4. [Pull Request Guidelines](#pull-request-guidelines)
5. [Local Development Setup](#local-development-setup)
6. [License](#license)

---

## How Can I Contribute?

### Reporting Issues

If you encounter a bug or have a question, please open an issue in the repository. When reporting an issue:
- Provide a clear and descriptive title.
- Include steps to reproduce the issue.
- Mention the expected and actual behavior.
- Attach relevant logs, screenshots, or error messages if applicable.

### Suggesting Enhancements

We welcome suggestions for new features or improvements. To suggest an enhancement:
- Open an issue with the label `enhancement`.
- Clearly describe the feature or improvement.
- Explain why it would be beneficial to the project.

### Contributing Code

If you'd like to contribute code, follow the steps outlined in the [Development Workflow](#development-workflow) section. Contributions can include:
- Fixing bugs.
- Adding new features.
- Improving documentation.
- Enhancing test coverage.

---

## Development Workflow

1. **Fork the Repository**: Create a personal copy of the repository by forking it.
2. **Clone the Repository**: Clone your fork to your local machine:
   ```bash
   git clone https://github.com/AethonGr/keystone-api-standard
   cd keystone-api-standard
   ```
3. **Create a Branch**: Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes**: Implement your changes, ensuring they align with the project's [Coding Standards](#coding-standards).
5. **Test Your Changes**: Run tests to verify your changes do not break existing functionality.
6. **Commit Your Changes**: Write clear and concise commit messages:
   ```bash
   git commit -m "Add feature: your-feature-name"
   ```
7. **Push Your Changes**: Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Submit a Pull Request**: Open a pull request to the main repository. Provide a detailed description of your changes and link any related issues.

---

## Coding Standards

To maintain consistency and readability, follow these coding standards:
- Use Python 3.10+ features where applicable.
- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code style.
- Write descriptive comments and docstrings for functions and classes.
- Use type hints for function signatures.
- Ensure code is modular and reusable.

---

## Pull Request Guidelines

To ensure a smooth review process:
- Keep pull requests focused on a single feature or fix.
- Include a detailed description of the changes made.
- Reference any related issues in the pull request description.
- Ensure your branch is up-to-date with the `master` branch before submitting:
   ```bash
   git fetch upstream
   git merge upstream/master
   ```
- Address any feedback provided during the review process promptly.

---

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project. For more details, see the `LICENSE` file.
