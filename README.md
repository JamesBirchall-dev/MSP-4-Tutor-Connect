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
- [Admin](#admin)
- [Security](#security)
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
'# 1F6F5B'
Deep green
Used for main buttons, navigation highlights, and important links.

Secondary colour:
'# D97706'
Warm amber
Used for accents, prices, icons, and selected states.

Background:
'# FAFAF7'
Warm off-white
Used as the main page background.

Surface:
'# FFFFFF'
White
Used for cards, forms, and content sections.

Main text:
'# 1F2933'
Dark charcoal
Used for headings and body text.

Muted text:
'# 6B7280'
Grey
Used for helper text, dates, descriptions, and secondary labels.

Border:
'# E5E7EB'
Light grey
Used for form fields, cards, and dividers.

Success:
'# 15803D'
Green
Used for successful bookings and payments.

Error:
'# B91C1C'
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

Tutor Connect is a full-stack tutoring marketplace that allows students to discover tutors, book scheduled lessons and securely complete payment through Stripe. The platform provides separate functionality for students and tutors while ensuring users can only access and manage their own content.

---

### Accounts

#### User Registration

Users can create an account using the custom registration form. Registration validates user input and securely stores account credentials using Django's built-in authentication system.

Once registration is complete the user is automatically logged in and redirected to their dashboard.

Features include:

- Secure password hashing
-Automatic login after registration
-Validation for duplicate usernames and email addresses
-Success messaging following account creation

---

#### Dashboard

Each registered user has access to a personalised dashboard.

Student users can:

Browse tutors
View all available lessons
Access and manage their bookings

Users with a Tutor Profile additionally gain access to tutor management features including:

Edit tutor profile
-View upcoming scheduled lessons
-Create new lesson listings
-Manage existing lessons

The dashboard dynamically changes depending on whether the logged-in user has created a Tutor Profile.

---

### Tutor Profiles

Users wishing to offer lessons can create a Tutor Profile.

Each tutor profile contains:

- Display name
- Biography
- Teaching experience
- Location
- Profile image
- Active status

If no profile image has been uploaded a default placeholder image is displayed.

Tutor profiles are publicly viewable and include a summary of the tutor together with their upcoming available lessons.

---

### Lessons (Marketplace)

The lesson system was redesigned during development to more closely reflect a real-world tutoring platform.

Instead of allowing students to request arbitrary dates and times, tutors now create scheduled lesson slots which students can browse and book.

Each lesson includes:

- Lesson title
- Subject category
- Subject
- Skill level
- Description
- Duration
- Price
- Scheduled date
- Scheduled time
- Availability status

Lessons are automatically linked to the tutor who created them.

---

### Subject Categories

Subjects are selected from predefined choices rather than free-text entry, providing consistent filtering and preventing duplicate spellings.

Categories currently include:

- Academic Subjects
- Languages
- Music
- Creative Arts
- Technology
- Study & Life Skills

Each category contains multiple predefined subjects allowing accurate searching and filtering.

---

### Browse All Lessons

Students can browse lessons from every tutor through the marketplace.

Features include:

- Pagination
- Subject filtering
- Skill level filtering
- Lesson title search
- Sorting by:
  - Date
  - Lowest price
  - Highest price
  - Recently added

Only lessons that are currently available are displayed.

Past lessons are automatically hidden from the public lesson marketplace.

Lessons with pending or confirmed bookings are also excluded to prevent double-booking.

---

### Tutor Lesson Management

Tutors can:

- Create lessons
- Edit lessons
- Delete lessons
- View all lessons they have created

Upcoming lessons are displayed on both the tutor dashboard and public tutor profile.

Success messages are displayed following lesson creation, editing and deletion.

---

### Bookings

Students can create bookings for available lessons.

Each booking stores:

- Student
- Lesson
- Booking date
- Booking time
- Notes
- Booking status

Booking statuses include:

- Pending
- Confirmed
- Cancelled

Students may:

- View booking details
- Update pending bookings
- Cancel bookings

Access controls ensure users can only manage their own bookings.

---

### Checkout

Tutor Connect integrates with Stripe Checkout to provide secure payment processing.

The checkout flow consists of:

Booking

↓

Booking Review

↓

Stripe Checkout

↓

Payment Confirmation

Before payment users can review:

- Tutor
- Lesson
- Date
- Time
- Duration
- Price

Successful payments automatically update the booking payment status through Stripe webhooks.

---

### Security and checks

Tutor Connect applies authentication and ownership checks throughout the application.

Security measures include:

- Login required decorators
- Object ownership validation
- Protection against editing other users' content
- CSRF protection
- Secure password hashing
- Server-side form validation
- Environment variables for secret configuration
- Custom 403 and 500 error pages

---

### User Experience

The application provides consistent feedback using Django's messaging framework.

Examples include:

- Account created successfully
- Tutor profile updated
- Lesson created
- Lesson updated
- Lesson deleted
- Booking updated
- Booking cancelled

Custom placeholder images ensure tutor profiles remain visually consistent even when no image has been uploaded.

---

#### Responsive Design

Tutor Connect has been designed with a mobile-first responsive layout.

The interface adapts across desktop, tablet and mobile devices using CSS Grid and Flexbox layouts.

Responsive components include:

- Navigation
- Dashboard
- Tutor cards
- Lesson marketplace
- Booking pages
- Forms
- Checkout pages

---

## Testing Coverage

The Tutors feature is covered by automated tests ensuring:

- Tutor lesson list loads successfully
- Correct template rendering
- Search returns expected lesson results
- Subject filtering works correctly
- Skill level filtering works correctly
- Filtered querysets correctly update displayed results

---

## Example User Flow

1. User visits a tutor profile
2. User navigates to **“View Lessons”**
3. User searches for `"Math"`
4. User filters by `"Beginner"`
5. User browses paginated results
6. User selects a lesson to proceed to booking (future feature)

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

(<https://github.com/users/JamesBirchall-dev/projects/7>)

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
Manual Testing
Deployed site: Tutor Connect
Testing Objectives
The purpose of this test plan is to confirm that Tutor Connect works as expected for visitors, registered users, tutors and administrators. Testing covers navigation, authentication, tutor profiles, lesson browsing, bookings, checkout, security rules, responsive design and deployed functionality.
Full manual testing evidence is also recorded in the manual testing spreadsheet.
> Screenshots are placed inside expandable sections. Click each heading to expand the evidence, then click the image to open it at full size.

#### Visitor Testing
<details>
<summary>Visitor Testing summary table</summary>
<a href="https://github.com/user-attachments/assets/e25dafe1-1813-4491-9a8a-686ce89f7bf2">
  <img src="https://github.com/user-attachments/assets/e25dafe1-1813-4491-9a8a-686ce89f7bf2" alt="Visitor Testing summary table" width="700">
</a>
</details>
<details>
<summary>Homepage</summary>
<a href="https://github.com/user-attachments/assets/a80de12d-9a43-41e9-952b-f3de24e54aca">
  <img src="https://github.com/user-attachments/assets/a80de12d-9a43-41e9-952b-f3de24e54aca" alt="Homepage" width="700">
</a>
</details>
<details>
<summary>Image</summary>
<a href="https://github.com/user-attachments/assets/2e9cca0a-c6c6-4de9-8a3b-2415663d5210">
  <img src="https://github.com/user-attachments/assets/2e9cca0a-c6c6-4de9-8a3b-2415663d5210" alt="Image" width="700">
</a>
</details>
<details>
<summary>Lessons:</summary>
<a href="https://github.com/user-attachments/assets/615e38f9-042d-40b2-bdbc-a4e79e5c7a1b">
  <img src="https://github.com/user-attachments/assets/615e38f9-042d-40b2-bdbc-a4e79e5c7a1b" alt="Lessons:" width="700">
</a>
</details>
<details>
<summary>Lessons filtered:</summary>
<a href="https://github.com/user-attachments/assets/a3e27060-3d2b-4c11-bc30-13b2dd0eb362">
  <img src="https://github.com/user-attachments/assets/a3e27060-3d2b-4c11-bc30-13b2dd0eb362" alt="Lessons filtered:" width="700">
</a>
</details>
<details>
<summary>Image (2)</summary>
<a href="https://github.com/user-attachments/assets/97320ce4-5764-44af-a918-e697f8063f8f">
  <img src="https://github.com/user-attachments/assets/97320ce4-5764-44af-a918-e697f8063f8f" alt="Image" width="700">
</a>
</details>
<details>
<summary>Attempt logged out booking</summary>
<a href="https://github.com/user-attachments/assets/bb558c89-fe45-40fd-ba1f-30e637a907b1">
  <img src="https://github.com/user-attachments/assets/bb558c89-fe45-40fd-ba1f-30e637a907b1" alt="Attempt logged out booking" width="700">
</a>
</details>
<details>
<summary>Tutors:</summary>
<a href="https://github.com/user-attachments/assets/34e6cfa7-74e7-4430-9121-a49a11710d20">
  <img src="https://github.com/user-attachments/assets/34e6cfa7-74e7-4430-9121-a49a11710d20" alt="Tutors:" width="700">
</a>
</details>
<details>
<summary>Image (3)</summary>
<a href="https://github.com/user-attachments/assets/52b521fd-8a01-4107-bbe5-6efb96c2b3b0">
  <img src="https://github.com/user-attachments/assets/52b521fd-8a01-4107-bbe5-6efb96c2b3b0" alt="Image" width="700">
</a>
</details>

#### Account Testing
<details>
<summary>Image (4)</summary>
<a href="https://github.com/user-attachments/assets/e712e45f-be78-4d5c-b541-71ff7001e8f6">
  <img src="https://github.com/user-attachments/assets/e712e45f-be78-4d5c-b541-71ff7001e8f6" alt="Image" width="700">
</a>
</details>
<details>
<summary>Registration validation</summary>
<a href="https://github.com/user-attachments/assets/cedb4921-5396-450d-95e3-46402e5c57cf">
  <img src="https://github.com/user-attachments/assets/cedb4921-5396-450d-95e3-46402e5c57cf" alt="Registration validation" width="700">
</a>
</details>
<details>
<summary>Successful registration</summary>
<a href="https://github.com/user-attachments/assets/39affca8-82c7-4c95-8d48-ff4b9a206fd7">
  <img src="https://github.com/user-attachments/assets/39affca8-82c7-4c95-8d48-ff4b9a206fd7" alt="Successful registration" width="700">
</a>
</details>
<details>
<summary>Login validation</summary>
<a href="https://github.com/user-attachments/assets/05f0afa6-97bd-4c29-9efc-4fc9fa554119">
  <img src="https://github.com/user-attachments/assets/05f0afa6-97bd-4c29-9efc-4fc9fa554119" alt="Login validation" width="700">
</a>
</details>
<details>
<summary>Successful login</summary>
<a href="https://github.com/user-attachments/assets/c490c155-f242-4bd1-9b93-958635663b43">
  <img src="https://github.com/user-attachments/assets/c490c155-f242-4bd1-9b93-958635663b43" alt="Successful login" width="700">
</a>
</details>
<details>
<summary>Logout</summary>
<a href="https://github.com/user-attachments/assets/1c0df439-4686-4dae-a094-06c970f99585">
  <img src="https://github.com/user-attachments/assets/1c0df439-4686-4dae-a094-06c970f99585" alt="Logout" width="700">
</a>
</details>

#### Tutor Profile Testing
<details>
<summary>Image (5)</summary>
<a href="https://github.com/user-attachments/assets/7d701a3b-bb4e-4ca4-830c-664592c4223e">
  <img src="https://github.com/user-attachments/assets/7d701a3b-bb4e-4ca4-830c-664592c4223e" alt="Image" width="700">
</a>
</details>
<details>
<summary>Create Tutor Profile:</summary>
<a href="https://github.com/user-attachments/assets/338aca14-52e8-42a5-8f58-6f014e79f8ae">
  <img src="https://github.com/user-attachments/assets/338aca14-52e8-42a5-8f58-6f014e79f8ae" alt="Create Tutor Profile:" width="700">
</a>
</details>
<details>
<summary>Image (6)</summary>
<a href="https://github.com/user-attachments/assets/0bd42c1d-0e9c-458b-b719-d44af12c59ba">
  <img src="https://github.com/user-attachments/assets/0bd42c1d-0e9c-458b-b719-d44af12c59ba" alt="Image" width="700">
</a>
</details>
<details>
<summary>Tutor profile validation</summary>
<a href="https://github.com/user-attachments/assets/07ad3277-d540-4604-be18-7bffdcefa1c8">
  <img src="https://github.com/user-attachments/assets/07ad3277-d540-4604-be18-7bffdcefa1c8" alt="Tutor profile validation" width="700">
</a>
</details>
<details>
<summary>Tutor profile update</summary>
<a href="https://github.com/user-attachments/assets/514eada1-b39d-4054-857a-e7fba9ea5568">
  <img src="https://github.com/user-attachments/assets/514eada1-b39d-4054-857a-e7fba9ea5568" alt="Tutor profile update" width="700">
</a>
</details>
<details>
<summary>Profile placeholder image</summary>
<a href="https://github.com/user-attachments/assets/96130c74-1403-4910-b08c-ba58a425302a">
  <img src="https://github.com/user-attachments/assets/96130c74-1403-4910-b08c-ba58a425302a" alt="Profile placeholder image" width="700">
</a>
</details>
<details>
<summary>Lesson and contact information displayed in confirmed bookings</summary>
<a href="https://github.com/user-attachments/assets/454cf75b-74a2-4754-9d36-5de446bb05a4">
  <img src="https://github.com/user-attachments/assets/454cf75b-74a2-4754-9d36-5de446bb05a4" alt="Lesson and contact information displayed in confirmed bookings" width="700">
</a>
</details>

#### Dashboard Testing
<details>
<summary>Image (7)</summary>
<a href="https://github.com/user-attachments/assets/0ac1ad29-4541-4502-98fa-c2b506883c76">
  <img src="https://github.com/user-attachments/assets/0ac1ad29-4541-4502-98fa-c2b506883c76" alt="Image" width="700">
</a>
</details>
<details>
<summary>Student login landing page, shows create profile CTA:</summary>
<a href="https://github.com/user-attachments/assets/c437ee1e-4b53-4630-be16-208193e68b47">
  <img src="https://github.com/user-attachments/assets/c437ee1e-4b53-4630-be16-208193e68b47" alt="Student login landing page, shows create profile CTA:" width="700">
</a>
</details>
<details>
<summary>Tutor dashboard and upcoming lessons</summary>
<a href="https://github.com/user-attachments/assets/dbf7227d-e648-4258-be87-4a6be30437da">
  <img src="https://github.com/user-attachments/assets/dbf7227d-e648-4258-be87-4a6be30437da" alt="Tutor dashboard and upcoming lessons" width="700">
</a>
</details>

#### Lesson Testing
<details>
<summary>Image (8)</summary>
<a href="https://github.com/user-attachments/assets/359467ae-ce36-4494-bfcd-cde19eab956a">
  <img src="https://github.com/user-attachments/assets/359467ae-ce36-4494-bfcd-cde19eab956a" alt="Image" width="700">
</a>
</details>
<details>
<summary>Create new lesson</summary>
<a href="https://github.com/user-attachments/assets/f0a50ce6-766e-4152-9107-17093b32276f">
  <img src="https://github.com/user-attachments/assets/f0a50ce6-766e-4152-9107-17093b32276f" alt="Create new lesson" width="700">
</a>
</details>
<details>
<summary>Edit lesson</summary>
<a href="https://github.com/user-attachments/assets/ebf05c70-3ae1-4a2c-9ca7-790bcba05d3c">
  <img src="https://github.com/user-attachments/assets/ebf05c70-3ae1-4a2c-9ca7-790bcba05d3c" alt="Edit lesson" width="700">
</a>
</details>
<details>
<summary>Image (9)</summary>
<a href="https://github.com/user-attachments/assets/a1f5a570-23be-45d1-ac61-b260c1c556e8">
  <img src="https://github.com/user-attachments/assets/a1f5a570-23be-45d1-ac61-b260c1c556e8" alt="Image" width="700">
</a>
</details>
<details>
<summary>Delete Lesson</summary>
<a href="https://github.com/user-attachments/assets/a095177a-ebed-4e7f-ad09-ece9006dd907">
  <img src="https://github.com/user-attachments/assets/a095177a-ebed-4e7f-ad09-ece9006dd907" alt="Delete Lesson" width="700">
</a>
</details>
<details>
<summary>Image (10)</summary>
<a href="https://github.com/user-attachments/assets/54f794e0-49d8-49e1-a51d-59704351d976">
  <img src="https://github.com/user-attachments/assets/54f794e0-49d8-49e1-a51d-59704351d976" alt="Image" width="700">
</a>
</details>
<details>
<summary>Lesson form validation</summary>
<a href="https://github.com/user-attachments/assets/7404f7c2-0220-4fe7-b73a-1534afbcfc0c">
  <img src="https://github.com/user-attachments/assets/7404f7c2-0220-4fe7-b73a-1534afbcfc0c" alt="Lesson form validation" width="700">
</a>
</details>
<details>
<summary>not available</summary>
<a href="https://github.com/user-attachments/assets/1925a8c7-bd33-492e-b7ad-f8d7ecb07c6a">
  <img src="https://github.com/user-attachments/assets/1925a8c7-bd33-492e-b7ad-f8d7ecb07c6a" alt="not available" width="700">
</a>
</details>
<details>
<summary>Edit Blocked</summary>
<a href="https://github.com/user-attachments/assets/2d8b25a8-b338-4b3e-a7de-d91a07c9a5d7">
  <img src="https://github.com/user-attachments/assets/2d8b25a8-b338-4b3e-a7de-d91a07c9a5d7" alt="Edit Blocked" width="700">
</a>
</details>
<details>
<summary>Unavailable lesson not shown in lesson filter</summary>
<a href="https://github.com/user-attachments/assets/b33c0463-7d2e-4eb1-aded-cf1ea59c0477">
  <img src="https://github.com/user-attachments/assets/b33c0463-7d2e-4eb1-aded-cf1ea59c0477" alt="Unavailable lesson not shown in lesson filter" width="700">
</a>
</details>
<details>
<summary>Update to past date</summary>
<a href="https://github.com/user-attachments/assets/0ec36a1e-2ed0-4cfc-bb21-f83ed842a750">
  <img src="https://github.com/user-attachments/assets/0ec36a1e-2ed0-4cfc-bb21-f83ed842a750" alt="Update to past date" width="700">
</a>
</details>
<details>
<summary>Pagination showing and working for 10 or more lessons</summary>
<a href="https://github.com/user-attachments/assets/e68961c2-95b3-473b-8019-b004861ba4f7">
  <img src="https://github.com/user-attachments/assets/e68961c2-95b3-473b-8019-b004861ba4f7" alt="Pagination showing and working for 10 or more lessons" width="700">
</a>
</details>
<details>
<summary>Image (11)</summary>
<a href="https://github.com/user-attachments/assets/cce75a57-aab9-4ad7-b78f-d97ebf6fd665">
  <img src="https://github.com/user-attachments/assets/cce75a57-aab9-4ad7-b78f-d97ebf6fd665" alt="Image" width="700">
</a>
</details>

#### Booking Test
<details>
<summary>Booking Testing summary table</summary>
<a href="https://github.com/user-attachments/assets/cef804c6-e636-4b9b-9f9b-d1fa4cf7056d">
  <img src="https://github.com/user-attachments/assets/cef804c6-e636-4b9b-9f9b-d1fa4cf7056d" alt="Booking Testing summary table" width="700">
</a>
</details>
<details>
<summary>Book a lesson</summary>
<a href="https://github.com/user-attachments/assets/8e5841bc-8f14-40ad-868a-dc90f5d09f2d">
  <img src="https://github.com/user-attachments/assets/8e5841bc-8f14-40ad-868a-dc90f5d09f2d" alt="Book a lesson" width="700">
</a>
</details>
Issue: Obsolete text as booking is fixed slot.
<details>
<summary>Bookings shown for user in dashboard</summary>
<a href="https://github.com/user-attachments/assets/a3a5ac16-cee7-4a34-b05d-cd8bbf7e0fb8">
  <img src="https://github.com/user-attachments/assets/a3a5ac16-cee7-4a34-b05d-cd8bbf7e0fb8" alt="Bookings shown for user in dashboard" width="700">
</a>
</details>
<details>
<summary>View booking details</summary>
<a href="https://github.com/user-attachments/assets/9746262a-f8f4-448c-83aa-2618da197cd1">
  <img src="https://github.com/user-attachments/assets/9746262a-f8f4-448c-83aa-2618da197cd1" alt="View booking details" width="700">
</a>
</details>
<details>
<summary>Cancel booking</summary>
<a href="https://github.com/user-attachments/assets/6102480a-ed77-4ff6-886c-7b3c7f70eda5">
  <img src="https://github.com/user-attachments/assets/6102480a-ed77-4ff6-886c-7b3c7f70eda5" alt="Cancel booking" width="700">
</a>
</details>
<details>
<summary>Attempt to access another user&#x27;s booking</summary>
<a href="https://github.com/user-attachments/assets/2878041e-7321-4a34-91a6-810bded25601">
  <img src="https://github.com/user-attachments/assets/2878041e-7321-4a34-91a6-810bded25601" alt="Attempt to access another user&#x27;s booking" width="700">
</a>
</details>

#### Checkout Test
<details>
<summary>Checkout review displays correct booking information</summary>
<a href="https://github.com/user-attachments/assets/af4a8c2b-2099-46c5-8f10-353950eb9dba">
  <img src="https://github.com/user-attachments/assets/af4a8c2b-2099-46c5-8f10-353950eb9dba" alt="Checkout review displays correct booking information" width="700">
</a>
</details>
<details>
<summary>Redirect to Stripe Checkout</summary>
<a href="https://github.com/user-attachments/assets/7bc2da55-cfef-4b1c-8cf6-0841449168fc">
  <img src="https://github.com/user-attachments/assets/7bc2da55-cfef-4b1c-8cf6-0841449168fc" alt="Redirect to Stripe Checkout" width="700">
</a>
</details>
<details>
<summary>Payment success page</summary>
<a href="https://github.com/user-attachments/assets/31816c73-748e-4ae5-8c01-25029aac350c">
  <img src="https://github.com/user-attachments/assets/31816c73-748e-4ae5-8c01-25029aac350c" alt="Payment success page" width="700">
</a>
</details>
<details>
<summary>Booking status confirmed after payment</summary>
<a href="https://github.com/user-attachments/assets/77913c73-b042-44da-89c6-4d79ef6206aa">
  <img src="https://github.com/user-attachments/assets/77913c73-b042-44da-89c6-4d79ef6206aa" alt="Booking status confirmed after payment" width="700">
</a>
</details>
<details>
<summary>Payment cancelled</summary>
<a href="https://github.com/user-attachments/assets/a06397f7-08ae-4b8d-a617-52124f3a1868">
  <img src="https://github.com/user-attachments/assets/a06397f7-08ae-4b8d-a617-52124f3a1868" alt="Payment cancelled" width="700">
</a>
</details>
<details>
<summary>Attempt to access another user&#x27;s checkout</summary>
<a href="https://github.com/user-attachments/assets/cdd3d994-756b-456e-b4bf-4659d111ae74">
  <img src="https://github.com/user-attachments/assets/cdd3d994-756b-456e-b4bf-4659d111ae74" alt="Attempt to access another user&#x27;s checkout" width="700">
</a>
</details>

#### Admin Testing
<details>
<summary>Admin Testing summary table</summary>
<a href="https://github.com/user-attachments/assets/45758f6a-fc4e-4edd-a07a-f5ab2214f8de">
  <img src="https://github.com/user-attachments/assets/45758f6a-fc4e-4edd-a07a-f5ab2214f8de" alt="Admin Testing summary table" width="700">
</a>
</details>
<details>
<summary>Admin dashboard loads</summary>
<a href="https://github.com/user-attachments/assets/bf38b05f-4740-45bb-99c3-094b5d00e896">
  <img src="https://github.com/user-attachments/assets/bf38b05f-4740-45bb-99c3-094b5d00e896" alt="Admin dashboard loads" width="700">
</a>
</details>
<details>
<summary>Tutor profile search and filter</summary>
<a href="https://github.com/user-attachments/assets/a0187d67-841e-439a-b727-dd311d2bb327">
  <img src="https://github.com/user-attachments/assets/a0187d67-841e-439a-b727-dd311d2bb327" alt="Tutor profile search and filter" width="700">
</a>
</details>
<details>
<summary>Lesson type search and filter</summary>
<a href="https://github.com/user-attachments/assets/eaf8ec69-26ac-439e-afd7-21e9a4661f71">
  <img src="https://github.com/user-attachments/assets/eaf8ec69-26ac-439e-afd7-21e9a4661f71" alt="Lesson type search and filter" width="700">
</a>
</details>
<details>
<summary>Booking admin review</summary>
<a href="https://github.com/user-attachments/assets/c5f0ada0-4fc2-4579-8583-54d79f081e8b">
  <img src="https://github.com/user-attachments/assets/c5f0ada0-4fc2-4579-8583-54d79f081e8b" alt="Booking admin review" width="700">
</a>
</details>
<details>
<summary>Payment admin shows records without secrets</summary>
<a href="https://github.com/user-attachments/assets/914f22cf-d293-472b-a789-03661696274d">
  <img src="https://github.com/user-attachments/assets/914f22cf-d293-472b-a789-03661696274d" alt="Payment admin shows records without secrets" width="700">
</a>
</details>

Security Testing
<details>
<summary>Image (12)</summary>
<a href="https://github.com/user-attachments/assets/829ba659-531e-4084-be31-1c1859750142">
  <img src="https://github.com/user-attachments/assets/829ba659-531e-4084-be31-1c1859750142" alt="Image" width="700">
</a>
</details>
<details>
<summary>Secret keys not shown in repository</summary>
<a href="https://github.com/user-attachments/assets/f99c0bec-fb08-49a7-b030-3c2c57d7da11">
  <img src="https://github.com/user-attachments/assets/f99c0bec-fb08-49a7-b030-3c2c57d7da11" alt="Secret keys not shown in repository" width="700">
</a>
</details>

Fixes
https://github.com/JamesBirchall-dev/MSP-4-Tutor-Connect/issues/49
Issue 1:
<details>
<summary>CSRF error on logout</summary>
<a href="https://github.com/user-attachments/assets/224ec610-5f43-4b14-a336-dd516d9356d6">
  <img src="https://github.com/user-attachments/assets/224ec610-5f43-4b14-a336-dd516d9356d6" alt="CSRF error on logout" width="700">
</a>
</details>

Issue:
Sometimes when logging out from dashboard this error page flags.

Troubleshooting:
<details>
<summary>Check post form in base.html to make sure csrf is called - OK</summary>
<a href="https://github.com/user-attachments/assets/dc307a5d-e612-42fd-86ec-04e11b7cdc5a">
  <img src="https://github.com/user-attachments/assets/dc307a5d-e612-42fd-86ec-04e11b7cdc5a" alt="Check post form in base.html to make sure csrf is called - OK" width="700">
</a>
</details>

Resolution:
Likely caused with copying direct link, multiple sessions.
<details>
<summary>Cleared cache and tested again - PASS</summary>
<a href="https://github.com/user-attachments/assets/5338b582-c836-4f62-a0c0-342744df1918">
  <img src="https://github.com/user-attachments/assets/5338b582-c836-4f62-a0c0-342744df1918" alt="Cleared cache and tested again - PASS" width="700">
</a>
</details>

Issue 2:

Issue:
Unable to update image in deployed, returns a 500 error page.

Cause of issue:
Cloudinary required configuration for third-party image management.

Resolution:
Cloudinary configured in Django settings and Heroku Config Vars.
Cloudinary credentials added locally via `.env` and in Heroku Config Vars.

Issue 3:
<details>
<summary>Subject and category lists not in alphabetical order</summary>
<a href="https://github.com/user-attachments/assets/189fa2a1-53b8-4a1e-b0ae-0265c544b43f">
  <img src="https://github.com/user-attachments/assets/189fa2a1-53b8-4a1e-b0ae-0265c544b43f" alt="Subject and category lists not in alphabetical order" width="700">
</a>
</details>
<details>
<summary>Image (13)</summary>
<a href="https://github.com/user-attachments/assets/3c4168ca-08e6-4fbc-baaf-37262bb30223">
  <img src="https://github.com/user-attachments/assets/3c4168ca-08e6-4fbc-baaf-37262bb30223" alt="Image" width="700">
</a>
</details>
Resolution: Updated model choice lists into alphabetical order.
<details>
<summary>Resolution: Updated model choice lists into alphabetical order.</summary>
<a href="https://github.com/user-attachments/assets/fd9c5961-2202-4afb-890b-8738dfc1fa83">
  <img src="https://github.com/user-attachments/assets/fd9c5961-2202-4afb-890b-8738dfc1fa83" alt="Resolution: Updated model choice lists into alphabetical order." width="700">
</a>
</details>
<details>
<summary>Local test: PASS</summary>
<a href="https://github.com/user-attachments/assets/b91f6e68-2312-4840-ac92-56b29615f09d">
  <img src="https://github.com/user-attachments/assets/b91f6e68-2312-4840-ac92-56b29615f09d" alt="Local test: PASS" width="700">
</a>
</details>
<details>
<summary>Image (14)</summary>
<a href="https://github.com/user-attachments/assets/b414ed05-12b7-4788-9f2b-174c40012176">
  <img src="https://github.com/user-attachments/assets/b414ed05-12b7-4788-9f2b-174c40012176" alt="Image" width="700">
</a>
</details>
<details>
<summary>Deployed test: PASS</summary>
<a href="https://github.com/user-attachments/assets/4977c464-184b-4159-8c2f-e76c676c40be">
  <img src="https://github.com/user-attachments/assets/4977c464-184b-4159-8c2f-e76c676c40be" alt="Deployed test: PASS" width="700">
</a>
</details>
<details>
<summary>Image (15)</summary>
<a href="https://github.com/user-attachments/assets/35e92cf8-9c73-4005-9f06-6b9d6d1098cc">
  <img src="https://github.com/user-attachments/assets/35e92cf8-9c73-4005-9f06-6b9d6d1098cc" alt="Image" width="700">
</a>
</details>

Issue 4:
Text displayed supports time and date editing which is now obsolete.

Resolution:
Remove text from template.
<details>
<summary>Deployed test with corrected text</summary>
<a href="https://github.com/user-attachments/assets/33834538-e9c7-4c9c-888b-607a464971ba">
  <img src="https://github.com/user-attachments/assets/33834538-e9c7-4c9c-888b-607a464971ba" alt="Deployed test with corrected text" width="700">
</a>
</details>

Issue:
<details>
<summary>Badly positioned, duplicate CTA to all lessons:</summary>
<a href="https://github.com/user-attachments/assets/4e802792-b41b-4e33-bd0f-d71f8fff9e3d">
  <img src="https://github.com/user-attachments/assets/4e802792-b41b-4e33-bd0f-d71f8fff9e3d" alt="Badly positioned, duplicate CTA to all lessons:" width="700">
</a>
</details>

Resolution:
Remove 2nd CTA from template.
<details>
<summary>Deployed fix</summary>
<a href="https://github.com/user-attachments/assets/1ad64a05-d958-4c99-aef1-99a11609eb84">
  <img src="https://github.com/user-attachments/assets/1ad64a05-d958-4c99-aef1-99a11609eb84" alt="Deployed fix" width="700">
</a>
</details>


### Automated Testing

#### Feature - Accounts

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
email="<testuser@example.com>",
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

# Result

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
<summary><strong>Profile - Creation </strong></summary>

Model:

from django.conf import settings
from django.db import models

# Create your models here

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

# Create your tests here

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
<summary><strong> Profile - information storage</strong></summary>

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
<summary><strong> Profile - image</summary>

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
<summary><strong> Profile - Active Status</summary>

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

</details>

<details>
<summary><strong> Profile - Timestamp</summary>

Models:
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

Test:

    def test_profile_has_timestamps(self):
        """Test that created_at and updated_at fields are set."""
        profile = TutorProfile.objects.create(
            user=self.user,
            display_name="Test Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online"
        )
        self.assertIsNotNone(profile.created_at)
        self.assertIsNotNone(profile.updated_at)

Results:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py makemigrations  
It is impossible to add the field 'created_at' with 'auto_now_add=True' to tutorprofile without providing a default. This is because the database needs something to populate existing rows.

1. Provide a one-off default now which will be set on all existing rows
2. Quit and manually define a default value in models.py.
    Select an option: 1
    Please enter the default value as valid Python.
    Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
    The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
    Type 'exit' to exit this prompt
    [default: timezone.now] >>>
    Migrations for 'tutors':
    tutors\migrations\0004_tutorprofile_created_at_tutorprofile_updated_at.py + Add field created_at to tutorprofile + Add field updated_at to tutorprofile
    (.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.TutorProfileModelTest.test_profile_has_timestamps
    Found 1 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    .

---

Ran 1 test in 0.626s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

_PASS_

</details>

<details>
<summary><strong> Profile - Meta (Ordering) </summary>

Model:
class Meta:
ordering = ["display_name"]

Test:

    def test_profiles_are_ordered_by_display_name(self):
        """Test that TutorProfiles are ordered by display_name."""

        user1 = User.objects.create_user(
            username="charlie",
            password="testpassword123!",
        )
        user2 = User.objects.create_user(
            username="alice",
            password="testpassword123!",
        )
        user3 = User.objects.create_user(
            username="bob",
            password="testpassword123!",
        )

        profile1 = TutorProfile.objects.create(
            user=user1,
            display_name="Charlie",
            bio="Tutor Charlie.",
            experience="3 years of tutoring experience.",
            location="Online"
        )
        profile2 = TutorProfile.objects.create(
            user=user2,
            display_name="Alice",
            bio="Tutor Alice.",
            experience="4 years of tutoring experience.",
            location="Online"
        )
        profile3 = TutorProfile.objects.create(
            user=user3,
            display_name="Bob",
            bio="Tutor Bob.",
            experience="2 years of tutoring experience.",
            location="Online"
        )
        profiles = TutorProfile.objects.all()
        self.assertEqual(profiles[0], profile2)  # Alice
        self.assertEqual(profiles[1], profile3)  # Bob
        self.assertEqual(profiles[2], profile1)  # Charlie

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.TutorProfileModelTest.test_profiles_are_ordered_by_display_name
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 2.335s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Profile - String Representation </summary>

Model:

    def __str__(self):
        return self.display_name

Test:
def test_tutor_profile_string_representation(self):
profile = TutorProfile.objects.create(
user=self.user,
display_name="Test Tutor",
bio="Experienced tutor.",
experience="5 years.",
location="Online",
)
self.assertEqual(str(profile), "Test Tutor")

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.TutorProfileModelTest.test_tutor_profile_string_representation
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.627s

OK
Destroying test database for alias 'default'...

</details>

<details>
<summary><strong> Lesson Type - saves with tutor and title  </summary>

Model:
class LessonType(models.Model):
"""
Represents a type of lesson that a tutor can offer.

    This model allows tutors to specify the subjects or topics they can teach.
    """
    tutor = models.ForeignKey(
        TutorProfile,
        on_delete=models.CASCADE,
        related_name="lesson_types"
    )
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} (Tutor: {self.tutor.display_name})"

Test:
def test_lesson_type_saves_with_tutor_annd_title(self):
"""Test that a LessonType can be created with a tutor and title."""
lesson_type = LessonType.objects.create(
tutor=self.tutor_profile,
title="Math Tutoring"
)
self.assertEqual(lesson_type.tutor, self.tutor_profile)
self.assertEqual(lesson_type.title, "Math Tutoring")
self.assertIn(lesson_type, self.tutor_profile.lesson_types.all())

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.LessonTypeModelTest.test_lesson_type_saves_with_tutor_annd_title
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.838s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Lesson Type - extended fields  </summary>

Model:
title = models.CharField(max_length=100)
description = models.TextField(blank=True)
duration_minutes = models.PositiveIntegerField(default=60)
skill_level = models.CharField(max_length=20,
choices=SKILL_CHOICES,
default="other")
price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

Test:

    def test_extended_fields_and_defaults(self):
        """Test that LessonType can be created with just required fields."""
        lesson_type = LessonType.objects.create(
            tutor=self.tutor_profile,
            title="Beginner Science Tutoring",
            description="A lesson type for beginners in science.",
            duration_minutes=45,
            skill_level="beginner",
            price=30.00
        )
        self.assertEqual(lesson_type.description,
                         "A lesson type for beginners in science.")
        self.assertEqual(lesson_type.duration_minutes, 45)
        self.assertEqual(lesson_type.skill_level, "beginner")
        self.assertEqual(lesson_type.price, 30.00)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.LessonTypeModelTest.test_extended_fields_and_defaults  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.732s

OK

_PASS_

</details>

<details>
<summary><strong> Lesson Type - availabilityh and timestamps  </summary>

Model:

is_available = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

Test: def test_availability_and_timestamps(self):
"""Test that is_available defaults to True and timestamps are set."""
lesson_type = LessonType.objects.create(
tutor=self.tutor_profile,
title="English Tutoring"
)
self.assertTrue(lesson_type.is_available)
self.assertIsNotNone(lesson_type.created_at)
self.assertIsNotNone(lesson_type.updated_at)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.tests.LessonTypeModelTest.test_availability_and_timestamps
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.629s

OK
Destroying test database for alias 'default'...

</details>

<details>
<summary><strong> Tutor Profile Views - List and Detail  </summary>

views:

def tutor_list(request):
tutors = TutorProfile.objects.filter(is_active=True)
return render(request, 'tutors/tutor_list.html', {'tutors': tutors})

def tutor_detail(request, pk):
tutor = get_object_or_404(TutorProfile, pk=pk, is_active=True)
return render(request, 'tutors/tutor_detail.html', {'tutor': tutor})

tests:

class TutorListViewTest(TestCase):
"""Tests for the views in the tutors app."""

    def setUp(self):
        """Set up a user and tutor profile for testing."""
        self.user = User.objects.create_user(
            username="testuser",
        )

        self.active_tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Active Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=True
        )

        self.inactive_tutor = TutorProfile.objects.create(
            user=User.objects.create(username="inactiveuser"),
            display_name="Inactive Tutor",
            bio="Experienced tutor in math and science.",
            experience="5 years of tutoring experience.",
            location="Online",
            is_active=False
        )

    def test_tutor_list_status_code(self):
        """Test that the tutor list view returns a 200 status code."""
        response = self.client.get(reverse('tutors:tutor_list'))
        self.assertEqual(response.status_code, 200)

    def test_only_active_tutors_in_list(self):
        """Test that only active tutors are displayed in the tutor list."""
        response = self.client.get(reverse("tutors:tutor_list"))
        self.assertContains(response, "Active Tutor")
        self.assertNotContains(response, "Inactive Tutor")

    def test_correct_template_used(self):
        response = self.client.get(reverse("tutors:tutor_list"))
        self.assertTemplateUsed(response, "tutors/tutor_list.html")

Results:

1.

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorListViewTest.test_tutor_list_status_code
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.287s

OK

2.

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorListViewTest.test_only_active_tutors_in_list
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.310s

OK
Destroying test database for alias 'default'...

3.

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorListViewTest.test_correct_template_used  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.302s

OK
Destroying test database for alias 'default'...

</details>

<details>

<summary><strong> Tutor CRUD - Create - Test - active/inactive status return (TEST ONLY)  </strong></summary>

Tests:

'def test_tutor_detail_status_code(self):
        """Test that the tutor detail view returns
        a 200 status code for an active tutor."""
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.active_tutor.pk]))
        self.assertEqual(response.status_code, 200)

