from django.shortcuts import render, redirect, get_object_or_404
from .tasks import generate
# Create your views here.
from .models import ShootNumbers
from .forms import LottoForm
from .crawling import getLast, checkLast, crawler, insert

def index(request):
    lottos = ShootNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos": lottos})

def list(request):
    if request.method == "POST":
        return redirect('index')
    else:
        lottos = ShootNumbers.objects.all()
        return render(request, "lotto/list.html", {"lottos": lottos})

def post(request):
    if request.method == "POST":
        form = LottoForm(request.POST)
        if form.is_valid():
            lotto = form.save()
            # launch asynchronuous task
            generate.delay()
            return redirect('index')
    else:
        form = LottoForm()
        return render(request, 'lotto/form.html', {"form": form})

def detail(request, lottokey):
    if request.method == "POST":
        return redirect('list_lotto')
    else:
        # lotto = ShootNumbers.objects.get(pk = lottokey)
        lotto = get_object_or_404(ShootNumbers, pk = lottokey)
        return render(request, "lotto/detail.html", {"lotto": lotto})

def crawling(request):
    lotto_list = []
    last_time = getLast()
    dblast_time = checkLast()

    if request.method == "POST":
        return redirect('index')
    else:
        if dblast_time < last_time:
            lotto_list = crawler(dblast_time, last_time)
        #신규 회차 있을때 db update
        if len(lotto_list) > 0:
            insert(lotto_list)
        return render(request, 'lotto/crawling.html',{"last_time":last_time, "dblast_time":dblast_time})
