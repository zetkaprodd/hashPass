# HashPass Password Generator
<a id="readme-top"></a>
### Overview
This project is a password generator that allows users to create secure passwords based on a master password and a tag. It also provides the functionality to generate random passwords with customizable options.

### Features
- **Generate Random Password:** Create a random password with user-defined criteria.
- **Generate Password from tag an master password:** Derive a password using the master password and a tag.
- **User-Friendly Menu:** Simple command-line interface for easy navigation.

### How It Works
1. Setting the Master Password:

When the application starts, users are prompted to set a master password. This password is crucial as it will be used to generate other passwords.
The master password is securely stored and can be changed at any time.

2. Generating a Random Password:

Users can choose to generate a random password by specifying the desired length and character types (e.g., uppercase letters, lowercase letters, numbers, and special characters).
The application uses a secure random number generator to ensure that the passwords are unpredictable and strong.

3. Generating a Password from Master Password:

Users can derive a password by entering a tag (e.g., the name of a website or service). The application combines the master password and the tag to create a unique password.
This ensures that even if the same tag is used across different services, the resulting passwords will be different as long as the master password is unique.

### Requirements
- Python 3.x
- cryptography library (for encryption)

### Installation

Clone the repository :
```
git clone <repository-url>
cd <repository-directory>
```
Install the required libraries :
```
pip install cryptography
```
### Usage
Run the application :
```
python main.py
```

<p align="middle"><a href="#readme-top">To the top</a></p>
