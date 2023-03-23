from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Post, Category


class IndexView(ListView):
    model = Post
    paginate_by = 9
    ordering = '-create_at'
    template_name = 'blog/index.html'


class SearchView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        Post.objects.filter(
            title__icontains=self.request.GET.get('q')
        )
class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(slug=self.kwargs.get('slug'))


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return self.get_object().get_absolute_url()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)
