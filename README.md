# CRUD App with Flask, SQLAlchemy, HTML, and Jinja

This is a simple CRUD (Create, Read, Update, Delete) web application built using Python, Flask, SQLAlchemy, HTML, and Jinja. It allows users to interact with a database, perform CRUD operations, and view the changes in the web interface.

## Features

- **Create**: Allows users to add new records to the database.
- **Read**: Displays the records from the database in a user-friendly interface.
- **Update**: Enables users to edit existing records.
- **Delete**: Provides functionality to remove records from the database.

## Technologies Used

- **Python**: The programming language used for the backend logic.
- **Flask**: A lightweight Python web framework used to build the application.
- **SQLAlchemy**: An ORM (Object Relational Mapper) used to interact with the database.
- **HTML**: Markup language for the web pages.
- **Jinja**: Templating engine used to render dynamic content in HTML pages.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```

2. Navigate into the project folder:

   ```bash
   cd your-repository
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If the `requirements.txt` file is not present, you can manually install the dependencies:

   ```bash
   pip install Flask SQLAlchemy
   ```

4. Set up the database by running the following command:

   ```bash
   python app.py
   ```

### Running the Application

1. To run the app, use:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

   You should now see the app running locally.

## Project Structure

```
/your-repository
│
├── app.py                  # Main Flask application
├── Templates/              # Folder containing HTML templates
│   ├── index.html          # Home page
│   ├── update_user.html    # Update user page
│
├── models.py               # SQLAlchemy models
├── requirements.txt        # List of dependencies
└── instance/               # Instance folder for configuration files (optional)
```

## Contributing

Feel free to fork the repository and submit pull requests for any changes or improvements. 

### Steps for Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
