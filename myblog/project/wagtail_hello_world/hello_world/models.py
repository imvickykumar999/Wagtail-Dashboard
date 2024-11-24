from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HelloWorldPage(Page):
    """A simple Hello World page."""

    subtitle = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', heading="Subtitle"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['message'] = "Hello World"
        return context

class ToDoItem(models.Model):
    """Model for a to-do list item."""
    title = models.CharField(max_length=255, help_text="Title of the to-do item")
    description = models.TextField(blank=True, help_text="Optional description")
    is_completed = models.BooleanField(default=False, help_text="Mark as completed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
