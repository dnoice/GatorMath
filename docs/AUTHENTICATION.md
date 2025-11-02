# GatorMath Authentication Documentation

**Version:** 0.1.0
**Last Updated:** 2025-11-02
**Document Path:** `/docs/AUTHENTICATION.md`
**Status:** Not Currently Implemented

---

## Table of Contents

1. [Current Status](#current-status)
2. [Future Implementation Guidelines](#future-implementation-guidelines)
3. [Recommended Architecture](#recommended-architecture)
4. [Security Best Practices](#security-best-practices)
5. [API Authentication](#api-authentication)

---

## Current Status

**GatorMath v0.1.0 does not implement user authentication.**

The current version is designed as an open-access mathematical toolkit:
- No user accounts required
- No login/registration system
- All features publicly accessible
- API endpoints are open (no authentication)

### Why No Authentication?

**Use Case:** GatorMath is a mathematical calculation and visualization toolkit, similar to a calculator or graphing tool. The primary use cases don't require user accounts:
- Performing mathematical calculations
- Visualizing geometric shapes
- Testing precision operations
- Learning mathematical concepts

**When Authentication Might Be Needed:**

If future versions add features such as:
- Saving calculations and projects
- User-specific settings and preferences
- Collaboration and sharing
- API rate limiting per user
- Premium features or tiered access

---

## Future Implementation Guidelines

If authentication becomes necessary, follow these guidelines for implementation.

### Recommended Approach

**Option 1: Session-Based Authentication (Web)**
- Suitable for: Web application with traditional server-rendered pages
- Technology: Flask-Login or Flask-Security
- Storage: Secure session cookies
- Use case: User dashboard, saved projects

**Option 2: Token-Based Authentication (API)**
- Suitable for: REST API clients, mobile apps, third-party integrations
- Technology: JWT (JSON Web Tokens) or API keys
- Storage: Tokens in headers
- Use case: Programmatic API access

**Option 3: OAuth 2.0 (Third-Party)**
- Suitable for: "Sign in with Google/GitHub" functionality
- Technology: Authlib or Flask-Dance
- Provider: Google, GitHub, Microsoft
- Use case: Quick sign-up without password management

### Technology Stack Recommendations

**Flask Extensions:**
```python
# Session-based
pip install Flask-Login Flask-Bcrypt

# Token-based
pip install Flask-JWT-Extended

# OAuth
pip install Authlib

# Database
pip install Flask-SQLAlchemy Flask-Migrate
```

---

## Recommended Architecture

### User Model (SQLAlchemy)

```python
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    User account model.

    Attributes:
        id: Primary key
        username: Unique username
        email: Unique email address
        password_hash: Bcrypt password hash
        created_at: Account creation timestamp
        last_login: Last login timestamp
        is_active: Account active status

    Version: 0.2.0 (future)
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password: str) -> None:
        """Hash and set password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verify password against hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'<User {self.username}>'
```

### Authentication Routes

```python
from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register new user account.

    Request JSON:
        {
            "username": str,
            "email": str,
            "password": str
        }

    Returns:
        JSON response with user ID or error

    Version: 0.2.0 (future)
    """
    data = request.get_json()

    # Validate input
    if not all(k in data for k in ['username', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if user exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400

    # Create user
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login user and create session.

    Request JSON:
        {
            "email": str,
            "password": str
        }

    Returns:
        JSON response with success status

    Version: 0.2.0 (future)
    """
    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.check_password(data.get('password')):
        return jsonify({'error': 'Invalid credentials'}), 401

    login_user(user)
    user.last_login = datetime.utcnow()
    db.session.commit()

    return jsonify({
        'message': 'Login successful',
        'user': {'id': user.id, 'username': user.username}
    }), 200


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    """
    Logout current user.

    Version: 0.2.0 (future)
    """
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200


@auth_bp.route('/me', methods=['GET'])
@login_required
def get_current_user():
    """
    Get current authenticated user info.

    Version: 0.2.0 (future)
    """
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'email': current_user.email,
        'created_at': current_user.created_at.isoformat()
    }), 200
```

---

## Security Best Practices

### Password Security

**Requirements:**
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

**Hashing:**
- Use bcrypt or argon2 (never plain text)
- Salt automatically included in hash
- Cost factor: 12-14 rounds (bcrypt)

**Implementation:**
```python
from werkzeug.security import generate_password_hash, check_password_hash

# Hash password
password_hash = generate_password_hash(password, method='pbkdf2:sha256')

# Verify password
is_valid = check_password_hash(password_hash, password)
```

### Session Security

**Flask Configuration:**
```python
app.config.update(
    # Secret key (use environment variable)
    SECRET_KEY=os.environ.get('SECRET_KEY'),

    # Session configuration
    SESSION_COOKIE_SECURE=True,      # HTTPS only
    SESSION_COOKIE_HTTPONLY=True,    # No JavaScript access
    SESSION_COOKIE_SAMESITE='Lax',   # CSRF protection
    PERMANENT_SESSION_LIFETIME=3600,  # 1 hour timeout
)
```

### HTTPS/TLS

**Production Requirements:**
- Always use HTTPS in production
- Redirect HTTP to HTTPS
- Use TLS 1.2 or higher
- Obtain certificate from Let's Encrypt or trusted CA

**Flask Configuration:**
```python
from flask_talisman import Talisman

# Force HTTPS
if not app.debug:
    Talisman(app, content_security_policy=None)
```

### CSRF Protection

**Flask-WTF:**
```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

# Exempt API endpoints if using token auth
@csrf.exempt
@auth_bp.route('/api/login', methods=['POST'])
def api_login():
    pass
```

### Rate Limiting

**Flask-Limiter:**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    pass
```

---

## API Authentication

### JWT Token Authentication (Recommended for API)

**Implementation:**
```python
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour

@auth_bp.route('/api/login', methods=['POST'])
def api_login():
    """
    API login returning JWT token.

    Request JSON:
        {
            "email": str,
            "password": str
        }

    Response JSON:
        {
            "access_token": str,
            "expires_in": int
        }

    Version: 0.2.0 (future)
    """
    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.check_password(data.get('password')):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        'access_token': access_token,
        'token_type': 'Bearer',
        'expires_in': 3600
    }), 200


@api_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    """
    Protected API endpoint requiring JWT.

    Usage:
        Authorization: Bearer <token>

    Version: 0.2.0 (future)
    """
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    return jsonify({'message': f'Hello {user.username}'}), 200
```

### API Key Authentication (Simple Alternative)

**Implementation:**
```python
import secrets
from functools import wraps

class APIKey(db.Model):
    """API key for programmatic access."""
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_used = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    @staticmethod
    def generate_key() -> str:
        """Generate secure random API key."""
        return secrets.token_urlsafe(48)


def require_api_key(f):
    """Decorator to require API key authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')

        if not api_key:
            return jsonify({'error': 'API key required'}), 401

        key_obj = APIKey.query.filter_by(key=api_key, is_active=True).first()

        if not key_obj:
            return jsonify({'error': 'Invalid API key'}), 401

        # Update last used
        key_obj.last_used = datetime.utcnow()
        db.session.commit()

        return f(*args, **kwargs)

    return decorated_function


@api_bp.route('/calculate', methods=['POST'])
@require_api_key
def calculate():
    """Protected calculation endpoint."""
    pass
```

**Usage:**
```bash
curl -X POST https://api.gatormath.com/calculate \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 1, "b": 2}'
```

---

## Migration Path

If authentication is added in a future version, follow this migration path:

### Phase 1: Optional Authentication
- Add authentication routes
- Make authentication optional
- All features remain publicly accessible
- Users can optionally create accounts to save work

### Phase 2: Progressive Enhancement
- Add user-specific features (saved calculations, history)
- Keep core mathematical functions public
- Authentication required only for personalized features

### Phase 3: Full Integration (if needed)
- API rate limiting per user
- Advanced features behind authentication
- User dashboards and collaboration

---

## References

**Flask Authentication Resources:**
- Flask-Login: https://flask-login.readthedocs.io/
- Flask-JWT-Extended: https://flask-jwt-extended.readthedocs.io/
- Flask-Security: https://flask-security-too.readthedocs.io/
- Authlib: https://docs.authlib.org/

**Security Resources:**
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

---

**Version:** 0.1.0 (Authentication not implemented)
**See Also:** [API Docs](API_DOCS.md) | [Development Guide](DEVELOPMENT.md) | [Standards](STANDARDS.md)
