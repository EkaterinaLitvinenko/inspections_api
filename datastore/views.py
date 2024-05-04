from datetime import timezone, timedelta

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

        existing_inspections = StkEk.objects.filter(vin=vin, inspection_type='stk')

        if not existing_inspections.exists():
            num_inspections = random.randint(1, 3)
            inspections = []
            for _ in range(num_inspections):
                inspection_date = faker.date_between(start_date='-1y', end_date='today')
                valid_to = faker.date_between(start_date=inspection_date, end_date='+2y')
                inspection = StkEk.objects.create(
                    vin=vin,
                    inspection_date=inspection_date,
                    valid_to=valid_to,
                    service_address=faker.address(),
                    inspection_type='stk',
                    protocol=faker.numerify(text="#########"),
                    result=random.choices(['Pass', 'Fail'], weights=[9, 1], k=1)[0],
                )
                inspections.append(inspection)
        else:
            inspections = list(existing_inspections)

        serializer = StkEkSerializer(inspections, many=True)
        return Response(serializer.data)


class EkView(APIView):
    def get(self, request, vin):
        faker = Faker()

        existing_inspections = StkEk.objects.filter(vin=vin, inspection_type='ek')

        if not existing_inspections.exists():
            num_inspections = random.randint(1, 3)
            inspections = []
            for _ in range(num_inspections):
                inspection_date = faker.date_between(start_date='-1y', end_date='today')
                valid_to = faker.date_between(start_date=inspection_date, end_date='+2y')
                inspection = StkEk.objects.create(
                    vin=vin,
                    inspection_date=inspection_date,
                    valid_to=valid_to,
                    service_address=faker.address(),
                    inspection_type='ek',
                    protocol=faker.numerify(text="#########"),
                    result=random.choices(['Pass', 'Fail'], weights=[9, 1], k=1)[0],
                )
                inspections.append(inspection)
        else:
            inspections = list(existing_inspections)

        serializer = StkEkSerializer(inspections, many=True)
        return Response(serializer.data)


class PzpView(APIView):
    def get(self, request, vin):
        faker = Faker()
        insurances = list(Insurance.objects.filter(vin=vin))

        if not insurances:
            num_insurances = random.randint(1, 3)
            for _ in range(num_insurances):
                insurance_date = faker.date_between(start_date='-1y', end_date='today')
                valid_to = faker.date_between(start_date=insurance_date, end_date='+2y')
                insurance = Insurance.objects.create(
                    vin=vin,
                    insurance_date=insurance_date,
                    valid_to=valid_to,
                    insurance_company=faker.company(),
                    policy_number=faker.bothify(text='???-#######'),
                )
                insurances.append(insurance)

        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data)


class ZnamkaView(APIView):
    def get(self, request, vin):
        faker = Faker()

        vignettes = list(Vignette.objects.filter(vin=vin).order_by('-valid_to'))

        if not vignettes:
            num_vignettes = random.randint(1, 7)
            for _ in range(num_vignettes):
                valid_from = faker.date_between(start_date='-1y', end_date='today')
                type_choice = random.choice(['Annual', '365', '30', '10'])

                if type_choice in ['Annual', '365']:
                    price = 60.00
                elif type_choice == '30':
                    price = 17.00
                elif type_choice == '10':
                    price = 12.00
                else:
                    price = 0

                if type_choice == 'Annual':
                    next_year = valid_from.year + 1
                    valid_to = timezone.datetime(next_year, 1, 1).date()
                elif type_choice == '365':
                    valid_to = valid_from + timedelta(days=365)
                elif type_choice == '30':
                    valid_to = valid_from + timedelta(days=30)
                elif type_choice == '10':
                    valid_to = valid_from + timedelta(days=10)

                new_vignette = Vignette.objects.create(
                    vin=vin,
                    type=type_choice,
                    valid_from=valid_from,
                    valid_to=valid_to,
                    price=price,
                )
                vignettes.append(new_vignette)

        # Serialize and return all vignettes
        serializer = VignetteSerializer(vignettes, many=True)
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

