from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Transaction


def export_transactions_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'User', 'Amount', 'Status', 'Created At'])

    for transaction in queryset:
        writer.writerow([
            transaction.id,
            transaction.user.username,
            transaction.amount,
            transaction.status,
            transaction.created_at
        ])

    return response


export_transactions_csv.short_description = "Export Selected Transactions CSV"


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'status', 'created_at']
    actions = [export_transactions_csv]