def test_inactive_tutor_detail_returns_404(self):
        """Test that the tutor detail view returns
        a 404 status code for an inactive tutor."""
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.inactive_tutor.pk]))
        self.assertEqual(response.status_code, 404)

def test_correct_template_used(self):
        response = self.client.get(reverse("tutors:tutor_detail",
                                           args=[self.active_tutor.pk]))
        self.assertTemplateUsed(response, "tutors/tutor_detail.html")'

Results:

Fail:

Corrections made to urls and base.html:

urls.py

- path('<int:pk>/', views.tutor_detail, name='tutor_detail'), updated from int:id
  base.py

- {% url 'tutors:tutor_list' %} now used

re:Test:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorDetailViewTests
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...

---

Ran 3 tests in 0.738s

OK
Destroying test database for alias 'default'...
_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Create - Test - Tutor create (TEST ONLY) </summary>

Test:
def tutor_create(request): # Placeholder for tutor creation logic
return render(request, 'tutors/tutor_form.html', {})

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorCreateViewTests
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.188s

OK
Destroying test database for alias 'default'...

</details>

<details>
<summary><strong> Tutor CRUD - Create - Test - Tutor create view contains form text (TEST ONLY) </summary>

test:

def test_create_view_shows_form_text(self):
        # Test that the tutor create view contains the form text.
        response = self.client.get(reverse("tutors:tutor_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Tutor")

result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorCreateViewTests.test_create_view_shows_form_text
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.173s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

PASS

</details>

<details>
<summary><strong> Tutor CRUD - Create - Test - Checking post creates new tutor (TEST ONLY) </summary>

test:
def test_create_tutor_post_creates_tutor(self): # Test that posting to the tutor create view creates a new tutor profile.
user = User.objects.create_user(username="newuser")

        response = self.client.post(reverse("tutors:tutor_create"), {
            "user": user.id,
            "display_name": "New Tutor",
            "bio": "Test bio",
            "experience": "3 years",
            "location": "London",
            "is_active": True
        })

        self.assertEqual(TutorProfile.objects.count(), 1)

        tutor = TutorProfile.objects.first()
        self.assertEqual(tutor.display_name, "New Tutor")

Result:

2 files changed, 40 insertions(+)
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorCreateViewTests.test_create_tutor_post_creates_tutor
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================

FAIL: test_create_tutor_post_creates_tutor (tutors.test_views.TutorCreateViewTests.test_create_tutor_post_creates_tutor)

---

Traceback (most recent call last):
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\tutors\test_views.py", line 122, in test_create_tutor_post_creates_tutor
self.assertEqual(TutorProfile.objects.count(), 1)
AssertionError: 0 != 1

---

Ran 1 test in 0.232s

FAILED (failures=1)
Destroying test database for alias 'default'..

PASS - Expected as POST Handling not created_

- Implemented Create Logic

View:
def tutor_create(request): # This view is for creating a new tutor profile.
if request.method == 'POST':
user = get_object_or_404(User, id=request.POST["user"])

tutor = TutorProfile.objects.create(
        user=user,
        display_name=request.POST["display_name"],
        bio=request.POST["bio"],
        experience=request.POST["experience"],
        location=request.POST["location"],
        is_active=True,
    )
    return render(request, 'tutors/tutor_detail.html', {'tutor': tutor})

return render(request, 'tutors/tutor_form.html')

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorCreateViewTests.test_create_tutor_post_creates_tutor  
Found 1 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.282s

OK
Destroying test database for alias 'default'...

PASS

</details>

<details>
<summary><strong> Tutor CRUD - Create - Implement Redirect </summary>

Views:

def tutor_create(request): # This view is for creating a new tutor profile.
if request.method == 'POST':
user = get_object_or_404(User, id=request.POST["user"])

tutor = TutorProfile.objects.create(
        user=user,
        display_name=request.POST["display_name"],
        bio=request.POST["bio"],
        experience=request.POST["experience"],
        location=request.POST["location"],
        is_active=True,
    )
    return redirect('tutors:tutor_detail', pk=tutor.pk)

return render(request, 'tutors/tutor_form.html')

Test:

    def test_create_tutor_post_redirects(self):
        # Test that posting to the tutor create
        # view redirects to the tutor detail page.
        user = User.objects.create_user(username="newuser")

        response = self.client.post(reverse("tutors:tutor_create"), {
            "user": user.id,
            "display_name": "Redirect Tutor",
            "bio": "Test bio",
            "experience": "3 years",
            "location": "London",
            "is_active": True
        })

        tutor = TutorProfile.objects.get(display_name="Redirect Tutor")
        self.assertRedirects(
            response,
            reverse("tutors:tutor_detail", args=[tutor.pk])
        )

Results:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorCreateViewTests.test_create_tutor_post_redirects
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.283s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Update - View returns 200 (VIEW AND TEST) </summary>

View:

def tutor_update(request, pk): # This view is for updating an existing tutor profile.
tutor = get_object_or_404(TutorProfile, pk=pk)

    if request.method == 'POST':
        tutor.display_name = request.POST["display_name"]
        tutor.bio = request.POST["bio"]
        tutor.experience = request.POST["experience"]
        tutor.location = request.POST["location"]
        tutor.save()
        return redirect('tutors:tutor_detail', pk=tutor.pk)

    return render(request, 'tutors/tutor_form.html', {'tutor': tutor})

Test:

    def test_update_view_returns_200(self):
        # Test that the tutor update view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:tutor_update", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorUpdateViewTests.test_update_view_returns_200  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.230s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Update - View shows form text (TEST ONLY)</summary>

test:
def test_update_view_shows_form_text(self):
response = self.client.get(
reverse("tutors:tutor_update", args=[self.tutor.pk])
)
self.assertEqual(response.status_code, 200)
self.assertContains(response, "Update Tutor")

results:

Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorUpdateViewTests.test_update_view_shows_form_text
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.249s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Update - View updates tutor profile (TEST ONLY)</summary>

Test:

    def test_update_tutor_post_updates_tutor(self):
        response = self.client.post(
            reverse("tutors:tutor_update", args=[self.tutor.pk]),
            {
                "display_name": "Updated Name",
                "bio": "Updated bio",
                "experience": "5 years",
                "location": "New York",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.tutor.refresh_from_db()

        self.assertEqual(self.tutor.display_name, "Updated Name")
        self.assertEqual(self.tutor.bio, "Updated bio")
        self.assertEqual(self.tutor.experience, "5 years")
        self.assertEqual(self.tutor.location, "New York")

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorUpdateViewTests.test_update_tutor_post_updates_tutor
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.275s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Update - View posting update view redirects to tutor detail (TEST ONLY)</summary>

Test:
def test_update_tutor_post_redirects(self): # Test that posting to the tutor update view redirects to the tutor detail page.
response = self.client.post(
reverse("tutors:tutor_update", args=[self.tutor.pk]),
{
"display_name": "Redirected Name",
"bio": "Redirected bio",
"experience": "4 years",
"location": "Paris",
},
)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorUpdateViewTests.test_update_tutor_post_redirects  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.285s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Delete - delete view returns 200 status</summary>
Test:

class TutorDeleteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="deleteuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Delete Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

    def test_delete_view_returns_200(self):
        # Test that the tutor delete view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorDeleteViewTests.test_delete_view_returns_200
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.260s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Delete - delete tutor removes object</summary>
Test:

    def test_delete_tutor_removes_object(self):
        # Test that posting to the tutor delete view removes the tutor profile.
        response = self.client.post(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertEqual(TutorProfile.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorDeleteViewTests.test_delete_tutor_removes_object
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.290s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor CRUD - Delete - delete tutor redirects</summary>
Test:

    def test_delete_tutor_post_redirects(self):
        # Test that posting to the tutor delete view
        # redirects to the tutor list page.
        response = self.client.post(
            reverse("tutors:tutor_delete", args=[self.tutor.pk])
        )
        self.assertRedirects(response, reverse("tutors:tutor_list"))

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.TutorDeleteViewTests.test_delete_tutor_post_redirects
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.315s

OK
Destroying test database for alias 'default'...

</details>
<details>
<summary><strong> Tutor - Lesson CRUD - Read - Test Lesson List returns 200</strong></summary>
view:

def lesson_list(request, tutor_pk): # This view lists all lesson types for a specific tutor.
tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
lessons = LessonType.objects.filter(tutor=tutor)
return render(
request, 'tutors/lesson_list.html',
{'tutor': tutor, 'lessons': lessons})

Test:

class LessonListViewTests(TestCase): # Tests for the lesson list view.
def setUp(self):
self.user = User.objects.create_user(username="lessonuser")

        self.tutor = TutorProfile.objects.create(
            user=self.user,
            display_name="Lesson Tutor",
            bio="Test bio",
            experience="3 years",
            location="London",
            is_active=True,
        )

        self.lesson = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Lesson",
            subject="math",
            description="Algebra",
            duration_minutes=60,
            skill_level="beginner",
            price=20.00,
        )

    def test_lesson_list_view_returns_200(self):
        # Test that the lesson list view returns a 200 status code.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )
        self.assertEqual(response.status_code, 200)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_lesson_list_view_returns_200
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.291s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

_PASS_

</details>
<details>
<summary><strong> Tutor - Lesson CRUD - Read - Test Lesson List uses correct template</strong></summary>

Test:

    def test_lesson_list_uses_correct_template(self):
        # Test that the lesson list view uses the correct template.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )
        self.assertTemplateUsed(response, "tutors/lesson_list.html")

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_lesson_list_uses_correct_template  
Found 1 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.300s

OK
Destroying test database for alias 'default'...

_PASS_

</details>
<details>
<summary><strong> Tutor - Lesson CRUD - Read - Test Lesson List displays Title</strong></summary>

Test:

    def test_lesson_title_displayed_in_list(self):
        # Test that the lesson title is displayed in the lesson list view.
        response = self.client.get(
            reverse(
                "tutors:lesson_list",
                args=[self.tutor.pk],
            )
        )

        self.assertTemplateUsed(
            response,
            "tutors/lesson_list.html",
        )

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_lesson_title_displayed_in_list  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.292s

OK
Destroying test database for alias 'default'...

</details>

<details>
<summary><strong> Tutor - Lesson CRUD - Update - Test that the lesson update view returns a 200 status code</strong></summary>

view:

def lesson_update(request, tutor_pk, pk): # This view is for updating an existing lesson type for a specific tutor.
tutor = get_object_or_404(TutorProfile, pk=tutor_pk)
lesson = get_object_or_404(LessonType, pk=pk, tutor=tutor)

    if request.method == 'POST':
        lesson.title = request.POST["title"]
        lesson.subject = request.POST["subject"]
        lesson.description = request.POST.get("description", "")
        lesson.duration_minutes = request.POST["duration_minutes"]
        lesson.skill_level = request.POST["skill_level"]
        lesson.price = request.POST["price"]
        lesson.save()
        return redirect('tutors:lesson_list', tutor_pk=tutor.pk)

    return render(
        request, 'tutors/lesson_form.html',
        {'tutor': tutor, 'lesson': lesson})

Test:
def test_lesson_update_view_returns_200(self): # Test that the lesson update view returns a 200 status code.
response = self.client.get(self.url)
self.assertEqual(response.status_code, 200)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonUpdateViewTests.test_lesson_update_view_returns_200
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.314s

OK
Destroying test database for alias 'default'...
_PASS_

</details>

<details>
<summary><strong> Tutor - Lesson CRUD - Update - Test that the lesson update view contains form text</strong></summary>

test:
def test_lesson_update_view_shows_form(self): # Test that the lesson update view contains the form text.
response = self.client.get(self.url)
self.assertContains(response, "Math Lesson")

result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonUpdateViewTests.test_lesson_update_view_shows_form

> > Found 1 test(s).
> > Creating test database for alias 'default'...
> > System check identified no issues (0 silenced).

## 

Ran 1 test in 0.304s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor - Lesson CRUD - Update - Test posting to lesson updates object</strong></summary>

Test:

    def test_lesson_update_updates_object(self):
        # Test that posting to the lesson
        # update view updates the lesson object.
        self.client.post(self.url, {
            "title": "Updated Math Lesson",
            "subject": "math",
            "description": "Updated Algebra",
            "duration_minutes": 90,
            "skill_level": "intermediate",
            "price": 30.00,
        })

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Updated Math Lesson")
        self.assertEqual(self.lesson.description, "Updated Algebra")
        self.assertEqual(self.lesson.duration_minutes, 90)
        self.assertEqual(self.lesson.skill_level, "intermediate")
        self.assertEqual(float(self.lesson.price), 30.00)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonUpdateViewTests.test_lesson_update_updates_object
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.310s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Tutor - Lesson CRUD - Update - Test update redirects</strong></summary>

test:
def test_lesson_update_redirects(self): # Test that posting to the lesson update # view redirects to the lesson list.
response = self.client.post(self.url, {
"title": "Updated Math Lesson",
"subject": "math",
"description": "Updated Algebra",
"duration_minutes": 90,
"skill_level": "intermediate",
"price": 30.00,
})

        self.assertRedirects(
            response,
            reverse("tutors:lesson_list", args=[self.tutor.pk])
        )

result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonUpdateViewTests.test_lesson_update_redirects  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.347s

OK
Destroying test database for alias 'default'...

</details>
<details>
<summary><strong> Tutor - Lesson CRUD - Delete - Test delete view returns 200 status code</strong></summary>

Test:

    def test_lesson_delete_view_returns_200(self):
        # Test that the lesson delete view returns a 200 status code.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonDeleteViewTests.test_lesson_delete_view_returns_200
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.321s

OK
Destroying test database for alias 'default'...
_PASS_

</details>
<details>
<summary><strong> Tutor - Search & Filter - test filter by title</strong></summary>

Template:

{% extends "base.html" %}

{% block title %}Lesson List{% endblock %}

{% block content %}

<h1>{{ tutor.display_name }}'s Lessons</h1>

<form method="get">
    <input type="text" name="q" placeholder="Search lessons..." value="{{ request.GET.q }}">
    <select name="subject">
        <option value="">All Subjects</option>
        <option value="math">Math</option>
        <option value="science">Science</option>
        <option value="english">English</option>
    </select>

    <select name="skill_level">
        <option value="">All Skill Levels</option>
        <option value="beginner">Beginner</option>
        <option value="intermediate">Intermediate</option>
        <option value="advanced">Advanced</option>
    </select>
    <button type="submit">Filter</button>

</form>

{% for lesson in lessons %}

<div>
<h3>{{ lesson.title }}</h3>
<p>{{ lesson.subject }} | {{ lesson.skill_level }}</p>
<p>{{ lesson.description }}</p>
<p>£{{ lesson.price }}</p>
</div>
{% empty %}
<p>No lessons found.</p>
{% endfor %}
{% endblock %}

Test:

    def test_search_filters_lessons_by_title(self):
        # Test that the search functionality filters lessons by title.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk]) + "?q=Math"
        )
        self.assertContains(response, "Math Lesson")

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_search_filters_lessons_by_title
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.329s

OK
Destroying test database for alias 'default'...

_PASS_

</details>
<details>
<summary><strong> Tutor - Search & Filter - Test subject and skill filters </strong></summary>

Test:

    def test_subject_filter_works(self):
        # Test that filtering lessons by subject works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?subject=math"
        )
        self.assertContains(response, "Math Lesson")

    def test_skill_filter_works(self):
        # Test that filtering lessons by skill level works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?skill=beginner"
        )
        self.assertContains(response, "Math Lesson")

Results:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_subject_filter_works  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.299s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_skill_filter_works  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.286s

OK
Destroying test database for alias 'default'...

_PASS_

</details>
<details>
<summary><strong> Tutor - Search & Filter - Test Django configuration re-test filters- </strong></summary>

Updated template:

{% extends "base.html" %}

{% block title %}Lesson List{% endblock %}

{% block content %}

<h1>{{ tutor.display_name }}'s Lessons</h1>

<form method="get">
    {{ filter.form.as_p }}
    <button type="submit">Filter</button>
</form>

{% for lesson in lessons %}

<div>
<h3>{{ lesson.title }}</h3>
<p>{{ lesson.subject }} | {{ lesson.skill_level }}</p>
<p>{{ lesson.description }}</p>
<p>£{{ lesson.price }}</p>
</div>
{% empty %}
<p>No lessons found.</p>
{% endfor %}
{% endblock %}

Updated view:
def lesson_list(request, tutor_pk): # This view lists all lesson types for a specific tutor.
tutor = get_object_or_404(TutorProfile, pk=tutor_pk)

    queryset = LessonType.objects.filter(tutor=tutor)

    lesson_filter = LessonFilter(request.GET, queryset=queryset)

    return render(
        request, 'tutors/lesson_list.html',
        {
            'tutor': tutor,
            'lessons': lesson_filter.qs,
            'filter': lesson_filter,
        }
    )

Tests:

    def test_search_filters_lessons_by_title(self):
        # Test that the search functionality filters lessons by title.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk]) + "?q=Math"
        )
        self.assertContains(response, "Math Lesson")

    def test_subject_filter_works(self):
        # Test that filtering lessons by subject works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?subject=math"
        )
        self.assertContains(response, "Math Lesson")

    def test_skill_filter_works(self):
        # Test that filtering lessons by skill level works.
        response = self.client.get(
            reverse("tutors:lesson_list", args=[self.tutor.pk])
            + "?skill_level=beginner"
        )
        self.assertContains(response, "Math Lesson")

