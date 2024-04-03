# Agri-Ecommerce

Go-to market Solution 

# Ecomm_API

Ecomm_API is a Django-based e-commerce API project that provides endpoints for managing users, products, categories, orders, order items, addresses, and payments. It is designed to serve as the backend for an e-commerce website or mobile application.

## Features

- User Management: Create, retrieve, update, and delete users.
- Product Management: Manage product details, including CRUD operations.
- Category Management: Categorize products and perform CRUD operations on categories.
- Order Management: Create, retrieve, update, and delete orders, along with their associated items.
- Address Management: Manage user addresses for shipping and billing.
- Payment Management: Handle payment details and transactions.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/ecomm-api.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ecomm-api
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

4. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the API at `http://localhost:8000/api/`.

## API Documentation

The API endpoints and their usage are documented in the [API documentation](API_DOCUMENTATION.md) file. Refer to this documentation for detailed information on how to interact with the API.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```shell
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes and push the branch:

   ```shell
   git commit -m "Add your commit message"
   git push origin feature/your-feature-name
   ```

4. Create a pull request explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).
## Author
1. -[Dovine K.](https://Sophinius-comp-os.github.io)
2. -[Dericocity](https://github.com/dericocity)
