from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News
from .forms import NewsForm

def news_list(request):
    news_items = News.objects.all()
    per_page = request.GET.get('per_page', 10)
    paginator = Paginator(news_items, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news_feed/news_list.html', {
        'page_obj': page_obj,
        'per_page': per_page
    })

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()

    return render(request, 'news_feed/add_news.html', {'form': form})