Results:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_skill_filter_works
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.297s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_search_filters_lessons_by_title  
Found 1 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.323s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_subject_filter_works  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.298s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test tutors.test_views.LessonListViewTests.test_skill_filter_works  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.562s

OK
Destroying test database for alias 'default'...

_PASS_

</details>
<details>
<summary><strong> Bookings - Data Model - Test booking can be created with correct default status-</strong></summary>

ModeL:

class Booking(models.Model):
"""
Represents a booking made by a student for a lesson type.
"""
STATUS_CHOICES = [
("pending", "Pending"),
("confirmed", "Confirmed"),
("cancelled", "Cancelled"),
]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    lesson_type = models.ForeignKey(
        LessonType,
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.student} - "
            f"{self.lesson_type} on "
            f"{self.booking_date} at "
            f"{self.booking_time}"
        )

Test:

class BookingModelTest(TestCase):
def setUp(self):
self.user = User.objects.create_user(
username="testuserstudent")
self.tutor = TutorProfile.objects.create(
user=self.user,
display_name="Test Tutor",
bio="Experienced tutor in math and science.",
experience="5 years of tutoring experience.",
location="Online",
is_active=True,
)

        self.lesson_type = LessonType.objects.create(
            tutor=self.tutor,
            title="Math Tutoring",
            subject="math",
            skill_level="beginner",
            duration_minutes=60,
            price=50.00,
        )

    def test_booking_creation(self):
        """
        Test that a Booking can be created and has the correct default status.
        """
        booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

        self.assertEqual(booking.status, "pending")

        self.assertEqual(
            str(booking),
            f"{self.user} - {self.lesson_type} on 2024-06-15 at 14:00:00"
        )

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingModelTest.test_booking_creation
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.256s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

