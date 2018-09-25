from common.mymako import render_mako_context,render_json
from iwork.models import workRecord

# Create your views here.


def home(request):
    return render_mako_context(request, '/iwork/home.html')


def save_record(request):
    theme = request.POST.get('theme', '')
    content = request.POST.get('content', '')

    data = {
        'theme': theme,
        'content': content,
        'username': request.user.username,
    }
    result = workRecord.objects.save_record(data)
    return render_json(result)


def records(request):
    record_list = workRecord.objects.all().order_by('-id')
    data = []
    for index, record in enumerate(record_list):
        data.append({
            'index': index,
            'theme': record.theme,
            'content': record.content,
        })
    return render_json({'code': 0, 'message': 'success', 'data': data})