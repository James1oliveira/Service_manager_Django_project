"""
Copies the services from the old db.sqlite3 file into the permanent database,
but only once: if the permanent database already has services, it does nothing.
"""
from django.conf import settings
from django.core.management.base import BaseCommand

from service_manager.models import Service


class Command(BaseCommand):
    help = "Copy the original services into the permanent database (first time only)"

    def handle(self, *args, **options):
        if "original" not in settings.DATABASES:
            self.stdout.write("No permanent database set up, nothing to copy.")
            return
        if Service.objects.exists():
            self.stdout.write("Permanent database already has services, nothing to copy.")
            return

        copied = 0
        for old in Service.objects.using("original").all():
            Service.objects.create(
                title=old.title,
                description=old.description,
                image=old.image.name if old.image else None,
            )
            copied += 1
        self.stdout.write(self.style.SUCCESS(f"Copied {copied} original services."))
