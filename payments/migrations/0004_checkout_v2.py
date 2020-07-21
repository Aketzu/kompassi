# Generated by Django 2.2.10 on 2020-07-21 13:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_event_cancelled'),
        ('payments', '0003_payment_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='test',
        ),
        migrations.CreateModel(
            name='CheckoutPayment',
            fields=[
                ('stamp', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.TextField(editable=False)),
                ('price_cents', models.IntegerField(editable=False)),
                ('items', django.contrib.postgres.fields.jsonb.JSONField(editable=False)),
                ('customer', django.contrib.postgres.fields.jsonb.JSONField(editable=False)),
                ('checkout_reference', models.TextField(blank=True, editable=False)),
                ('checkout_transaction_id', models.TextField(blank=True, editable=False)),
                ('provider', models.TextField(blank=True, editable=False)),
                ('status', models.CharField(choices=[('new', 'New'), ('ok', 'OK'), ('fail', 'Failed'), ('pending', 'Pending'), ('delayed', 'Delayed')], default='new', editable=False, max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Event')),
            ],
        ),
    ]
