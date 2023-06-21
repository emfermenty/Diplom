from django.shortcuts import render, redirect
from .models import PDF
from .forms import PDFForm

def pdf_upload(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFForm()
    return render(request, 'pdfapp/pdf_upload.html', {'form': form})

def pdf_list(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdfapp/pdf_list.html', {'pdfs': pdfs})