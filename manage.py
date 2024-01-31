#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth import get_user_model


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openflix.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

    # Cria o superusuário se ele ainda não existir
    User = get_user_model()
    email = os.getenv("EMAIL_ADMIN")
    senha = os.getenv("SENHA_ADMIN")

    if email is not None and senha is not None:
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin', email=email, password=senha, is_active=True, is_staff=True)
        except Exception as e:
            print(f"Erro ao criar superusuário: {e}")


if __name__ == '__main__':
    main()
