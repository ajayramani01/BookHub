# **Community-Driven Book Recommendation Platform**

## **Overview**
This project is a web application built using Django that allows users to search for books using the Google Books API and submit their own book recommendations. Users can also view recommendations from other users. The application provides user authentication, allowing users to register, log in, and manage their recommendations.

## **Features**
- **User Authentication:** Register, login, and logout functionalities.
- **Book Search:** Search for books using the Google Books API.
- **Submit Recommendations:** Authenticated users can submit book recommendations, including details like title, author, genre, description, rating, and publication date.
- **View Recommendations:** Users can view all submitted book recommendations.

## **Installation & Setup**
### **Prerequisites**
- Python 3.x
- Django 4.x

### **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/community-book-recommendation.git
   cd community-book-recommendation

2. **Run migrations:**
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Start the server:**
    ```
    python manage.py runserver
    ```

4. **User can Search Books without creating account** 
5. **After Creating Account , User can also add/view recommendation**
