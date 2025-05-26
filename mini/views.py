from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Post, Author, Category, Tag, Comment
from .forms import CommentForm  # You'll create this form

def home(request):
    posts = Post.objects.filter(status='published').order_by('-published_date')[:10]
    editors_picks = Post.objects.filter(status='published', is_editors_pick=True).order_by('-published_date')[:3]
    categories = Category.objects.all()
    return render(request, 'mini/index.html', {
        'posts': posts,
        'editors_picks': editors_picks,
        'categories': categories,
    })

def about(request):
    return render(request, 'mini/about.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    categories = Category.objects.annotate(num_posts=Count('posts'))
    popular_posts = Post.objects.filter(status='published').order_by('-views', '-published_date')[:5]
    tags = Tag.objects.all()
    last_comments = post.comments.filter(active=True).order_by('-created')[:5]  # Get last 5 comments for this post

    return render(request, 'mini/post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'categories': categories,
        'popular_posts': popular_posts,
        'tags': tags,
        'last_comments': last_comments,
    })

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author, status='published')
    return render(request, 'mini/posts_by_author.html', {'author': author, 'posts': posts})

def posts_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts_list = Post.objects.filter(category=category, status='published').order_by('-published_date')
    paginator = Paginator(posts_list, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    categories = Category.objects.all()
    popular_posts = Post.objects.filter(status='published').order_by('-views', '-published_date')[:5]  # or use your own logic for "popular"
    return render(request, 'mini/posts_by_category.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
        'popular_posts': popular_posts,
    })

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag, status='published').order_by('-published_date')
    categories = Category.objects.annotate(num_posts=Count('posts'))
    popular_posts = Post.objects.filter(status='published').order_by('-views', '-published_date')[:5]
    tags = Tag.objects.all()
    recent_comments = Comment.objects.filter(active=True).order_by('-created')[:3]
    return render(request, 'mini/posts_by_tag.html', {
        'tag': tag,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })