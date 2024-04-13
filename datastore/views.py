from faker import Faker
from faker.generator import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StkEk, Insurance, Vignette, Mileage
from .serializers import StkEkSerializer, InsuranceSerializer, VignetteSerializer, MileageSerializer


class StkView(APIView):
    def get(self, request, vin):
        faker = Faker()
        inspection = StkEk.objects.filter(vin=vin, inspection_type='stk').first()
        inspection_date = faker.date_between(start_date='-1y', end_date='today')
        valid_to = faker.date_between(start_date=inspection_date, end_date='+2y')
        if not inspection:
            inspection = StkEk.objects.create(
                vin=vin,
                inspection_date=faker.date_between(start_date='-1y', end_date='today'),
                valid_to=valid_to,
                service_address=faker.address(),
                inspection_type='stk',
                protocol=faker.numerify(text="#########"),
                result=random.choice(['Pass', 'Fail']),
            )

        serializer = StkEkSerializer(inspection)
        return Response(serializer.data)


class EkView(APIView):
    def get(self, request, vin):
        faker = Faker()
        inspection = StkEk.objects.filter(vin=vin, inspection_type='ek').first()
        inspection_date = faker.date_between(start_date='-1y', end_date='today')
        valid_to = faker.date_between(start_date=inspection_date, end_date='+2y')
        if not inspection:
            inspection = StkEk.objects.create(
                vin=vin,
                inspection_date=inspection_date,
                valid_to=valid_to,
                service_address=faker.address(),
                inspection_type='ek',
                protocol=faker.numerify(text="#########"),
                result=random.choice(['Pass', 'Fail']),
            )

        serializer = StkEkSerializer(inspection)
        return Response(serializer.data)


class PzpView(APIView):
    def get(self, request, vin):
        faker = Faker()
        insurance = Insurance.objects.filter(vin=vin).first()
        insurance_date = faker.date_between(start_date='-1y', end_date='today')
        valid_to = faker.date_between(start_date=insurance_date, end_date='+2y')
        if not insurance:
            insurance = Insurance.objects.create(
                vin=vin,
                insurance_date=insurance_date,
                valid_to=valid_to,
                insurance_company=faker.company(),
                policy_number=faker.bothify(text='???-#######'),
            )

        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data)


class ZnamkaView(APIView):
    def get(self, request, vin):
        faker = Faker()
        vignette = Vignette.objects.filter(vin=vin).order_by('-valid_to').first()

        if not vignette:
            valid_from = faker.date_between(start_date='-1y', end_date='today')
            valid_to = faker.date_between(start_date=valid_from, end_date='+1y')
            vignette = Vignette.objects.create(
                vin=vin,
                type=random.choice(['Annual', 'Monthly', 'Weekly']),
                valid_from=valid_from,
                valid_to=valid_to,
                price=faker.pydecimal(left_digits=2, right_digits=2, positive=True),
            )

        serializer = VignetteSerializer(vignette)
        return Response(serializer.data)


class KmView(APIView):
    def get(self, request, vin):
        faker = Faker()
        mileage_record = Mileage.objects.filter(vin=vin).first()

        if not mileage_record:
            mileage_record = Mileage.objects.create(
                vin=vin,
                kilometers=str(faker.random_int(min=1000, max=300000)),
            )

        return Response({"km": mileage_record.kilometers})

