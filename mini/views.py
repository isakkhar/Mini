from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from .models import Post, Author, Category, Tag, Comment, Portfolio, Service, Testimonial, Partner
from .forms import CommentForm, ContactForm  # You'll create this form
# from mini.views import home, about, post_detail, posts_by_author, posts_by_category, posts_by_tag

def home(request):
    post_list = Post.objects.filter(status='published').order_by('-published_date')
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    editors_picks = Post.objects.filter(status='published', is_editors_pick=True).order_by('-published_date')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:12]

    return render(request, 'mini/index.html', {
        'posts': posts,
        'editors_picks': editors_picks,
        'categories': categories,
        'tags': tags,
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
    recent_posts = Post.objects.filter(status='published').order_by('-published_date')[:5]
    return render(request, 'mini/posts_by_tag.html', {
        'tag': tag,
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'mini/contact.html', {'form': form})

def portfolio(request):
    projects = Portfolio.objects.all().order_by('-created')
    categories = Portfolio.CATEGORY_CHOICES
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()
    return render(request, 'mini/portfolio.html', {
        'projects': projects,
        'categories': categories,
        'services': services,
        'testimonials': testimonials,
        'partners': partners,
    })

def portfolio_detail(request, slug):
    project = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'mini/portfolio_detail.html', {'project': project})