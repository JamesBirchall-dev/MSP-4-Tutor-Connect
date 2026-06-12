# MSP-4-Tutor-Connect

![logo transparent](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-logo-transparent.png?raw=true)

## Table of Contents

- [MSP-4-Tutor-Connect](#msp-4-tutor-connect)
- [Project Overview](#project-overview)
- [User Journey](#user-journey)
- [Live Site](#live-site)
- [Repository](#repository)
- [UX](#ux)
  - [User Stories And Acceptance Criteria](#user-stories-and-acceptance-criteria)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Data Model](#data-model)
  - [Data Tables](#data-tables)
  - [Relationships](#relationships)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
- [Project Management](#project-management)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
- [Security Features](#security-features)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)

## Project Overview

Tutor Connect is a full-stack Django web application designed to help students find, book, and pay for lessons online. The site connects learners with tutors by allowing users to browse tutor profiles, view available lesson types, create bookings, and complete secure payments through Stripe.

The application has been designed for users who want a simple and reliable way to arrange lessons without needing to contact tutors manually. It is especially useful for beginners who may be unsure where to start, as tutor and lesson information is presented clearly with details such as experience, location, skill level, duration, and price.

The project uses Django’s full-stack framework to manage the back end, front end templates, relational database, user authentication, permissions, booking logic, and payment flow. The application is split into multiple Django apps to keep functionality organised and reusable. The accounts app manages registration, login-related user journeys, and the dashboard. The tutors app manages tutor profiles and lesson types. The bookings app manages lesson bookings and booking CRUD functionality. The checkout app manages Stripe payment integration and payment feedback.

## User Journey

The main user journey begins with a visitor landing on the homepage and immediately understanding that the site is for finding and booking tutors. Visitors can browse tutor profiles without creating an account, which supports easy comparison and helps users decide whether the service is useful to them. When a user wants to book a lesson, they are required to register or log in. This ensures bookings are connected to the correct user account and allows users to manage their own bookings securely.

Logged-in users can create, view, update, and cancel their own bookings. The application prevents users from accessing or changing bookings that belong to someone else. This supports appropriate authorisation and protects user data. Users are also shown clear feedback messages after important actions such as creating a booking, editing a booking, cancelling a booking, or completing payment.

The payment process is handled through Stripe. Before payment, users are shown a checkout review page where they can confirm the tutor, lesson, date, time, duration, and total price. This gives users control before committing to payment and reduces the risk of booking mistakes. After payment, users are redirected to either a success page or a cancellation page, both of which provide clear feedback.

## Live Site

## Repository

## UX

### User Stories And Acceptance Criteria

#### 1. Understand Site Purpose

**User Story:**  
As a first-time visitor, I want to understand the purpose of the website immediately so that I can decide whether it helps me find a tutor.

**Acceptance Criteria:**

- The homepage includes a short description of the service.
- The homepage includes a visible call-to-action to browse tutors.
- The main navigation is visible on the homepage.

---

#### 2. Browse Tutors Without An Account

**User Story:**  
As a visitor, I want to browse available tutors without creating an account so that I can compare lesson options before registering.

**Acceptance Criteria:**

- Anonymous users can access the tutor listing page.
- Anonymous users can access individual tutor profile pages.
- Tutor cards show key information such as tutor name, location, and short bio.
- Anonymous users are prompted to log in or register before booking a lesson.

---

#### 3. View Clear Tutor Information

**User Story:**  
As a visitor, I want tutor information to be clearly presented so that I can quickly understand each tutor’s experience, lesson types, prices, and availability.

**Acceptance Criteria:**

- Each tutor profile displays the tutor’s name, bio, experience, and location or online availability.
- Each tutor profile displays available lesson types.
- Lesson information includes title, description, duration, skill level, and price.
- Unavailable lessons are not shown as bookable.

---

#### 4. Register For An Account

**User Story:**  
As a new user, I want to register for an account easily so that I can book lessons and manage my activity on the site.

**Acceptance Criteria:**

- The registration page is accessible from the main navigation.
- The registration form includes clear labels for each field.
- The form displays validation errors if required information is missing or invalid.
- A successful registration logs the user in or redirects them to the login page/dashboard.
- Logged-in users are not encouraged to register again.

---

#### 5. Book A Lesson

**User Story:**  
As a logged-in student, I want to book a lesson through a simple form so that I can choose a suitable date and time without confusion.

**Acceptance Criteria:**

- Only logged-in users can access the booking form.
- The booking form displays the selected lesson summary.
- The user can select a booking date and time.
- The form includes optional notes for the tutor.
- The form validates required booking information.
- After a successful booking, the user receives a confirmation message.

---

#### 6. Manage My Bookings

**User Story:**  
As a logged-in student, I want to view, update, or cancel my bookings so that I stay in control of my lesson schedule.

**Acceptance Criteria:**

- Logged-in users can view a list of their own bookings.
- Users cannot view or manage bookings belonging to another user.
- Users can update the date, time, or notes for their own pending bookings.
- Users can cancel their own bookings.
- The site asks for confirmation before cancelling a booking.
- Booking changes are immediately reflected in the user interface.

---

#### 7. Review Booking Before Payment

**User Story:**  
As a user making a payment, I want to review my booking details before paying so that I can confirm the tutor, lesson, date, time, and price are correct.

**Acceptance Criteria:**

- The checkout page displays the lesson title, tutor name, date, time, duration, and total price.
- The user can return to edit the booking before payment.
- The payment button is clearly labelled.
- Payment is handled through Stripe.
- The user is redirected to a success or cancellation page after the payment process.

---

#### 8. Receive Clear Feedback

**User Story:**  
As a user, I want clear success, error, and cancellation messages so that I always understand the result of my actions, including bookings, updates, cancellations, and payments.

**Acceptance Criteria:**

- The site displays a success message after creating, editing, or cancelling a booking.
- The site displays a success message after a successful payment.
- The site displays a clear cancellation message if payment is cancelled.
- Form validation errors are displayed near the relevant form fields.
- Error and success messages use clear, readable language.
- Feedback messages are visible and styled consistently across the site.

---

### Visual Design

---

#### Overall Concept

The visual design is calm, modern, and easy to navigate. The colour palette uses deep green for primary actions, warm amber for accents, and a soft off-white background to create a friendly but professional appearance. The typography uses Google Fonts, with Inter for readable interface text and Playfair Display for headings. The layout is responsive and designed to work across desktop, tablet, and mobile screen sizes.

#### Logo and Favicon

<details>
<summary><strong>Logo and Favicon Transparent</strong></summary>

![logo transparent](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-logo-transparent.png?raw=true)

</details>

<details>
<summary><strong>Logo and Favicon White Background</strong></summary>

![logo white](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-logo-white.png?raw=true)

</details>

#### Colors and Typography

<details>
<summary><strong>Colours and Typography Overview</strong></summary>

![Colours and Typography](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-design-styles-colorsandfonts.png?raw=true)

Primary colour:
#1F6F5B
Deep green
Used for main buttons, navigation highlights, and important links.

Secondary colour:
#D97706
Warm amber
Used for accents, prices, icons, and selected states.

Background:
#FAFAF7
Warm off-white
Used as the main page background.

Surface:
#FFFFFF
White
Used for cards, forms, and content sections.

Main text:
#1F2933
Dark charcoal
Used for headings and body text.

Muted text:
#6B7280
Grey
Used for helper text, dates, descriptions, and secondary labels.

Border:
#E5E7EB
Light grey
Used for form fields, cards, and dividers.

Success:
#15803D
Green
Used for successful bookings and payments.

Error:
#B91C1C
Red
Used for validation errors and failed payments.

</details>

### Wireframes

---

The following wireframes were created during the planning and design phase of the project. They helped define the structure, navigation flow, and key functionality before development began.

<details>
<summary><strong>404 Error Page</strong></summary>

![404 Error Page](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-404.png?raw=true)

</details>

<details>
<summary><strong>Home Page</strong></summary>

![Home Page](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-home.png?raw=true)

</details>

<details>
<summary><strong>Base Template</strong></summary>

![Base Template](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-base.png?raw=true)

</details>

<details>
<summary><strong>User Registration</strong></summary>

![User Registration](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-account-register.png?raw=true)

</details>

<details>
<summary><strong>User Login</strong></summary>

![User Login](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-registration-login.png?raw=true)

</details>

<details>
<summary><strong>Account Dashboard</strong></summary>

![Account Dashboard](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-accounts-dashboard.png?raw=true)

</details>

<details>
<summary><strong>Tutor List</strong></summary>

![Tutor List](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-tutors-tutorlist.png?raw=true)

</details>

<details>
<summary><strong>Tutor Detail</strong></summary>

![Tutor Detail](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-tutors-tutordetail.png?raw=true)

</details>

<details>
<summary><strong>Create / Edit Tutor Form</strong></summary>

![Tutor Form](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-tutors-tutorform.png?raw=true)

</details>

<details>
<summary><strong>Lesson Form</strong></summary>

![Lesson Form](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-tutors-lessonform.png?raw=true)

</details>

<details>
<summary><strong>Booking List</strong></summary>

![Booking List](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-bookings-list.png?raw=true)

</details>

<details>
<summary><strong>Booking Deletion Confirmation</strong></summary>

![Booking Deletion Confirmation](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-bookings-confirmdelete.png?raw=true)

</details>

<details>
<summary><strong>Checkout Success</strong></summary>

![Checkout Success](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-checkout-checkoutsuccess.png?raw=true)

</details>

<details>
<summary><strong>Checkout Cancellation</strong></summary>

![Checkout Cancellation](https://github.com/JamesBirchall-dev/imagehost/blob/main/readme-wireframe-checkout-checkoutcancel.png?raw=true)

</details>

## Features

### Existing Features

_Description of existing features goes here._

### Future Features

_Planned features and improvements._

---

## Data Model

The application uses Django's built-in 'User' model and four custom models:

-'TutorProfile'
-'LessonType'
-'Booking'
-'Payment'

This structure supports the main user journeys in the application: registering or logging in, browsing tutors, viewing tutor details, creating and editing tutor information, booking lessons, managing bookings, and completing payments through Stripe.

---

## Data Tables

### User

The application uses Django’s built-in `User` model for authentication and account management.

| Field          | Purpose                                |
| -------------- | -------------------------------------- |
| `id`           | Primary key                            |
| `username`     | User login name                        |
| `email`        | User email address                     |
| `password`     | Hashed password                        |
| `first_name`   | Optional first name                    |
| `last_name`    | Optional last name                     |
| `is_staff`     | Allows access to Django admin if true  |
| `is_superuser` | Gives full admin permission if true    |
| `is_active`    | Controls whether the account is active |
| `date_joined`  | Date and time the account was created  |
| `last_login`   | Date and time of most recent login     |

---

### TutorProfile

Stores public tutor profile information.

| Field          | Purpose                                                 |
| -------------- | ------------------------------------------------------- |
| `id`           | Primary key                                             |
| `user_id`      | Foreign key to `User`                                   |
| `display_name` | Public tutor name shown on tutor cards and detail pages |
| `bio`          | Main tutor profile description                          |
| `experience`   | Teaching or playing experience summary                  |
| `location`     | Location or online availability                         |
| `image`        | Optional tutor profile image                            |
| `is_active`    | Controls whether the tutor appears publicly             |
| `created_at`   | Date and time the tutor profile was created             |
| `updated_at`   | Date and time the tutor profile was last updated        |

---

### LessonType

Stores the types of lessons a tutor offers.

| Field              | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| `id`               | Primary key                                         |
| `tutor_id`         | Foreign key to `TutorProfile`                       |
| `title`            | Lesson title, for example Beginner                  |
| `description`      | Lesson description                                  |
| `duration_minutes` | Lesson length in minutes                            |
| `skill_level`      | Beginner, Intermediate, Advanced, or All Levels     |
| `price`            | Lesson price                                        |
| `is_available`     | Controls whether the lesson can currently be booked |
| `created_at`       | Date and time the lesson was created                |
| `updated_at`       | Date and time the lesson was last updated           |

---

### Booking

Stores lesson bookings made by students.

| Field            | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `id`             | Primary key                                  |
| `student_id`     | Foreign key to `User`                        |
| `lesson_type_id` | Foreign key to `LessonType`                  |
| `booking_date`   | Date of the booked lesson                    |
| `booking_time`   | Time of the booked lesson                    |
| `status`         | Pending, Confirmed, or Cancelled             |
| `notes`          | Optional notes from the student to the tutor |
| `created_at`     | Date and time the booking was created        |
| `updated_at`     | Date and time the booking was last updated   |

---

### Payment

Stores checkout and payment information.

| Field                   | Purpose                                           |
| ----------------------- | ------------------------------------------------- |
| `id`                    | Primary key                                       |
| `booking_id`            | One-to-one relationship with `Booking`            |
| `user_id`               | Foreign key to `User`                             |
| `amount`                | Amount paid or due                                |
| `stripe_checkout_id`    | Stripe checkout session reference                 |
| `stripe_payment_status` | Stripe payment status, for example paid or unpaid |
| `paid`                  | Whether the payment was successful                |
| `created_at`            | Date and time the payment record was created      |
| `updated_at`            | Date and time the payment record was last updated |

---

## Relationships

| Model A        | Relationship | Model B        | Explanation                                     |
| -------------- | ------------ | -------------- | ----------------------------------------------- |
| `User`         | One-to-one   | `TutorProfile` | A registered user can create one tutor profile. |
| `TutorProfile` | One-to-many  | `LessonType`   | One tutor can offer multiple lesson types.      |
| `User`         | One-to-many  | `Booking`      | A student can make multiple bookings.           |
| `LessonType`   | One-to-many  | `Booking`      | One lesson type can be booked many times.       |
| `Booking`      | One-to-one   | `Payment`      | Each booking has one payment record.            |
| `User`         | One-to-many  | `Payment`      | A user can make multiple payments.              |

---

## Entity Relationship Diagram

```text
User
----
id
username
email
password
first_name
last_name
is_staff
is_superuser
is_active
date_joined
last_login
        |
        | one-to-one
        v
TutorProfile
------------
id
user_id
display_name
bio
experience
location
image
is_active
created_at
updated_at
        |
        | one-to-many
        v
LessonType
----------
id
tutor_id
title
description
duration_minutes
skill_level
price
is_available
created_at
updated_at
        |
        | one-to-many
        v
Booking
-------
id
student_id  ------------> User
lesson_type_id
booking_date
booking_time
status
notes
created_at
updated_at
        |
        | one-to-one
        v
Payment
-------
id
booking_id
user_id  ----------------> User
amount
stripe_checkout_id
stripe_payment_status
paid
created_at
updated_at
```

## Project Management

(https://github.com/users/JamesBirchall-dev/projects/7)

---

## Technologies Used

### Dependencies

Django Main web framework
gunicorn Production server for Heroku
whitenoise Serves static files on Heroku
dj-database-url Reads Heroku DATABASE_URL easily
psycopg2-binary PostgreSQL database adapter
stripe Stripe payment integration
python-decouple Environment variable handling
coverage Test coverage reporting

_List of main technologies, frameworks, and tools._

---

## Testing

### Manual Testing

#### Feature - Accounts (local)

<details>
<summary><strong> Anonymous Access to Registration Page </strong></summary>

Test:

from django.test import TestCase
from django.urls import reverse

class AccountViewTests(TestCase):
"""Tests for the account-related views."""

    def test_register_page_loads_for_anonymous_user(self):
        """Test that the registration page loads for anonymous users."""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test accounts
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\handlers\base.py:62: UserWarning: No directory at: C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\staticfiles\
 mw_instance = middleware(adapted_handler)
.

---

Ran 1 test in 0.190s

OK
Destroying test database for alias 'default'...

NOTE: Static file error showing due to not being configured yet, updated with deployment test following local test for the feature.

_PASS_

</details>

<details>
<summary><strong> Authenticated Users Redirect From the Registration Page </strong></summary>

Import added:
from django.contrib.auth.models import User

Test:
def test_register_page_redirects_for_authenticated_user(self):
"""Test that authenticated users are redirected from the reg page.""" # Create and log in a test user
User.objects.create_user(
username="testuser",
email="testuser@example.com",
password="testpassword123!"
)

        self.client.login(username="testuser", password="testpassword123!")

        response = self.client.get(reverse("register"))

        self.assertRedirects(response, reverse("dashboard"))

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test accounts.tests.AccountViewTests.test_register_page_redirects_for_authenticated_user
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\handlers\base.py:62: UserWarning: No directory at: C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\staticfiles\
 mw_instance = middleware(adapted_handler)
.

---

Ran 1 test in 0.907s

OK

Destroying test database for alias 'default'...

NOTE: Static file error showing due to not being configured yet, updated with deployment test following local test for the feature.

_PASS_

</details>

<details>
<summary><strong> Account dashboard page loads for autheticated users.</strong></summary>
Test: 
    def test_account_dashboard_page_loads_for_authenticated_user(self):
        """Test that the account dashboard page loads for auth users."""
        # Create and log in a test user
        User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123!"
        )

        self.client.login(username="testuser", password="testpassword123!")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/dashboard.html")
        self.assertContains(response, "Dashboarduser")

# Result:

FAIL: test_account_dashboard_page_loads_for_authenticated_user (accounts.tests.AccountViewTests.test_account_dashboard_page_loads_for_authenticated_user)
Test that the account dashboard page loads for auth users.

---

Traceback (most recent call last):
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\accounts\tests.py", line 43, in test_account_dashboard_page_loads_for_authenticated_user
self.assertContains(response, "Dashboarduser")
AssertionError: False is not true : Couldn't find 'Dashboarduser' in the following response
b'\n<!DOCTYPE html>\n<html lang="en">\n<head>\n <meta charset="UTF-8">\n <meta name="description" content="Tutor Connect helps students find, book, and pay for guitar lessons with trusted tutors.">\n <meta name="viewport" content="width=device-width, initial-scale=1.0">\n <title>\n Dashboard | GuitarTutorHub\n</title>\n <link rel="preconnect" href="https://fonts.googleapis.com">\n <link rel="stylesheet" href="/static/css/styles.css">\n</head>\n<body>\n <header class="site-header">\n <a class="site-logo" href="/">Tutor Connect</a>\n <nav class="site-nav" aria-label="Main navigation">\n <a href="/">Home</a>\n <a href="/tutors/">Tutors</a>\n \n <a href="/tutors/accounts/dashboard/">Dashboard</a>\n <a href="/bookings/">My Bookings</a>\n <form class="logout-form" action="/tutors/accounts/logout/" method="post">\n <input type="hidden" name="csrfmiddlewaretoken" value="XQZCcmAAc25aERtyzYDhtpWqxLWsCB7QcOOSxw4AZrTyjtaSiYUQ3ZGd15Y7ewXe">\n <button type="submit">Log out</button>\n </form>\n \n </nav>\n </header>\n\n \n\n <main class="site-main">\n \n<!-- Main dashboard content begins -->\n\n<section class="container">\n <!-- Main container for dashboard content -->\n\n <h1>My Dashboard</h1>\n\n <!-- Display a personalised welcome message using the logged-in user\'s username -->\n <p>Welcome back, testuser.</p>\n\n <!-- Navigation buttons providing quick access to key features -->\n <div class="button-row">\n\n <!-- Link to view all available guitar tutors -->\n <a class="btn btn-primary" href="/tutors/">\n Browse Tutors\n </a>\n\n <!-- Link to view the user\'s lesson bookings -->\n <a class="btn btn-outline" href="/bookings/">\n My Bookings\n </a>\n\n <!-- Link to create a new tutor profile -->\n <a class="btn btn-secondary" href="/tutors/create/">\n Create Tutor Profile\n </a>\n\n </div>\n</section>\n\n\n </main>\n\n <footer class="site-footer">\n <p>&copy; Tutor Connect. All rights reserved.</p>\n </footer>\n</body>\n</html>'

---

Ran 3 tests in 1.863s

FAILED (failures=1)

Issue: self.assertContains(response, "Dashboarduser") incorrect assertion on page.
Fix: self.assertContains(response, "My Dashboard")

Found 3 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\handlers\base.py:62: UserWarning: No directory at: C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\staticfiles\
 mw_instance = middleware(adapted_handler)
...

---

Ran 3 tests in 1.835s

OK
Destroying test database for alias 'default'...

_PASS_

NOTE: Static file error showing due to not being configured yet, updated with deployment test following local test for the feature.

</details>

<details>
<summary><strong> Registration rejecting missmatched passwords</strong></summary>

Test:

    def test_registration_rejects_missmatched_passwords(self):
        """Test that registration fails if passwords don't match."""
        response = self.client.post(reverse("register"), {
            "username": "baduser",
            "email": "baduser@example.com",
            "password1": "password123!",
            "password2": "differentpassword456!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="baduser").exists())
        self.assertContains(response, "The two password fields didn’t match.")

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test accounts.tests.AccountViewTests.test_registration_rejects_missmatched_passwords
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\handlers\base.py:62: UserWarning: No directory at: C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\staticfiles\
 mw_instance = middleware(adapted_handler)
.

---

Ran 1 test in 0.061s

OK
Destroying test database for alias 'default'...

_PASS_
NOTE: Static file error showing due to not being configured yet, updated with deployment test following local test for the feature.

</details>

#### Feature - Tutors (local)

<details>
<summary><strong> Create Profile</strong></summary>

Model:

from django.conf import settings
from django.db import models

# Create your models here.

class TutorProfile(models.Model):
"""Model representing a tutor's profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile"
    )

    def __str__(self):
        return str(self.user)

Test:
from django.contrib.auth.models import User
from django.test import TestCase
from tutors.models import TutorProfile

# Create your tests here.

class TutorProfileModelTest(TestCase):
"""Tests for the TutorProfile model."""

    def setUp(self):
        """Set up a user for testing."""
        self.user = User.objects.create_user(
            username="testuser",
            email="tutor@example.com",
            password="testpassword123!",
            )

    def test_tutor_profile_creation(self):
        """Test that a TutorProfile can be created for a user."""
        profile = TutorProfile.objects.create(user=self.user)
        self.assertEqual(profile.user, self.user)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.664s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Profile information storage</strong></summary>

model:

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_profile"
    )
    display_name = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name

Test:

    def test_tutor_profile_stores_information(self):
        """Test that TutorProfile can store and retrieve information."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertEqual(profile.display_name, "Test Tutor")
        self.assertEqual(profile.bio, "Experienced tutor in math and science.")
        self.assertEqual(profile.experience, "5 years of tutoring experience.")
        self.assertEqual(profile.location, "Online")

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..

---

Ran 2 tests in 1.249s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Profile image</summary>

model update:

    image = models.ImageField(
        upload_to="tutor_profiles/",
        blank=True,
        null=True,
    )

test:

    def test_image_field_is_optional(self):
        """Test that the image field can be left blank."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertIsNone(profile.image)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...

---

Ran 3 tests in 2.025s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> User Active Status</summary>

Model:
is_active = models.BooleanField(default=True)

Test:
def test_is_active_default(self):
"""Test that the is_active field defaults to True."""
profile = TutorProfile.objects.create(
user=self.user,
display_name="Test Tutor",
bio="Experienced tutor in math and science.",
experience="5 years of tutoring experience.",
location="Online"
)
self.assertTrue(profile.is_active)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.TutorProfileModelTest.test_is_active_default
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.655s

OK
Destroying test database for alias 'default'...

_PASS_

### Validator Testing

_Automated validation and tools used._

### Bugs

_Known issues and how they were addressed._

---

## Deployment

_Deployment instructions and environment details._

---

## Stripe Payments

_Details about Stripe integration and payment flow._

---

## Security Features

_Security measures and best practices implemented._

---

## Credits

### Code

_Attributions for code snippets or libraries._

### Content

_Sources for written content or inspiration._

### Media

_Image, icon, and media attributions._

---

## Acknowledgements

_Special thanks and acknowledgements._
