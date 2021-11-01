from django.shortcuts import redirect, render
from .models import Post, CommentModel
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.


def index(request):
    posts = Post.objects.filter(status='Published')
    return render(request, 'index.html', {'posts': posts})


def article(request, slug):
    post = Post.objects.get(slug=slug)
    comments  = CommentModel.objects.filter(post=post)[::-1]
    likes = post.likes.count()
    print(comments)
    if request.method == 'POST':
        comment = request.POST['comment']
        obj = CommentModel(post  = post, user = request.user, text = comment)
        obj.save()
        return redirect('article',slug = post.slug)


    return render(request, 'article.html', {'post': post,'comments' : comments,'likes':likes})


def signup(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            user = User.objects.filter(email=email)
            if len(user) == 0:
                raise User.DoesNotExist
            return render(request, 'signup.html', {'msg': 'Email already exists 🔑'})
        except User.DoesNotExist:
                # user = '@'+request.POST['email']
            user_obj = User.objects.create_user(
                first_name=request.POST['fname'], last_name=request.POST['lname'], username=request.POST['email'], password=request.POST['pass'], email=request.POST['email'])
            print(user_obj)

            user_obj.save()
            # print(request.POST['isauthor'])
            try:
                if request.POST['isauthor'] == 'on':
                    user_obj.is_staff = True
                    group = Group.objects.get(name='Author')
                    print(group)
                    user_obj.groups.add(group)
                    user_obj.save()
            except:
                pass
        return redirect('signin')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        try:
            uname = request.POST['email']
            pwd = request.POST['pass']

            uid = User.objects.get(username=uname)

            user_authenticate = auth.authenticate(username=uname, password=pwd)
            print(user_authenticate)
            if user_authenticate is not None:
                    auth.login(request, user_authenticate)
                    request.session['username'] = uname
                    return redirect('profile')
            else:
                print('Login Failed')
                return render(request, 'signin.html', {"msg": "Invalid Credentials ❌"})
        except:
            pass
    else:
        return render(request, 'signin.html', {"msg": "Please Verify your Account ‼"})

        




def logout(request,):

    uid = User.objects.get(username=request.user)
    print(uid)
    auth.logout(request)

    if request.session.has_key('username'):
        del request.session['username']
    else:
        pass

    return redirect('signin')

def profile(request):

    if request.session.has_key('username'):
        return render(request, 'profile.html')
    else:
        return redirect('signin')

def likesPost(request, slug):
    post = Post.objects.get(slug =slug)
    if request.session.has_key('username'):
        print(post)
        post.likes.add(request.user)
        print(post.likes)
        return redirect('article',slug = post.slug)

        
