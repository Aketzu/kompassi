from django.conf.urls import include, url

from payments.views import (
    payments_checkout_success_view,
    payments_checkout_cancel_view,
    payments_checkout_success_callback,
    payments_checkout_cancel_callback,
)


urlpatterns = [
    url(
        r'payments/checkout/success/?$',
        payments_checkout_success_view,
        name="payments_checkout_success_view",
    ),

    url(
        r'payments/checkout/cancel/?$',
        payments_checkout_cancel_view,
        name="payments_checkout_cancel_view",
    ),

    url(
        r'payments/checkout/callbacks/success/?$',
        payments_checkout_success_callback,
        name="payments_checkout_success_callback",
    ),

    url(
        r'payments/checkout/cassbacks/cancel/?$',
        payments_checkout_cancel_callback,
        name="payments_checkout_cancel_callback",
    ),

]
