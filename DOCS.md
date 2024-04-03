# Ecomm_API API Documentation

The Ecomm_API project provides an e-commerce API with various endpoints for managing users, products, categories, orders, order items, addresses, and payments. This documentation outlines the available endpoints and their usage.

## Base URL

All API endpoints are relative to the base URL of your server. By default, during development, the base URL is `http://localhost:8000/api/`.

## Authentication

The Ecomm_API does not require authentication for accessing most endpoints. However, certain endpoints, such as user-specific details, may require authentication. In such cases, you need to include an authentication token in the request headers. To obtain an authentication token, you can use Django REST framework's built-in authentication mechanisms.

## Error Handling

The API follows standard HTTP status codes for indicating the success or failure of a request. In case of an error, the response body will contain an `error` field with the error message.

Example Error Response:

```json
{
    "error": "Product not found."
}
```

## Endpoints

### Users

#### Get a List of Users

- **URL**: `/api/users/`
- **Method**: GET
- **Description**: Fetches a list of all users.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of user objects.

#### Get a User's Details

- **URL**: `/api/users/<int:user_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific user.
- **Response**:
  - Status Code: 200 (OK)
  - Body: User object.

### Products

#### Get a List of Products

- **URL**: `/api/products/`
- **Method**: GET
- **Description**: Fetches a list of all products.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of product objects.

#### Get a Product's Details

- **URL**: `/api/products/<int:product_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific product.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Product object.

### Categories

#### Get a List of Categories

- **URL**: `/api/categories/`
- **Method**: GET
- **Description**: Fetches a list of all categories.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of category objects.

#### Get a Category's Details

- **URL**: `/api/categories/<int:category_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific category.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Category object.

### Orders

#### Get a List of Orders

- **URL**: `/api/orders/`
- **Method**: GET
- **Description**: Fetches a list of all orders.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of order objects.

#### Get an Order's Details

- **URL**: `/api/orders/<int:order_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific order.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Order object.

### Order Items

#### Get a List of Order Items

- **URL**: `/api/orderitems/`
- **Method**: GET
- **Description**: Fetches a list of all order items.
- **Response**:
  - Status Code: 200

 (OK)
  - Body: List of order item objects.

#### Get an Order Item's Details

- **URL**: `/api/orderitems/<int:order_item_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific order item.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Order item object.

### Addresses

#### Get a List of Addresses

- **URL**: `/api/addresses/`
- **Method**: GET
- **Description**: Fetches a list of all addresses.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of address objects.

#### Get an Address's Details

- **URL**: `/api/addresses/<int:address_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific address.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Address object.

### Payments

#### Get a List of Payments

- **URL**: `/api/payments/`
- **Method**: GET
- **Description**: Fetches a list of all payments.
- **Response**:
  - Status Code: 200 (OK)
  - Body: List of payment objects.

#### Get a Payment's Details

- **URL**: `/api/payments/<int:payment_id>/`
- **Method**: GET
- **Description**: Retrieves details for a specific payment.
- **Response**:
  - Status Code: 200 (OK)
  - Body: Payment object.

## Note

The API documentation for the Ecomm_API project. You can use the provided endpoints to interact with the e-commerce system and perform various operations on users, products, categories, orders, order items, addresses, and payments.

For any further information or assistance, please refer to the project's source code or contact the project maintainers.

**Note**: The API documentation is subject to change and may require updates as new features are added or existing ones are modified.
