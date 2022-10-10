from tasks.models import Type

def get_type_query_set():
    return Type.objects.all()