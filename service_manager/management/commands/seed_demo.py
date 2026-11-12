"""
Makes sure the demo login always exists.
Render's free plan resets the database file whenever the app sleeps or redeploys,
so this runs every time the app starts (see the Start Command on Render).
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

DEMO_USERNAME = "James"
DEMO_PASSWORD = "james1234"


class Command(BaseCommand):
    help = "Create (or reset) the demo login"

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username=DEMO_USERNAME)
        user.set_password(DEMO_PASSWORD)
        user.is_active = True
        user.save()
        self.stdout.write(self.style.SUCCESS(
            f"Demo login ready: {DEMO_USERNAME} ({'created' if created else 'reset'})"
        ))
