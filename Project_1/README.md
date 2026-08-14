# Project 1 — Password Strength Checker 🔐

## Overview

As part of my **DecodeLabs Cyber Security Internship 2026**, Project 1 focuses on building a **Password Strength Checker**.

The goal of this project is to create a program that evaluates a password based on its length and character variety, then classifies it as **Weak, Medium, or Strong**.

This project helped me practice fundamental programming concepts while applying them to a cybersecurity-related problem.

## Project Objectives

The program checks whether a password contains:

* Appropriate password length
* At least one digit
* At least one uppercase letter
* At least one symbol

It then displays the password strength.

## Technologies Used

* **Python 3**
* Python `string` module
* String handling
* Conditional statements
* `for` loops
* Boolean variables

## How It Works

The program first asks the user to enter a password.

It then loops through each character and checks whether it is:

* A digit using `.isdigit()`
* An uppercase letter using `.isupper()`
* A symbol using `string.punctuation`

Boolean flags are used to keep track of whether each requirement has been found.

The password is then classified according to the rules implemented for this project:

### Strong

* At least **12 characters**
* Contains an uppercase letter
* Contains a digit
* Contains a symbol

### Medium

* At least **8 characters**
* Contains an uppercase letter
* Contains a symbol

### Weak

* Does not meet the Medium or Strong requirements

## Example

```text
Enter your password: Abcdefgh123!

Strong password.
```

Another example:

```text
Enter your password: Abcdefg!

Medium password.
```

## What I Learned

Through this project, I practiced:

* Taking user input with `input()`
* Measuring strings with `len()`
* Iterating through strings using `for` loops
* Using Boolean values (`True` / `False`)
* Using `if`, `elif`, and `else`
* Using `.isdigit()` and `.isupper()`
* Working with `string.punctuation`
* Designing security rules and translating them into program logic
* Testing and debugging a Python program

## Security Concepts

This project introduced the importance of **password strength and character variety** as basic security considerations.

The DecodeLabs training material also encourages extending the project with additional security checks, such as checking against common leaked passwords and improving character variety validation.

## Project Status

**Completed ✅**

This project is part of my **DecodeLabs Cyber Security Internship 2026**.
