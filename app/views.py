from django.shortcuts import render
# Create your views here.

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, APIView
from .models import Mijoz, Xodim, Tovar, Zakaz ,Statistics
from rest_framework.response import Response
from rest_framework import serializers

class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zakaz
        fields = '__all__'    

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = '__all__'    

class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = '__all__'    

class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'    

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'    



# @api_view([])




    # @swagger_auto_schema(method='get')

class StatisticsViews(APIView):

    def get(self,request,pk, *args, **kwargs):

        month = request.query_params.get("month")
        year = request.query_params.get("year")

        try:
            month = int(month)
            year = int(year)
        except Exception as e:
            return Response({"error":str(e)})
        # zakaz = Zakaz.objects.all()
        xodim = Xodim.objects.all()
        mijoz = Mijoz.objects.all()
        tovar = Zakaz.objects.all()
        statistic = Statistics.objects.all()

        statist = Statistics.objects.filter(xodim = pk).first()

        if month:
            zakaz = Zakaz.objects.filter(created_at__month=month)
        if year:
            zakaz = Zakaz.objects.filter(created_at__year=year)
    
        # print(statist.id,statist.mijoz,statist.xodim)
        mijozlar_soni = 0
        print(xodim)
        mahsulotlar_soni = zakaz.count()

        xodim_id = 1


        # for i in xodim:
        #     print(i.id)
        # print(zakaz)
        for z in zakaz:
            # print(z.mijoz.id,z.xodim.id,)
            if z.xodim.id == xodim_id:
                mijozlar_soni += 1

        print(mijozlar_soni)
        serializer = StatisticsSerializer(statistic, many=True)
        return Response(serializer.data)