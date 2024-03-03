from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import TemplateView, ListView

from .models import News, Categories
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, template_name='news/news_list.html', context=context)


def notFound(request):
    return render(request, 'news/404.html')


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    categories = Categories.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]
    local_one = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[0]
    local_news = News.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_one': local_one,
        'local_news': local_news,
    }

    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[:6]
        context['xorij_xabarlar'] = News.published.all().filter(category__name="Xorij").order_by('-publish_time')[:6]
        context['texnologiya_xabarlar'] = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[:6]
        context['sport_xabarlar'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[:6]
        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h1>Biz bilan bog'langaningiz uchun raxmat!</h1>")
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'news/contact.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>Biz bilan bog\'langaningiz uchun raxmat</h2>')
        context = {
            'form': form,
        }
        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiglikalar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news


class FogiegnNewsView(ListView):
    model = News
    template_name = 'news/foreign.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news


class TexnologyNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologik_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.filter(category__name='Sport')
        return news