_PASS_

</details>
<details>
<summary><strong> Bookings - Data Form - Test booking form is valid with correct data-</strong></summary>

Form:
class BookingForm(forms.ModelForm):
"""
Form for creating and updating Booking instances.

    Uses Django's ModelForm to automatically generate form fields
    based on the Booking model and apply model validation.
    """
    class Meta:
        """
        Meta configuration for the BookingForm.
        """
        model = Booking
        fields = [
            "booking_date",
            "booking_time",
            "notes",
        ]

Test:

class BookingFormTest(TestCase):

    def test_valid_booking_form(self):
        """
        Test that a Booking form is valid with correct data.
        """
        def test_valid_booking_form(self):
            form = BookingForm(data={
                "booking_date": "2024-06-15",
                "booking_time": "14:00:00",
                "notes": "Hello, I would like to book a lesson."
            })

            self.assertTrue(form.is_valid())

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingFormTest.test_valid_booking_form  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.153s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

_PASS_

</details>
<details>
<summary><strong> Bookings - Data Form - Test login required for booking</strong></summary>

test:

class BookingViewTests(TestCase):

    def test_login_required_for_booking(self):
        response = self.client.get(
            reverse("bookings:create_booking", args=[1]))
        self.assertNotEqual(response.status_code, 200)

    def test_booking_page_loads_for_logged_in_user(self):
        self.client.login(username="student", password="pass")
        response = self.client.get(
            reverse("bookings:create_booking", args=[1]))
        self.assertEqual(response.status_code, 200)

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingViewTest.test_login_required_for_booking  
Found 1 test(s).  
Traceback (most recent call last):
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\manage.py", line 22, in <module>
main()
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\manage.py", line 18, in main
execute_from_command_line(sys.argv)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\_\_init**.py", line 443, in execute_from_command_line
utility.execute()
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\_\_init**.py", line 437, in execute
self.fetch_command(subcommand).run_from_argv(self.argv)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\commands\test.py", line 24, in run_from_argv
super().run_from_argv(argv)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\base.py", line 420, in run_from_argv
self.execute(*args, \*\*cmd_options)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\base.py", line 464, in execute
output = self.handle(*args, **options)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\commands\test.py", line 63, in handle
failures = test_runner.run_tests(test_labels)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\test\runner.py", line 1133, in run_tests
self.run_checks(databases)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\test\runner.py", line 1055, in run_checks
call_command("check", verbosity=self.verbosity, databases=databases)
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\_\_init\_\_.py", line 195, in call_command
return command.execute(\*args, **defaults)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\base.py", line 464, in execute
output = self.handle(\*args, \*\*options)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\commands\check.py", line 81, in handle
self.check(
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\management\base.py", line 496, in check
all_issues = checks.run_checks(
^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\checks\registry.py", line 89, in run_checks
new_errors = check(app_configs=app_configs, databases=databases)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\core\checks\urls.py", line 136, in check_custom_error_handlers
handler = resolver.resolve_error_handler(status_code)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\urls\resolvers.py", line 743, in resolve_error_handler
callback = getattr(self.urlconf_module, "handler%s" % view_type, None)
^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\utils\functional.py", line 47, in **get**
res = instance.**dict**[self.name] = self.func(instance)
^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\urls\resolvers.py", line 722, in urlconf_module
return import_module(self.urlconf_name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\Owner\AppData\Local\Programs\Python\Python312\Lib\importlib\_\_init**.py", line 90, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1331, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 999, in exec_module
File "<frozen importlib._bootstrap>", line 488, in \_call_with_frames_removed
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\tutor_connect_project\urls.py", line 29, in <module>
path("bookings/", include("bookings.urls")),
^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\.venv\Lib\site-packages\django\urls\conf.py", line 39, in include
urlconf_module = import_module(urlconf_module)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\Owner\AppData\Local\Programs\Python\Python312\Lib\importlib\_\_init**.py", line 90, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1331, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 999, in exec_module
File "<frozen importlib._bootstrap>", line 488, in \_call_with_frames_removed
File "C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect\bookings\urls.py", line 12, in <module>
path("", views.booking_list, name="booking_list"),
^^^^^^^^^^^^^^^^^^
AttributeError: module 'bookings.views' has no attribute 'booking_list'
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

FAIL - EXPECTED - As booking list view not created yet. To retest after all views created.

RETESTS RESULTS following booking list view creation.

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingViewTests.test_booking_page_loads_for_logged_in_user
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.624s

OK

OK
Destroying test database for alias 'default'

</details>
<details>
<summary><strong> Bookings - Booking view tests -  page loads for logged in user</strong></summary>

''' Python test:
    def test_booking_page_loads_for_logged_in_user(self):
        self.client.login(username="student", password="pass")
        response = self.client.get(
            reverse("bookings:booking_create", args=[1]))
        self.assertRedirects(
            response,
            "/accounts/login/?next=/bookings/create/1/"
        )

Result:
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingViewTests.test_booking_page_loads_for_logged_in_user
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.624s

OK
Destroying test database for alias 'default'...

_PASS_

</details>

<details>
<summary><strong> Bookings - Booking view tests -  user can delete/cancel booking</strong></summary>

''' Python test:def test_user_can_delete_booking(self):
self.client.login(username="student", password="pass")

        booking = Booking.objects.create(
            student=self.user,
            lesson_type=self.lesson_type,
            booking_date="2024-06-15",
            booking_time="14:00:00",
        )

        self.client.post(
            reverse("bookings:booking_delete", args=[booking.id])
        )

        booking.refresh_from_db()
        self.assertEqual(booking.status, "cancelled")

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingViewTests.test_user_can_delete_booking  
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 1.512s

OK
Destroying test database for alias 'default'...

</details>
<details>
<summary><strong> Bookings - Booking update tests -  page loads correctly</strong></summary>

''' Python test
    def test_booking_update_page_loads(self):
        # Test that the booking update page loads correctly for a logged-in user.
        self.client.login(username="testuserstudent", password="pass")

        response = self.client.get(
            reverse("bookings:booking_update", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Booking")
        self.assertEqual(response.status_code, 200)
'''

''' Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingUpdateViewTests.test_booking_update_page_loads
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 1.579s

OK
Destroying test database for alias 'default'...

---
'''

Ran 1 test in 1.589s

</details>
<details>
<summary><strong> Bookings - Booking Detail tests -  Requires login, user specific detail</strong></summary>
View:

@login_required
def booking_detail(request, pk):
"""Display the details of a specific booking for the logged-in user.
Args:
pk (int): Primary key of the booking to view
"""
booking = get_object_or_404(Booking, pk=pk, student=request.user)
return render(request, "bookings/booking_detail.html", {
"booking": booking
})

Test:

    def test_booking_detail_page_loads(self):
        """Test that the booking detail page loads
        correctly for the logged-in user.
        """
        self.client.login(username="testuserstudent", password="pass")

        response = self.client.get(
            reverse("bookings:booking_detail", args=[self.booking.pk])
        )

        self.assertEqual(response.status_code, 200)

    def test_booking_detail_requires_login(self):
        response = self.client.get(
            reverse(
                "bookings:booking_detail",
                args=[self.booking.pk]
            )
        )

        self.assertEqual(response.status_code, 302)

    def test_user_cannot_view_another_users_booking(self):
        """Test that a user cannot view another user's booking detail page.
        """
        User.objects.create_user(
            username="otheruser",
            password="pass",
        )
        self.client.login(
            username="otheruser",
            password="pass",
        )

        response = self.client.get(
            reverse(
                "bookings:booking_detail",
                args=[self.booking.pk]
            )
        )

        self.assertEqual(response.status_code, 404)

Results:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingDetailViewTests.test_booking_detail_page_loads  
Found 1 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 1.610s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingDetailViewTests.test_booking_detail_requires_login
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 0.697s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingDetailViewTests.test_user_cannot_view_another_users_booking
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 2.215s

OK
Destroying test database for alias 'default'...

_PASS_

</details>
<details>
<summary><strong> Bookings - Booking Update Test- Test booking can be updated</strong></summary>

    def test_booking_can_be_updated(self):
        """Test that a booking can be updated successfully."""
        self.client.login(
            username="testuserstudent",
            password="pass",
        )

        self.client.post(
            reverse(
                "bookings:booking_update",
                args=[self.booking.pk]
            ),
            {
                "booking_date": "2026-08-01",
                "booking_time": "15:00",
                "notes": "Updated notes",
            }
        )

        self.booking.refresh_from_db()

        self.assertEqual(
            str(self.booking.booking_date),
            "2026-08-01"
        )

        self.assertEqual(
            str(self.booking.booking_time),
            "15:00:00"
        )

        self.assertEqual(
            self.booking.notes,
            "Updated notes"
        )

Result:

(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test bookings.tests.BookingUpdateViewTests.test_booking_can_be_updated  
Found 1 test(s).  
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.

---

Ran 1 test in 1.575s

OK
Destroying test database for alias 'default'...
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect>

Outcome: PASS

</details>

<details>

<summary><strong> Checkout - Checkout Review Requires Login</strong></summary>

Test:

    def test_checkout_review_requires_login(self):
        """Test that the checkout review view requires login."""
        response = self.client.get(
            reverse("checkout_review", args=[self.booking.pk])
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login


Results: 
(.venv) PS C:\Users\User\Documents\vscode-projects\msp-4-tutor-connect> python manage.py test checkout.tests.CheckoutReviewTests.test_checkout_review_requires_login    
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 1.145s

OK
Destroying test database for alias 'default'...

Outcome: PASS


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

## Admin

The Django admin interface was configured to make site management easier for superusers and staff users. Custom admin classes were added for the main project models so that records can be searched, filtered and reviewed efficiently.

### Tutor Profile Admin

The TutorProfile admin view allows staff users to manage tutor profiles from the Django admin panel.

Configured features include:

- Displaying key tutor information such as display name, linked user account, location, contact email, active status and creation date.
- Filtering tutor profiles by active status, location and creation date.
- Searching tutor profiles by display name, username, email address, biography, experience, location, contact email and lesson delivery information.
-  Ordering profiles alphabetically by display name.
- Making automatically generated timestamp fields read-only.

This makes it easier for administrators to review tutor profiles, check whether tutors are active and locate specific tutors quickly.

### Lesson Type Admin

The LessonType admin view allows staff users to manage scheduled lesson slots.

Configured features include:

- Displaying lesson title, tutor, category, subject, skill level, lesson date, lesson time, duration, price and availability.
- Filtering lessons by category, subject, skill level, availability, lesson date and creation date.
- Searching lessons by title, description and tutor display name.
- Ordering lessons by lesson date and lesson time.
- Using list\_select\_related to optimise related tutor lookups.
- Making automatically generated timestamp fields read-only.

This provides administrators with a clear overview of scheduled lessons and helps manage lesson availability across the platform.

### Booking Admin

The Booking admin view allows staff users to review student bookings.

Configured features include:

- Displaying student, lesson, booking date, booking time, status and creation date.
- Filtering bookings by status, booking date and creation date.
- Searching by student username, student email, lesson title, tutor display name and booking notes.
- Ordering bookings by booking date and booking time.
- Using list\_select\_related to optimise related student, lesson and tutor lookups.
- Making automatically generated timestamp fields read-only.

This helps administrators review booking activity and investigate booking issues if required.

### Payment Admin

The Payment admin view allows staff users to review payment records associated with bookings.

Configured features include:

- Displaying the related booking, payment amount and creation date.
- Searching by student username, student email and lesson title.
- Ordering payment records by newest first.
- Using list\_select\_related to optimise related booking, student and lesson lookups.
- Making automatically generated timestamp fields read-only.

Sensitive Stripe credentials are not displayed in the admin interface.

---

## Security

Security was considered throughout the project to protect user data, restrict access to sensitive functionality and ensure production credentials are not exposed in the codebase.

### Authentication

Tutor Connect uses Django's build-in authentication system to manage user registration, login, logout and session handling.

Protected views use Django's '@login_required' decorator to prevent unauthenticated users from accessing restricted pages.
This is used for functionality such as:

- Dashboard access
- Tutor profile creation
- Tutor profile editing
- Tutor profile deletion
- Lesson creation
- Lesson editing
- Lesson deletion
- Booking creation
- Booking management
- Checkout access

Unauthenticated users attempting to access protected pages are redirected to the login page.

### Authorisation

Authorisation rules were added to ensure users can only manage their own content.

Tutor profile management is restricted by filtering profile objects against the logged-in user. This prevents users from editing or deleting tutor profiles that do not belong to them.

Lesson management is also restricted to the owner of the tutor profile. Tutors can only create, edit or delete lessons attached to their own tutor profile.

Booking management is restricted to the student who created the booking. Users cannot view, edit or cancel bookings belonging to another account.

Checkout views are also protected so users can only review and pay for their own bookings.

Where appropriate, object lookups include the logged-in user as part of the query. This prevents ID guessing from exposing or modifying another user's records.

### Business Rule Protection

Additional business logic was implemented to protect booking integrity.

Lessons with pending or confirmed bookings cannot be edited or deleted by the tutor. This prevents a tutor from changing or removing a lesson after a student has booked it.

Booked lessons are hidden from the public lesson marketplace to prevent double-booking.

Past lessons are also hidden from public lesson listings.

### CSRF Protection

Django's CSRF middleware is enabled in the project settings.

All forms that submit data using POST include the `{% csrf_token %}` template tag. This includes:

- Registration forms
- Login/logout forms
- Tutor profile forms
- Lesson creation and update forms
- Delete confirmation forms
- Booking forms
- Checkout session form

Delete actions are handled through POST requests rather than simple GET links, reducing the risk of accidental or malicious destructive actions.

### Secret Keys and Credentials

Sensitive values are not hard-coded in the project.

The project uses environment variables for secret configuration, including:

- `SECRET_KEY`
- `DATABASE_URL`
- `STRIPE_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `DEBUG`

The local `.env` file is excluded from version control using `.gitignore`.

On Heroku, production values are stored using Config Vars. This keeps production credentials separate from the source code.

### Production Security Settings

Production security settings were added to strengthen deployment security.

These include:

- `DEBUG=False` in production.
- `CSRF_TRUSTED_ORIGINS` configured for the Heroku deployment domain.
- Secure session cookies enabled when not in debug mode.
- Secure CSRF cookies enabled when not in debug mode.
- HTTPS redirect enabled in production.
- HTTP Strict Transport Security configured for production.
- Allowed hosts restricted to local development domains and Heroku deployment domains.

These settings help protect sessions, CSRF tokens and production traffic.

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
