"""
Доменные классы заказов и клиентов.

Module: factory.domain.orders
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.orders.contract import Contract
from factory.domain.orders.customer import Customer
from factory.domain.orders.invoice import Invoice
from factory.domain.orders.order import Order
from factory.domain.orders.payment import Payment
from factory.domain.orders.production_plan import ProductionPlan


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Contract",
    "Customer",
    "Invoice",
    "Order",
    "Payment",
    "ProductionPlan",
]
