from django.http import HttpResponseNotAllowed, HttpResponse
import os

def filestorage(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return HttpResponse("FILE NOT PROVIDED", status=400)
        original_file = request.FILES['file']
        if os.path.exists("../file_repo/" + original_file.name):
            return HttpResponse('FILE ALREADY EXIST', status=406)
        with open("../file_repo/" + original_file.name, 'wb+') as destination:
            for chunk in original_file.chunks():
                destination.write(chunk)
        return HttpResponse(f'download at \'/download/?file={original_file.name}\'', status=201)
    if request.method == 'GET':
        return HttpResponse(""" 
<html>
    <head>
        <title>Upload</title>
    </head>
    <body>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>
    </body>
</html>
""")
    else:
        return HttpResponseNotAllowed(['POST','GET'])