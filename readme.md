# 🍽️ FoodTracker API

A backend REST API for tracking food items across multiple kitchens with user-based access control.  
This project focuses on **backend architecture, authentication, validation, and API design**.

The API is designed to be consumed by **web or mobile frontends** (e.g., React / React Native).

---

## 🚀 Tech Stack
- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Database ORM:** SQLAlchemy  
- **Authentication:** JWT (OAuth2 Password Flow)  
- **Validation:** Pydantic  
- **Password Security:** bcrypt (passlib)  
- **Database:** PostgreSQL / MySQL (configurable)  
- **File Handling:** Image uploads with server-side storage  

---

## 🔐 Authentication & Authorization
- User signup with secure password hashing  
- User login with JWT access token generation  
- Token-based authentication for protected routes  
- Ownership-based authorization (users access only their own data)  

---

## 🏠 Kitchen Management
- Create kitchens linked to authenticated users  
- Fetch all kitchens owned by the logged-in user  
- Ensures data isolation between users (multi-tenant logic)  

---

## 🍎 Food Item Management
- Add food items with:
  - Name  
  - Expiry date  
  - Quantity & unit  
  - Associated kitchen  
  - Image upload  
- Server-side validation:
  - Expiry date cannot be in the past  
  - Quantity must be positive  
  - Unit restricted to predefined values  
- Image files stored securely on the server with unique filenames  

---

## 🔍 Search, Sort & Pagination
- Offset-based pagination  
- Search functionality on food items  
- Sorting support based on provided fields  
- Combination of search + sort + pagination  
- Default ordering by expiry date  

> Note: Some search and sorting logic is intentionally implemented at the application level to explore algorithmic approaches before database optimization.

---

## 📦 API Structure
- Clean separation of concerns:
  - `routers` – API endpoints  
  - `models` – Database models  
  - `schemas` – Request/response validation  
  - `utils` – Authentication & helper logic  
  - `config` – Database and environment configuration  

---

## 🌐 CORS Support
- Configured to allow requests from local development frontends (e.g., Expo / React Native)

---

## 🧠 Learning Goals
- Understanding JWT authentication and protected routes  
- Designing RESTful APIs  
- Implementing data validation and security best practices  
- Managing relational data with SQLAlchemy  
- Handling file uploads and server storage  
- Exploring search and sorting strategies  

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
