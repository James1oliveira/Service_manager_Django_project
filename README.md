---

# 💼 Business Use Case

The Service Manager application is designed to help businesses organize and manage customer service requests efficiently. Instead of relying on paper records or spreadsheets, the system provides a centralized platform where staff can record customer information, track services, and manage ongoing work.

### Suitable for

- Computer repair businesses
- Automotive workshops
- Cleaning companies
- Appliance repair services
- General maintenance businesses
- Small and medium-sized service providers

### Business Benefits

- Centralized customer and service records
- Faster access to customer information
- Reduced paperwork
- Improved organization and record keeping
- Better tracking of completed and pending services
- Secure user authentication for authorized access

---

# ⚙️ Technical Specification

| Category | Details |
|----------|---------|
| Framework | Django |
| Language | Python 3 |
| Frontend | HTML5, CSS3, Bootstrap |
| Database | SQLite3 |
| Authentication | Django Authentication System |
| Architecture | MVC (Model-View-Template) |
| Version Control | Git & GitHub |

### Core Components

- Customer Management
- Service Management
- User Authentication
- Django Admin Panel
- Database Models
- CRUD Functionality
- Form Validation
- URL Routing
- Static File Management

### Functional Features

- User login/logout
- Add new customers
- Edit customer information
- Delete customer records
- Create service records
- Update service information
- View service history
- Admin management interface

---

# 📖 User Guide

## Logging In

1. Start the Django server:

```bash
python manage.py runserver
```

2. Open your browser and visit:

```
http://127.0.0.1:8000/
```

3. Log in using your registered account.

---

## Managing Customers

- Navigate to the **Customers** section.
- Click **Add Customer**.
- Complete the required information.
- Save the record.
- Edit or delete customers when necessary.

---

## Managing Services

- Open the **Services** page.
- Create a new service record.
- Assign it to the appropriate customer.
- Update the service status as work progresses.
- Save any changes.

---

## Administrator Functions

Users with administrator privileges can:

- Access the Django Admin dashboard
- Manage users
- Manage customers
- Manage services
- View and edit database records
- Control application data

Admin URL:

```
http://127.0.0.1:8000/admin/
```

---

## Logging Out

Select the **Logout** option from the navigation menu to securely end your session.

---

## Common Workflow

1. Log into the system.
2. Add a customer (if they do not already exist).
3. Create a service record.
4. Update the service as work progresses.
5. Mark the service as completed.
6. Log out securely.
