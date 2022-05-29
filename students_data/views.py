from logging import exception
from pprint import pprint
from django.shortcuts import render
from .models import StudentsData
from academic_calenders.models import Graduation
from academic_calenders.models import Batch
from academic_calenders.models import Department




# Create your views here.
def index(request):
    graduation_list = Graduation.objects.all()
    data_objects = {}
    try:
        for graduation_type in graduation_list:
            # print("\n=====================")
            # print("grad id : ",graduation_type.id, graduation_type.graduation)
            if graduation_type not in data_objects:
                data_objects[graduation_type] = {}
                batches_list = Batch.objects.filter(graduation=graduation_type.id)
                # print("batch list : ", batches_list)
                for batch in batches_list:
                    # print("batch id : ", batch.id)
                    departments_list = Department.objects.filter(batch=batch.id)
                    # print("department belogns to batch : ", departments_list)
                    data_objects[graduation_type][batch] = {}
                    for department in departments_list:
                        # print("current dept : ",department.id, department.department)
                        stu_details = StudentsData.objects.filter(graduation_id=graduation_type.id, batch_id=batch.id, department_id=department.id)
                        if len(stu_details) > 0:
                            data_objects[graduation_type][batch][department] = stu_details[0].doc_url
                            # print("\n")
                            # print(stu_details)
                        # print(f"{graduation_type.id} {batch.id} {department.id}")
                        # print(type(stu_details.doc_url))


                    # print(departments_list)
                    # print(batch.id)
                    # print(batch.batch)

                    # print("\n")
    except exception as e:
        print(e)
    else:
        print("_________________________________________\n")
        # for key in data_objects:
        #     batches_list = Batch.objects.filter(graduation=1)
        #     print(batches_list)

        # print(data_objects)
        for g_key,g_val in data_objects.items():
            print(g_key)
            for b_key,b_val in g_val.items():
                print(b_key)
                for d_key,d_val in b_val.items():
                    print(d_key)
                    print(d_val)
        pprint(data_objects)
        
        print("_________________________________________\n")

        # data_objects = StudentsData.objects.all()
    return render(request, 'students_data.html',{'data_objects' : data_objects})