from .forms import SearchForm


def search(request):
    search_form = {'search_form': SearchForm}
    return search_form


