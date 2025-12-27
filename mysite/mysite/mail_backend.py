from django.core.mail.backends.smtp import EmailBackend
import ssl
import certifi

class UnsafeEmailBackend(EmailBackend):
    def open(self):
        self.ssl_context = ssl._create_unverified_context()
        return super().open()
    

class VerifiedEmailBackend(EmailBackend):
    def open(self):
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        return super().open()    