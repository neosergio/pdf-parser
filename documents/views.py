import tabula
from io import BytesIO
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST', ])
@permission_classes((AllowAny, ))
def document_upload(request):
    file_raw = request.FILES.get('file').read()
    if file_raw:
        pdf = tabula.read_pdf(
            BytesIO(file_raw),
            pages="all",
            multiple_tables=True,
            output_format="JSON")
        return Response(pdf, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
