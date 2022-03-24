from urllib import response
from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {'id':1, 'nome':'Brendow'}
        return JsonResponse(aluno)