import pytest
from django.contrib.auth import get_user_model
from invoices.models import Invoices, Products, Contractors
from datetime import date


@pytest.fixture
def user(db):
    return get_user_model().objects.create(username='test_user')


@pytest.fixture
def product(db, user):
    return Products.objects.create(name='Test Product',
                                   vat_rate=23,
                                   price=100,
                                   owner=user
                                   )


@pytest.fixture
def contractor(db):
    return Contractors.objects.create(name='Test Contractor')


@pytest.fixture
def invoice(user, product, contractor):
    return Invoices.objects.create(
        number='INV-001',
        products=product,
        contractors=contractor,
        owner=user,
        amount=100,
        comment='Test comment',
        sale_date=date.today(),
        issue_date=date.today(),
        payment_date=date.today()
    )


@pytest.mark.django_db
def test_invoice_str_representation(invoice):
    assert str(invoice) == f'{invoice.owner} + {invoice.number}'


def test_invoice_owner(invoice, user):
    assert invoice.owner == user


def test_invoice_product(invoice, product):
    assert invoice.products == product


def test_invoice_contractor(invoice, contractor):
    assert invoice.contractors == contractor
