# CI/CD Pipeline – GitHub Actions + Docker + AWS EC2

![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=for-the-badge&logo=githubactions)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 📌 Project Overview

An end-to-end CI/CD pipeline that automatically builds a Docker image and deploys a Flask application to AWS EC2 on every code push — eliminating manual deployment completely.

---

## ⚙️ How It Works

```
Developer pushes code to GitHub (main branch)
            ↓
GitHub Actions Pipeline triggers automatically
            ↓
Step 1: Checkout latest code
            ↓
Step 2: SCP — copy files to AWS EC2
            ↓
Step 3: SSH into EC2
         → Stop old container
         → Build new Docker image
         → Run new container
            ↓
App is LIVE at http://<EC2-IP>:8080 🚀
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| GitHub Actions | CI/CD Pipeline automation |
| Docker | Containerization |
| AWS EC2 | Cloud server (Ubuntu 22.04) |
| Flask (Python) | Web application |
| SCP + SSH | Secure file transfer & remote execution |
| Linux | Server OS |

---

## 📁 Project Structure

```
flask-cicd-github-actions/
├── app.py                          # Flask application
├── Dockerfile                      # Docker image recipe
├── requirements.txt                # Python dependencies
└── .github/
    └── workflows/
        └── deploy.yml              # GitHub Actions pipeline
```

---

## 🔐 GitHub Secrets Used

| Secret | Description |
|--------|-------------|
| `EC2_HOST` | EC2 Public IP Address |
| `EC2_USER` | EC2 username (ubuntu) |
| `EC2_SSH_KEY` | EC2 private key (.pem) content |

---

## 🚀 Pipeline Steps (deploy.yml)

```yaml
1. Checkout Code       → Pull latest code from GitHub
2. Copy files to EC2   → SCP transfers files to EC2
3. Deploy to EC2       → SSH: docker build + docker run
```

---

## ✅ Key Achievements

- Automated deployments triggered on every `git push` to main branch
- Zero manual intervention required after initial setup
- Containerized application using Docker for consistent deployments
- Secure credential management using GitHub Secrets

---

## 👨‍💻 Author

**Eitish Tyagi**
- 🔗 LinkedIn: [linkedin.com/in/Eitishtyagi](https://linkedin.com/in/Eitishtyagi)
- 🐙 GitHub: [github.com/Eitishtyagi](https://github.com/Eitishtyagi)
- 📧 Email: tyagieitish2011@gmail.com
