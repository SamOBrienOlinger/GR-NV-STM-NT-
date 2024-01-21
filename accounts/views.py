from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Category
from .forms import MyForm

# Create your views here.

def account(request):
    """ A view to show the profile of a user """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'accounts/profile.html', context)

def update_budget(request):
    """  """

    categories = Category.objects.all()

    total_budget = int(request.POST.get('total_budget'))
    redirect_url = request.POST.get('redirect_url')
    amount = int(request.POST.get('expense_amount'))
    
    expenses = request.session.get('expenses', {})

    category_name = str(request.POST.get('categories'))
    
    if category_name in list(expenses.keys()):
        expenses[category_name] += amount
    else:
        expenses[category_name] = amount

    request.session['expenses'] = expenses
    request.session['total_budget'] = total_budget

    return redirect(redirect_url)


def adjust_budget(request):
    """ """

    category = str(request.POST.get('used_category'))
    new_amount = int(request.POST.get('new_amount'))
    redirect_url = request.POST.get('redirect_url')

    expenses = request.session.get('expenses', {})
    
    if new_amount > 0:
        expenses[category] = new_amount
    else:
        expenses.pop(category)

    # overwrite the variable with the updated version
    request.session['expenses'] = expenses
    print(expenses)

    return redirect(reverse('profile'))
