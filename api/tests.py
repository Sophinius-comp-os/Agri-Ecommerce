from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User, Product, Category, Order, OrderItem, Address, Payment

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testuser',
            name='Test User',
            email='test@example.com',
            password='test123',
            phone_number='1234567890',
            role='user'
        )

    def test_str_representation(self):
        user = User.objects.get(id=1)
        expected_str = 'Test User'
        self.assertEqual(str(user), expected_str)

    def test_fields(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'test123')
        self.assertEqual(user.phone_number, '1234567890')
        self.assertEqual(user.role, 'user')


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=9.99,
            quantity_available=10,
            image_url='http://example.com/image.jpg'
        )

    def test_str_representation(self):
        product = Product.objects.get(id=1)
        expected_str = 'Test Product'
        self.assertEqual(str(product), expected_str)

    def test_fields(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.quantity_available, 10)
        self.assertEqual(product.image_url, 'http://example.com/image.jpg')



from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Category object for testing
        Category.objects.create(name='Test Category')

    def test_name_field(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_str_representation(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'Test Category')


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User object for testing
        user = User.objects.create(username='testuser', name='Test User')
        # Create an Order object for testing
        Order.objects.create(user=user, total_amount=100.00)

    def test_user_field(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_total_amount_field(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('total_amount').verbose_name
        self.assertEqual(field_label, 'total amount')

    def test_order_date_auto_now_add(self):
        order = Order.objects.get(id=1)
        self.assertIsNotNone(order.order_date)

    def test_payment_status_default(self):
        order = Order.objects.get(id=1)
        payment_status = order.payment_status
        self.assertFalse(payment_status)

    def test_str_representation(self):
        order = Order.objects.get(id=1)
        self.assertEqual(str(order), 'Order ID: 1')

class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Product object for testing
        product = Product.objects.create(name='Test Product', price=10.00)
        # Create an Order object for testing
        order = Order.objects.create(user_id=1, total_amount=100.00)
        # Create an OrderItem object for testing
        OrderItem.objects.create(order=order, product=product, quantity=2, price=20.00)

    def test_order_field(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('order').verbose_name
        self.assertEqual(field_label, 'order')

    def test_product_field(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('product').verbose_name
        self.assertEqual(field_label, 'product')

    def test_quantity_field(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_price_field(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_str_representation(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertEqual(str(order_item), 'OrderItem ID: 1')

class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an Address object for testing
        Address.objects.create(street='Test Street', city='Test City', state='Test State', zip_code='12345')

    def test_street_field(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('street').verbose_name
        self.assertEqual(field_label, 'street')

    def test_city_field(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_state_field(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_zip_code_field(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('zip_code').verbose_name
        self.assertEqual(field_label, 'zip code')

    def test_string_representation(self):
        address = Address.objects.get(id=1)
        expected_str = 'Test Street, Test City, Test State'
        self.assertEqual(str(address), expected_str)


class PaymentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an Order object for testing
        order = Order.objects.create(user_id=1, total_amount=100.00, payment_status=False)
        # Create a Payment object for testing
        Payment.objects.create(order=order, payment_method='Credit Card', amount=50.00, transaction_status=False)

    def test_order_field(self):
        payment = Payment.objects.get(id=1)
        self.assertEqual(payment.order.user_id, 1)
        self.assertEqual(payment.order.total_amount, 100.00)
        self.assertEqual(payment.order.payment_status, False)

    def test_payment_method_field(self):
        payment = Payment.objects.get(id=1)
        field_label = payment._meta.get_field('payment_method').verbose_name
        self.assertEqual(field_label, 'payment method')

    def test_amount_field(self):
        payment = Payment.objects.get(id=1)
        field_label = payment._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_transaction_status_field(self):
        payment = Payment.objects.get(id=1)
        field_label = payment._meta.get_field('transaction_status').verbose_name
        self.assertEqual(field_label, 'transaction status')

    def test_string_representation(self):
        payment = Payment.objects.get(id=1)
        expected_str = 'Payment ID: 1'
        self.assertEqual(str(payment), expected_str)