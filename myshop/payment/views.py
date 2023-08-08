from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
import stripe
from orders.models import Order


stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION