# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Runar is a cryptographic messaging platform built with Django. It generates links to encrypted messages, hiding the privacy of sender and recipient. Messages are encrypted with AES-256-CBC and automatically deleted after 24 hours or upon first read.

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment (copy and configure)
cp Runar/example.env Runar/.env

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Run tests
python manage.py test messenger

# Lint
pylint messenger/

# Use alternate env file
ENV_PATH=other-env.env python manage.py runserver
```

## Architecture

### Project Structure
- `Runar/` - Django project settings and root URL configuration
- `messenger/` - Main Django app containing all business logic

### Core Components
- **Models** (`messenger/models.py`): Single `Message` model storing ciphertext, identifier (IV), creation timestamp, and default_key flag
- **Services** (`messenger/services.py`): Encryption/decryption logic using PyCryptodome AES-256-CBC
- **Views** (`messenger/views.py`): Request handlers for send/receive flow

### Message Flow
1. User submits message + optional key phrase via `/send`
2. `encrypt_message()` encrypts with AES, stores in DB, returns identifier (IV used as unique ID)
3. Generated URL contains hex-encoded identifier
4. Recipient visits `/receive/<identifier>`, enters key phrase
5. `decrypt_message()` retrieves, decrypts, then deletes message from DB

### Configuration
Environment variables loaded from `Runar/.env` via django-environ. Key settings:
- `DEFAULT_KEY`: Fallback encryption key when user provides none
- Database configured for PostgreSQL
- `ENV_PATH`: Override to use alternate env files
