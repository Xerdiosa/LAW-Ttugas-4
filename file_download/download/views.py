from django.http import HttpResponseNotAllowed, HttpResponse
import os, mimetypes

def filestorage(request):
    if request.method == 'GET':
        filename = request.GET.get('file')
        if filename is None:
            return HttpResponse("FILENAME NOT PROVIDED", status=400)
        if not os.path.exists("../file_repo/" + filename):
            return HttpResponse('FILE NOT FOUND', status=404)
        file_type = mimetypes.guess_type(filename)[0]
        file = open("../file_repo/" + filename, 'rb')
        response = HttpResponse(file.read(), content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename={filename}'
        file.close()
        return response
    else:
        return HttpResponseNotAllowed(['GET'])