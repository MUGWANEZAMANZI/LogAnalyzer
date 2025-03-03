# LogAnalyzer

## Project Overview
LogAnalyzer is a Python project designed to parse and analyze log files, specifically `auth.log`. It extracts and displays information such as command usage, user authentication changes, and alerts for failed sudo commands.

## Features
1. **Log Parse `auth.log`:**
   - **Extract Command Usage:**
     - Displays timestamp, executing users, and executed commands.
   - **Monitor User Authentication Changes:**
     - **Added Users:** Displays newly added users.
     - **Deleted Users:** Displays deleted users.
     - **Password Changes:** Displays password change events for users.
     - **SU Command Usage:** Displays when users have used the `su` command.
     - **SUDO Command Usage:** Displays when users have used the `sudo` command.
     - **SUDO Failures:** Alerts if `sudo` command fails.


PDF: https://drive.google.com/file/d/1fg_f0k6b8rUHg7bo6keDwPKXs2YG1Zvp/view?usp=drive_link
## Usage
To use the LogAnalyzer, follow the instructions below:

1. Clone the repository:
    ```bash
    git clone https://github.com/MUGWANEZAMANZI/LogAnalyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LogAnalyzer
    ```
3. Run the Python scripts to analyze the log file:
    ```bash
    python loganalyzer.py
    ```

## Code Examples
Here are some code examples for the functionalities:

### Extract Command Usage
```python
def command_usage():
    # Code to extract command usage
```

### Monitor Added Users
```python
def added_user():
    # Code to monitor added users
```

### Monitor Deleted Users
```python
def deleted_user():
    # Code to monitor deleted users
```

### Monitor Password Changes
```python
def password_ch():
    # Code to monitor password changes
```

### Monitor SU Command Usage
```python
def su_cmd():
    # Code to monitor su command usage
```

### Monitor SUDO Command Usage
```python
def sudo_cmd():
    # Code to monitor sudo command usage
```

### Alert on SUDO Failures
```python
def alert_sudo_cmd_fail():
    # Code to alert on sudo failures
```

## Contributors
- **Student Name:** MUGWANEZA MANZI Audace
- **Student Code:** s39
- **Class Code:** RW-University-II
- **Lecturer's Name:** Dominique HARELIMANA

---

You can create a new file named `README.md` in your repository and paste this content into it.
