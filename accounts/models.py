from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		"""
		creates a user with given email and password
		"""
		if not username:
			raise ValueError('user must have a username')

		if not email:
			raise ValueError('user must have a email address')

		user = self.model(
			username=self.normalize_email(username),
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(self._db)
		return user

	def create_staffuser(self, username, email, password):
		"""
		creates a user with staff permissions
		"""
		user = self.create_user(
			username=username,
			email=email,
			password=password
		)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		"""
		creates a superuser with email and password
		"""
		user = self.create_user(
			username=username,
			email=email,
			password=password
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(
		verbose_name='Email address',
		max_length=255,
		unique=True
	)

	date_joined = models.DateTimeField(default=timezone.now)
	date_updated = models.DateTimeField()

	active = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)  # <- admin user, not super user
	admin = models.BooleanField(default=False)  # <- super user

	# notice the absence of password field
	# that is built in

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']  # <- email and password are required by default

	def get_full_name(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		"""Does the user has a specific permission"""
		return True

	def has_module_perms(self, app_lable):
		"""Does the user has permission to view a specific app"""
		return True

	@property
	def is_staff(self):
		"""Is the user a staff member"""
		return self.staff

	@property
	def is_admin(self):
		"""Is the user a admin member"""
		return self.admin

	@property
	def is_active(self):
		"""Is the user active"""
		return self.active

	# hook the user manager to objects
	objects = UserManager()

	def save(self):
		self.date_updated = timezone.now()
		self.last_login = timezone.now()
		return super().save()
