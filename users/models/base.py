__all__ = ('BaseAbstractUser',)

from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField, BooleanField, DateTimeField, DecimalField, ImageField

from users.models.manager import BaseManagerUser
from users.services.upload_files import upload_name


class BaseAbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()

    image = ImageField(upload_to=upload_name, blank=True)

    email = EmailField(_("email"),
                       unique=True,
                       help_text=_("Required. exsample@mail.com"),
                       validators=[email_validator],
                       error_messages={"unique": _("A user with that email already exists.")},
                       )

    username = CharField(_("username"),
                         max_length=150,
                         unique=True,
                         help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
                         validators=[username_validator],
                         error_messages={"unique": _("A user with that username already exists.")},
                         )

    is_staff = BooleanField(_("staff status"),
                            default=False,
                            help_text=_("Designates whether the user can log into this admin site."))

    is_active = BooleanField(_("active"),
                             default=False,
                             help_text=_(
                                 "Designates whether this user should be treated as active. "
                                 "Unselect this instead of deleting accounts."))

    objects = BaseManagerUser()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['id', 'email']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


