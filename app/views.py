from django.shortcuts import render
# Create your views here.

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, APIView
from .models import Mijoz, Xodim, Tovar, Zakaz, ZakazItem 
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

# class ZakazSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Statistics
#         fields = '__all__'    

# class StatisticsSerializer(serializers.ModelSerializer):
#     class Meta:
#         # model = Statistics
#         fields = '__all__'    



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
        zakaz = Zakaz.objects.filter(xodim_id=pk)
        xodim = Xodim.objects.all()
        # mijoz = Mijoz.objects.all()
        # tovar = Zakaz.objects.all()
        # statistic = Statistics.objects.all()

        # statist = Statistics.objects.filter(xodim = pk).first()

        if month:
            zakaz = zakaz.filter(created_at__month=month)
        if year:
            zakaz = zakaz.filter(created_at__year=year)
    
        # print(statist.id,statist.mijoz,statist.xodim)
        mijozlar_soni = 0
        # print(xodim)
        # zakaz1 = 
        mahsulotlar_soni = zakaz.count()


        # for i in xodim:
        #     print(i.id)
        # print(zakaz)
        # for z in zakaz:
        #     # print(z.mijoz.id,z.xodim.id,)
        #     if z.xodim.id == pk:
        #         mijozlar_soni += 1
        # xodim_id = 1


        total_zakaz = zakaz.count()
        unique_clients = zakaz.values("mijoz").distinct().count()
        total_products = sum(item.quantity for o in zakaz for item in o.items.all())
        total_sales = sum(item.quantity * item.price for o in zakaz for item in o.items.all())

        print(mijozlar_soni)
        data = {
            "employee_id": pk,
            "total_orders": total_zakaz,
            "unique_clients": unique_clients,
            "total_products": total_products,
            "total_sales": total_sales,
        }
        return Response(data)

        # # serializer = StatisticsSerializer(statistic, many=True)
        # return Response(serializer.data)