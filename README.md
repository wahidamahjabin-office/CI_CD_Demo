# 🔄 CI/CD Demo — CSE Lecture Example

A minimal Python project demonstrating a **CI/CD pipeline** using **GitHub Actions**.

---

## 📁 Project Structure

```
cicd-demo/
├── .github/
│   └── workflows/
│       └── ci-cd.yml        ← The pipeline lives here
├── src/
│   └── calculator.py        ← Simple app code
├── tests/
│   └── test_calculator.py   ← Automated tests
├── requirements.txt
└── README.md
```

---

## 🚦 The CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci-cd.yml` and runs automatically on every `push` or `pull_request`.

```
Push Code
    │
    ▼
┌─────────────┐
│  JOB 1: Test │  ← Run pytest (fails fast if tests break)
└──────┬──────┘
       │ passes
       ▼
┌─────────────┐
│  JOB 2: Lint │  ← Check code style with flake8
└──────┬──────┘
       │ passes
       ▼
┌──────────────┐
│  JOB 3: Deploy│  ← Only runs on `main` branch
└──────────────┘
```

---

## 🧪 Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run linter
flake8 src/ --max-line-length=100
```

---

## 💡 Try It Yourself

1. Fork this repo
2. Make a change to `src/calculator.py`
3. Push to a branch and open a Pull Request
4. Watch the Actions tab — the pipeline runs automatically!

**Break a test intentionally** (e.g., change `return a + b` to `return a - b`) and see the pipeline go 🔴 red.

---

## 📚 Key Concepts

| Term | Meaning |
|------|---------|
| **CI** (Continuous Integration) | Automatically test every code change |
| **CD** (Continuous Delivery) | Automatically deploy after tests pass |
| **Workflow** | A YAML file that defines your pipeline |
| **Job** | A group of steps that run on one VM |
| **Step** | A single command or action in a job |
| **Trigger** | The event that starts the pipeline (`push`, `pull_request`) |
