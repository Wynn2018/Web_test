from django.shortcuts import render
from login.models import account
from login.models import D_O2
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.core.serializers import serialize


class Login(APIView):
    def post(self, request):
        print(request.data['ID'])
        id = request.data['ID']
        pas = request.data['Password']
        a = account.objects.all()
        c='no'
        for b in a:
            if(b.user == id):
                if(b.password == pas):
                    c = 'yes'
        print('yes')
        return Response(c)

    def get(self, request):
        c = 'no'
        print(request.data)
        print('meile')
        return Response(c)


class register(APIView):
    def post(self, request):
        a = account(user=request.data['ID'],password=request.data['Password'])
        a.save()
        return Response('注册成功')


class add_data(APIView):
    def post(self, request):
        a = D_O2(Province=request.data['P'])
        a.Year = request.data['Y']
        a.Data = request.data['D']
        a.save()
        c = D_O2.objects.all()
        return Response('添加成功')


class find_data(APIView):
    def post(self,request):
        a = D_O2.objects.all()
        for b in a:
            if(b.Province==request.GET.get('p1')):
                return Response(b.Data)
        return Response("未找到此用户")


def index(request):
    return render(request,'index.html')


def main(request):
    return render(request,'main.html')


class onload(APIView):
    def get(self,request):
        a = D_O2.objects.all()
        json_data = serialize('json', a)
        json_data = json.loads(json_data)
        return Response(json_data)


class search(APIView):
    def post(self, request):
        f = request.data['F']
        t = request.data['T']
        p = request.data['P']
        a = D_O2.objects.filter(Year__range=(f, t), Province__exact=p)
        json_data=serialize('json', a)
        json_data=json.loads(json_data)
        return Response(json_data)


class search_null(APIView):
    def post(self, request):
        f = request.data['F']
        t = request.data['T']
        a = D_O2.objects.filter(Year__range=(f, t))
        json_data = serialize('json', a)
        json_data = json.loads(json_data)
        return Response(json_data)

