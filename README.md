# MLOps Project: Abalone Age Prediction

Goal: predict the age (number of rings) of an abalone from its physical measurements, so nobody has to count rings under a microscope. The model is trained with Prefect and served with a FastAPI API in Docker.

Dataset: [Kaggle abalone dataset](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)

## Team

| Name | GitHub |
|---|---|
| Lancelot Brisset | brissetlancelot92 |
| Louan Bardou | louanbardou |
| Alix Bernal | ALX-7777 |
| Blanche Mahe | blanchemahe |

## Setup

You need [uv](https://docs.astral.sh/uv/) (it installs Python 3.11 for you) and make.

```bash
make install   # installs the dependencies and the pre-commit hooks
make lint      # formats and checks the code with ruff
```

## Train the model

The dataset is already in `data/abalone.csv` (UCI version, same data as Kaggle), so no Kaggle account needed.

```bash
make train   # trains the model and saves it in src/web_service/local_objects/model.pkl
uv run pytest   # runs the tests
```

The code is in `src/modelling/`: `preprocessing.py` (load + split), `training.py` (model + metrics), `predicting.py` (predict with the saved model), `main.py` (runs everything).
The model is a linear regression, with `Sex` one-hot encoded inside a sklearn pipeline (see `notebooks/` for the EDA and why we chose it).

The next commands (`make api`, `make docker-build`, `make docker-run`) are added in the next steps.

## 📋 What You'll Build

By the end of this project, you'll have created:

### 🤖 **Automated ML Pipeline**
- Training workflows using Prefect
- Automatic model retraining on schedule
- Reproducible model and data processing

### 🌐 **Prediction API**
- REST API for real-time predictions
- Input validation with Pydantic
- Docker containerization

### 📊 **Production-Ready Code**
- Clean, well-documented code
- Automated testing and formatting
- Proper error handling

## 📝 How to Work on This Project

### The Branch-by-Branch Approach

This project is organized into numbered branches, each representing a step in building your MLOps system. Think of it like a guided tutorial where each branch teaches you something new!

**Here's how it works**:

1. **Each branch = One pull request** with specific tasks
2. **Follow the numbers** (branch_0, branch_1, etc.) in order
3. **Read the PR instructions** (PR_0.md, PR_1.md, etc.) before starting
4. **Complete all TODOs** in that branch's code
5. **Create a pull request** when done
6. **Merge and move to the next branch**

### Step-by-Step Workflow

For each numbered branch:

```bash
# Switch to the branch
git checkout branch_number_i

# Get latest changes (except for branch_0)
git pull origin main
# Note: A VIM window might open - just type ":wq" to close it

# Push your branch
git push
```

Then:
1. 📖 Read the PR_i.md file carefully
2. 💻 Complete all the TODOs in the code
3. 🔧 Test your changes
4. 📤 Open **ONE** pull request to your main branch
5. ✅ Merge the pull request
6. 🔄 Move to the next branch

> **💡 Pro Tip**: Always integrate your previous work when starting a new branch (except branch_0)!

### 🔍 Understanding Pull Requests

Pull Requests (PRs) are how you propose and review changes before merging them into your main codebase. They're essential for team collaboration!

**Important**: When creating a PR, make sure you're merging into YOUR forked repository, not the original:

❌ **Wrong** (merging to original repo):
![PR Wrong](assets/PR_wrong.png)

✅ **Correct** (merging to your fork):
![PR Right](assets/PR_right.png)

## 💡 Development Tips

### Managing Dependencies

Use uv to manage dependencies. Install or update packages with:

```bash
uv add <package>==<version>
```

Then sync the environment and regenerate the dependency files:

```bash
uv sync
```

### Code Quality
- The pre-commit hooks will automatically format your code
- Remove all TODOs and unused code before final submission
- Use clear variable names and add docstrings

## ⚠️ Other Instructions

- **GitHub IDs**: Every student must make at least one significant commit that is merged into the main branch. Changing a variable value or adding a space is not significant. Don't fail the module over a mistake like this.
- **No squashing**: Do not squash your commits when you merge a branch. Your commit history is used to track your progress.
- **No blind coding or overengineering**: Stay in control of your code and understand all of it. This is evaluated specifically, so keep your code straight to the point and objective-oriented.
- **Clear setup instructions**: Keep them simple. Evaluators won't spend hours trying to start your project (but they'll try harder than [this dad](https://www.youtube.com/watch?v=H_ecbkcYH94)). A Makefile would be appreciated.
- **Main branch only**: Only the work on the `main` branch is evaluated. Any work left on other branches is not considered.

## 📊 Evaluation Criteria

Your project will be evaluated on:

### 🔍 **Code Quality**
- Clean, readable code structure
- Proper naming conventions
- Good use of docstrings and type hints

### 🎨 **Code Formatting**
- Consistent style (automated with pre-commit)
- Professional presentation

### ⚙️ **Functionality**
- Code runs without errors
- All requirements implemented correctly

### 📖 **Documentation & Reproducibility**
- Clear README with setup instructions
- Team member names and GitHub usernames
- Step-by-step instructions to run everything

### 🤝 **Collaboration**
- Effective use of Pull Requests
- Good teamwork and communication

---

## 🎯 Final Deliverables Checklist

When you're done, your repository should contain:

✅ **Automated Training Pipeline**
- [ ] Prefect workflows for model training
- [ ] Separate modules for training and inference
- [ ] Reproducible model and encoder generation

✅ **Automated Deployment**
- [ ] Prefect deployment for regular retraining

✅ **Production API**
- [ ] Working REST API for predictions
- [ ] Pydantic input validation
- [ ] Docker containerization

✅ **Professional Documentation**
- [ ] Updated README with team info
- [ ] Clear setup and run instructions
- [ ] All TODOs removed from code

---

**Ready to start? Head to branch_0 and read PR_0.md for your first task! 🚀**
