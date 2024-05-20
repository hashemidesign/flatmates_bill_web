# Flatmates Bill

Flatmates Bill is a web application designed to help flatmates split their bills fairly. It allows users to input the bill amount and the number of days each flatmate has stayed in the house, and calculates how much each person should pay.

## Features

- **Bill Calculation**: Input the total bill amount and the period, along with the names and days stayed for two flatmates, to calculate how much each flatmate owes.
- **Responsive Design**: The application uses Bulma CSS framework for a modern and responsive design.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-WTF

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flatmates-bill.git
    ```
2. Navigate to the project directory:
    ```sh
    cd flatmates-bill
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

```plaintext
flatmates-bill/
│
├── forms/
│ └── bill_form.py
├── models/
│ ├── bill.py
│ └── flatmate.py
├── static/
├── templates/
│ ├── index.html
│ └── bill-form.html
├── views/
│ ├── bill_view.py
│ └── home_view.py
├── .gitignore
├── README.md
├── requirements.txt
└── app.py
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue or contact [m.hashemi.code@gmail.com](mailto:m.hashemi.code@gmail.com).
