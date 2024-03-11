# Django

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Version Status](https://img.shields.io/badge/Version-dev-<COLOR>.svg)](https://new.lifetimegenetics.com/)

# Django Starter Project

This repository serves as a Django starter project, providing a foundational structure for building web applications using Django framework. Below are the instructions for installation, deployment, and basic Git commands to manage your project.

## Installation

1. **Clone Git Repository:**
    ```bash
    git clone https://github.com/jitesh-oss/lgp_django.git .
    ```

2. **Setup Virtual Environment:**
    ```bash
    virtualenv myenv
    ```

3. **Activate Virtual Environment:**
    ```bash
    myenv\Scripts\activate
    ```

4. **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Create Super User:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Migrate Database:**
    ```bash
    python manage.py migrate
    ```

## Deployment

7. **Start Server:**
    ```bash
    python manage.py runserver
    ```

## Git Commands

8. **Create Branch:**
    ```bash
    git branch <branch_name>
    ```

9. **Switch Branch:**
    ```bash
    git checkout <branch_name>
    ```

10. **Push Changes to Git:**
    ```bash
    git add -A
    git commit -m "Your commit message"
    git push origin <branch_name>
    ```

11. **Create Pull Request:**
    From `dev` to your branch:
    ```
    dev --> <your_branch>
    ```

12. **Switch to Master Branch:**
    ```bash
    git checkout master
    ```

13. **Delete Branch:**
    ```bash
    git branch -d <branch_name>
    ```

14. **Merge with Dev Branch:**
    ```bash
    git pull origin dev
    ```

By following these instructions, you can easily set up, deploy, and manage your Django starter project along with version control using Git.
