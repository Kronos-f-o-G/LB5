from django.shortcuts import render, redirect
from django.http import Http404
from .models import Shipment

def archive(request):
    return render(request, 'archive.html', {"posts": Shipment.objects.all()})

def get_article(request, article_id):
    try:
        post = Shipment.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Shipment.DoesNotExist:
        raise Http404

def create_post(request):
    # Проверяем, авторизован ли пользователь (is_anonymous - свойство, без скобок)
    if not request.user.is_anonymous:
        if request.method == "POST":
            # Обрабатываем данные формы, если метод POST
            form = {
                'text': request.POST.get("text", ""),
                'title': request.POST.get("title", "")
            }
            
            # Проверяем, что оба поля заполнены
            if form["text"] and form["title"]:
                # Проверка на уникальность названия маршрута
                if Shipment.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Перевозка с таким названием маршрута уже существует!"
                    return render(request, 'create_post.html', {'form': form})
                
                # Если название уникально — создаем запись
                article = Shipment.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            else:
                # Если поля пустые — возвращаем форму с ошибкой
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # Если метод GET — просто показываем пустую форму
            return render(request, 'create_post.html', {})
    else:
        # Если пользователь не авторизован — ошибка 404 (как в методичке)
        raise Http404