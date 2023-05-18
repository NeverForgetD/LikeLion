from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Comment
from django.utils import timezone

# Create your views here.
def home(request):
    games = Game.objects.all()
    count = len(games)
    ctx = {
        'games': games,
        'count' : count,
    }
    return render(request, 'home.html', ctx)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'detail.html', {'game':game})

def create(request):
    if request.method == 'POST':
        game = Game()
        game.title = request.POST['title']
        game.playtime = float(request.POST['playtime'])
        game.review = request.POST['review']
        game.save()
        return redirect('detail', game.id)
    return render(request, 'create.html')

def comment(request, game_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.game = get_object_or_404(Game, pk=game_id)
        new_comment.comment = request.POST['comment']
        new_comment.created_at = timezone.now()
        new_comment.save()
    return redirect('detail', game_id)


def edit(request, game_id):
    edit_game = get_object_or_404(Game, pk=game_id)
    return render(request, 'edit.html', {'game':edit_game})