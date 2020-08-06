from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Article
from .form import PostForm,CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users, admin_only
from .filters import ArticleFilter

# login required indique que l'user doit etre connecté
@login_required(login_url='login')
def blog_index(request):
    # recupere toute la data puis se sert du module filter pour reactualiser les objets selon les filtres
    article = Article.objects.all()

    myFilter = ArticleFilter(request.GET , queryset=article)

    article = myFilter.qs

    context ={"articles":article,"myFilter":myFilter}

    return render(request, 'blog/blog_index.html',context)

@login_required(login_url='login')
def article(request, article_id):
    # affiche un article selon un id passé dans l'url
    article = Article.objects.get(id=article_id)
    context ={"articles":article}
    return render(request, 'blog/article.html',context)

@login_required(login_url='login')
def update(request, article_id):
    # recupere les values d'un article puis remplis le form avec, lors du post recupere les values et les met a jour
    article = Article.objects.get(id=article_id)
    form = PostForm(instance=article)

    if request.method == "POST":
        form = PostForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blogIndex')
    
    context = {'form': form}
    return render(request, 'blog/update.html', context)


@login_required(login_url='login')
def create(request):
    # Verifie la méthode ensuite verifie la validité du formulaire, sauvegarde le form puis ajoute l'utilisateur connecté et sauvegarde
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blogIndex')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def delete(request,article_id):
    # delete selon un id
    article = Article.objects.get(id=article_id)
    article.delete()  
    return redirect("blogIndex") 

# bloque la page pour les users non authentifiés
@unauthenticated_user
def registerPage(request):
    # verifie que l'user n'est pas connecté et recupere le contenu du form pour l'ajotuer a la base et le redirige sur login
    if request.user.is_authenticated:
        return redirect("blogIndex")
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'Le compte a été crée pour ' + username)

                return redirect('login')
            

        context = {'form':form}
        return render(request, 'blog/register.html', context)

@unauthenticated_user
def loginPage(request):
# recupere les champ username et password et tente de se connecter si cela n'est pas bon il retourne un message indiquant
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('blogIndex')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'blog/login.html', context)

def logoutUser(request):
    # nous deconnecte
	logout(request)
	return redirect('login')


   