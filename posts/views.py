from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import Post
from posts.forms import AddPostForm
from authentication.models import RedditUser
from subreddit.models import SubReddit


# Create your views here.
def add_post(request):
    html = "addpost.html"

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title = data['title'],
                body = data['body'],
            )
            author = RedditUser.objects.get(id=request.user.id)
            #subreddit = SubReddit.objects.get(name=data['name'])
            post = Post.objects.get(title=data['title'])
            post.author.add(author)
            #post.subreddit.add(subreddit)
            post.save()
            return HttpResponseRedirect(reverse('homepage'))

    form = AddPostForm()

    return render(request, html, {"form": form})


def up_vote(request, id):
    #http://www.cs.virginia.edu/~evans/cs1120-f09/ps/project/django.html
    up_post = Post.objects.get(id=id)
    up_post.up_vote += 1
    up_post.sum_of_votes += 1
    up_post.save()
    return HttpResponseRedirect(reverse('homepage'))


def down_vote(request, id):
    down_post = Post.objects.get(id=id)
    down_post.down_vote += 1
    down_post.sum_of_votes -= 1
    down_post.save()
    return HttpResponseRedirect(reverse('homepage'))


<<<<<<< Updated upstream
def all_posts_view(request):
    posts = Post.objects.all().order_by('date_created')
    return render(request, 'posts.html', {'posts':posts})
=======
def postview(request, id, name):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    # This adds a comment to the post
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        user = RedditUser.objects.get(id=request.user.id)
        post = Post.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                body=data['body'],
                user=user,
                post=post
            )
            try:
                parent_id = request.POST['comment_id']
            except:
                pass
            comment = Comment.objects.get(body=data['body'])
            comment.parent = comments.get(id=parent_id)
            comment.save()
            return HttpResponseRedirect(reverse('postview', kwargs={'name': name, 'id': id}))
>>>>>>> Stashed changes

