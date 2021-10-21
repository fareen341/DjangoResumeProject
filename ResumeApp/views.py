from re import X
from django.http import HttpResponse, response
from django.template.loader import get_template		#for pdf
from django.views.generic import View
from .utils import render_to_pdf 
from django.shortcuts import render


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        name=request.COOKIES.get('name', "not found")
        email=request.COOKIES.get('email', "not found")
        contact=request.COOKIES.get('contact', "not found")
        summary=request.COOKIES.get('summary', "not found") 
        employment1=request.COOKIES.get('employment1', "not found")
        date1=request.COOKIES.get('date1', "not found")
        desc1=request.COOKIES.get('desc1', "not found")
        place1=request.COOKIES.get('place1', "not found")

        # employment2=request.COOKIES.get('employment2')
        # date2=request.COOKIES.get('date2')
        # desc2=request.COOKIES.get('desc2')
        # place2=request.COOKIES.get('place2')
        
        employment3=request.COOKIES.get('employment3', "not found")
        date3=request.COOKIES.get('date3', "not found")
        desc3=request.COOKIES.get('desc3', "not found")
        place3=request.COOKIES.get('place3', "not found")

        education1=request.COOKIES.get('education1', "not found")
        edate1=request.COOKIES.get('edate1', "not found")
        edesc1=request.COOKIES.get('edesc1', "not found")
        eplace1=request.COOKIES.get('eplace1', "not found")

        education2=request.COOKIES.get('education2', "not found")
        edate2=request.COOKIES.get('edate2', "not found")
        edesc2=request.COOKIES.get('edesc2', "not found")
        eplace2=request.COOKIES.get('eplace2', "not found")

        education3=request.COOKIES.get('education3', "not found")
        edate3=request.COOKIES.get('edate3', "not found")
        edesc3=request.COOKIES.get('edesc3', "not found")
        eplace3=request.COOKIES.get('eplace3', "not found")

        prodject1=request.COOKIES.get('prodject1', "not found")
        pdate1=request.COOKIES.get('pdate1', "not found")
        pdesc1=request.COOKIES.get('pdesc1', "not found")
        pplace1=request.COOKIES.get('pplace1', "not found")

        prodject2=request.COOKIES.get('prodject2', "not found")
        pdate2=request.COOKIES.get('pdate2', "not found")
        pdesc2=request.COOKIES.get('pdesc2', "not found")
        pplace2=request.COOKIES.get('pplace2', "not found")

        cert1=request.COOKIES.get('cert1', "not found")
        cdate1=request.COOKIES.get('cdate1', "not found")
        cdesc1=request.COOKIES.get('cdesc1', "not found")
        cplace1=request.COOKIES.get('cplace1', "not found")

        cert2=request.COOKIES.get('cert2', "not found")
        cdate2=request.COOKIES.get('cdate2', "not found")
        cdesc2=request.COOKIES.get('cdesc2', "not found")
        cplace2=request.COOKIES.get('cplace2', "not found")


        address=request.COOKIES.get('address', "not found") 
        template = get_template('invoice.html')
        context = {
            "name":name,
            "summary":summary,
            "email":email,
            "contact":contact,
            
            "employment1":employment1,
            "date1":date1,
            "desc1":desc1,
            "place1":place1,

            # "employment2":employment2,
            # "date2":date2,
            # "desc2":desc2,
            # "place2":place2,

            "employment3":employment3,
            "date3":date3,
            "desc3":desc3,
            "place3":place3,

            "education1":education1,
            "edate1":edate1,
            "edesc1":edesc1,
            "eplace1":eplace1,

            "education2":education2,
            "edate2":edate2,
            "edesc2":edesc2,
            "eplace2":eplace2,

            "education3":education3,
            "edate3":edate3,
            "edesc3":edesc3,
            "eplace3":eplace3,

            "address":address,

            "prodject1":prodject1,
            "pdate1":pdate1,
            "pdesc1":pdesc1,
            "pplace1":pplace1,

            "prodject2":prodject2,
            "pdate2":pdate2,
            "pdesc2":pdesc2,
            "pplace2":pplace2,

            "cert1":cert1,
            "cdate1":cdate1,
            "cdesc1":cdesc1,
            "cplace1":cplace1,

            "cert2":cert2,
            "cdate2":cdate2,
            "cdesc2":cdesc2,
            "cplace2":cplace2



            # "invoice_id": 123,
            # "customer_name": "John Cooper",
            # "amount": 1399.99,
            # "today": "Today",
            
        }
        html = template.render(context)
        # pdf.set_font('Times')
        # pdf.add_font('Comic Sans','','/usr/share/fonts/truetype/msttcorefonts/Comic_Sans_MS.ttf', uni=True)
        # # Set font family to Comic Sans, 'U'nderlined, size 14.0 pt
        # pdf.set_font('Comic Sans','U',14.0)
        pdf = render_to_pdf('invoice.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def home_view(request):
    x=request.GET
    print(x)
    if x:
        name=x['name']
        email=x['email']
        contact=x['contact']
        summary=x['summary']
        address=x['address']
        # skills = x['your_skills']
        # s=list(skills)
        employment1 = x['employment1']
        date1=x['date1']
        desc1=x['desc1']
        place1=x['place1']
        # employment2 = x['employment2']
        # date2=x['date2']
        # desc2=x['desc2']
        # place2=x['place2']
        employment3 = x['employment3']
        date3=x['date3']
        desc3=x['desc3']
        place3=x['place3']
        #education
        education1 = x['education1']
        edate1=x['edate1']
        edesc1=x['edesc1']
        eplace1=x['eplace1']
        education2 = x['education2']
        edate2=x['edate2']
        edesc2=x['edesc2']
        eplace2=x['eplace2']
        education3 = x['education3']
        edate3=x['edate3']
        edesc3=x['edesc3']
        eplace3=x['eplace3']
        #Project Detail
        prodject1=x['prodject1']
        pdate1=x['pdate1']
        pdesc1=['pdesc1']
        pplace1=x['pplace1']
        prodject2=x['prodject2']
        pdate2=x['pdate2']
        pdesc2=['edesc2']
        pplace2=x['pplace2']
        #certifucation detail
        cert1=x['cert1']
        cdate1=x['cdate1']
        cdesc1=x['cdesc1']
        cplace1=x['cplace1']
        cert2=x['cert2']
        cdate2=x['cdate2']
        cdesc2=x['cdesc2']
        cplace2=x['cplace2']
        response=render(request,'home.html')    
        response.set_cookie('name', name) 
        response.set_cookie('email', email) 
        response.set_cookie('contact', contact) 
        response.set_cookie('address', address) 
        response.set_cookie('summary', summary) 
        response.set_cookie('employment1', employment1) 
        response.set_cookie('date1', date1) 
        response.set_cookie('desc1', desc1) 
        response.set_cookie('place1', place1) 

        # response.set_cookie('employment2', employment2) 
        # response.set_cookie('date2', date2) 
        # response.set_cookie('desc2', desc2) 
        # response.set_cookie('place2', place2)

        response.set_cookie('employment3', employment3)
        response.set_cookie('date3', date3) 
        response.set_cookie('desc3', desc3) 
        response.set_cookie('place3', place3)

        response.set_cookie('education1', education1)
        response.set_cookie('edate1', edate1) 
        response.set_cookie('edesc1', edesc1) 
        response.set_cookie('eplace1', eplace1)

        response.set_cookie('education2', education2) 
        response.set_cookie('edate2', edate2) 
        response.set_cookie('edesc2', edesc2) 
        response.set_cookie('eplace2', eplace2)

        response.set_cookie('education3', education3)
        response.set_cookie('edate3', edate3) 
        response.set_cookie('edesc3', edesc3) 
        response.set_cookie('eplace3', eplace3) 

        response.set_cookie('prodject1', prodject1)
        response.set_cookie('pdate1', pdate1)
        response.set_cookie('pdesc1', pdesc1)
        response.set_cookie('pplace1', pplace1)     

        response.set_cookie('prodject2', prodject2)
        response.set_cookie('pdate2', pdate2)
        response.set_cookie('pdesc2', pdesc2)
        response.set_cookie('pplace2', pplace2)

        response.set_cookie('cert1', cert1)
        response.set_cookie('cdate1', cdate1)
        response.set_cookie('cdesc1', cdesc1)
        response.set_cookie('cplace1', cplace1)    

        response.set_cookie('cert2', cert2)
        response.set_cookie('cdate2', cdate2)
        response.set_cookie('cdesc2', cdesc2)
        response.set_cookie('cplace2', cplace2) 
        return response
    else:
        print("no data")
    return render(request, 'home.html')
   


def home_view2(request):
    x=request.GET
    print(x)
    if x:
        name=x['name']
        email=x['email']
        contact=x['contact']
        summary=x['summary']
        address=x['address']
        # skills = x['your_skills']
        # s=list(skills)
        employment1 = x['employment1']
        date1=x['date1']
        desc1=x['desc1']
        place1=x['place1']
        employment2 = x['employment2']
        date2=x['date2']
        desc2=x['desc2']
        place2=x['place2']
        # employment3 = x['employment3']
        # date3=x['date3']
        # desc3=x['desc3']
        # place3=x['place3']
        #education
        education1 = x['education1']
        edate1=x['edate1']
        edesc1=x['edesc1']
        eplace1=x['eplace1']
        education2 = x['education2']
        edate2=x['edate2']
        edesc2=x['edesc2']
        eplace2=x['eplace2']
        education3 = x['education3']
        edate3=x['edate3']
        edesc3=x['edesc3']
        eplace3=x['eplace3']
        #Project Detail
        prodject1=x['prodject1']
        pdate1=x['pdate1']
        pdesc1=['pdesc1']
        pplace1=x['pplace1']
        prodject2=x['prodject2']
        pdate2=x['pdate2']
        pdesc2=['edesc2']
        pplace2=x['pplace2']
        #certifucation detail
        cert1=x['cert1']
        cdate1=x['cdate1']
        cdesc1=x['cdesc1']
        cplace1=x['cplace1']
        cert2=x['cert2']
        cdate2=x['cdate2']
        cdesc2=x['cdesc2']
        cplace2=x['cplace2']
        #skills
        skills1=['skill1']
        skills2=['skill2']
        skills3=['skill3']
        skills4=['skill4']
        skills5=['skill5']
        skills6=['skill6']
        #links
        link1=['link1']
        link2=['link2']
        link3=['link3']
        link4=['link4']
        link5=['link5']
        link6=['link6']
        response=render(request,'home2.html')    
        response.set_cookie('name', name) 
        response.set_cookie('email', email) 
        response.set_cookie('contact', contact) 
        response.set_cookie('address', address) 
        response.set_cookie('summary', summary) 
        response.set_cookie('employment1', employment1) 
        response.set_cookie('date1', date1) 
        response.set_cookie('desc1', desc1) 
        response.set_cookie('place1', place1) 

        response.set_cookie('employment2', employment2) 
        response.set_cookie('date2', date2) 
        response.set_cookie('desc2', desc2) 
        response.set_cookie('place2', place2)

        # response.set_cookie('employment3', employment3)
        # response.set_cookie('date3', date3) 
        # response.set_cookie('desc3', desc3) 
        # response.set_cookie('place3', place3)

        response.set_cookie('education1', education1)
        response.set_cookie('edate1', edate1) 
        response.set_cookie('edesc1', edesc1) 
        response.set_cookie('eplace1', eplace1)

        response.set_cookie('education2', education2) 
        response.set_cookie('edate2', edate2) 
        response.set_cookie('edesc2', edesc2) 
        response.set_cookie('eplace2', eplace2)

        response.set_cookie('education3', education3)
        response.set_cookie('edate3', edate3) 
        response.set_cookie('edesc3', edesc3) 
        response.set_cookie('eplace3', eplace3) 

        response.set_cookie('prodject1', prodject1)
        response.set_cookie('pdate1', pdate1)
        response.set_cookie('pdesc1', pdesc1)
        response.set_cookie('pplace1', pplace1)     

        response.set_cookie('prodject2', prodject2)
        response.set_cookie('pdate2', pdate2)
        response.set_cookie('pdesc2', pdesc2)
        response.set_cookie('pplace2', pplace2)

        response.set_cookie('cert1', cert1)
        response.set_cookie('cdate1', cdate1)
        response.set_cookie('cdesc1', cdesc1)
        response.set_cookie('cplace1', cplace1)    

        response.set_cookie('cert2', cert2)
        response.set_cookie('cdate2', cdate2)
        response.set_cookie('cdesc2', cdesc2)
        response.set_cookie('cplace2', cplace2) 

        response.set_cookie('skills1', skills1) 
        response.set_cookie('skills2', skills2) 
        response.set_cookie('skills3', skills3) 
        response.set_cookie('skills4', skills4) 
        response.set_cookie('skills5', skills5) 
        response.set_cookie('skills6', skills6) 

        response.set_cookie('link1', link1) 
        response.set_cookie('link2', link2) 
        response.set_cookie('link3', link3) 
        response.set_cookie('link4', link4) 
        response.set_cookie('link5', link5) 
        response.set_cookie('link6', link6) 
        return response
    else:
        print("no data")
    return render(request, 'home2.html')


class GeneratePDF2(View):
    def get(self, request, *args, **kwargs):
        name=request.COOKIES.get('name')
        email=request.COOKIES.get('email')
        contact=request.COOKIES.get('contact')
        summary=request.COOKIES.get('summary') 
        employment1=request.COOKIES.get('employment1')
        date1=request.COOKIES.get('date1')
        desc1=request.COOKIES.get('desc1')
        place1=request.COOKIES.get('place1')

        employment2=request.COOKIES.get('employment2')
        date2=request.COOKIES.get('date2')
        desc2=request.COOKIES.get('desc2')
        place2=request.COOKIES.get('place2')

        # employment3=request.COOKIES.get('employment3')
        # date3=request.COOKIES.get('date3')
        # desc3=request.COOKIES.get('desc3')
        # place3=request.COOKIES.get('place3')

        education1=request.COOKIES.get('education1')
        edate1=request.COOKIES.get('edate1')
        edesc1=request.COOKIES.get('edesc1')
        eplace1=request.COOKIES.get('eplace1')

        education2=request.COOKIES.get('education2')
        edate2=request.COOKIES.get('edate2')
        edesc2=request.COOKIES.get('edesc2')
        eplace2=request.COOKIES.get('eplace2')

        education3=request.COOKIES.get('education3')
        edate3=request.COOKIES.get('edate3')
        edesc3=request.COOKIES.get('edesc3')
        eplace3=request.COOKIES.get('eplace3')

        prodject1=request.COOKIES.get('prodject1')
        pdate1=request.COOKIES.get('pdate1')
        pdesc1=request.COOKIES.get('pdesc1')
        pplace1=request.COOKIES.get('pplace1')

        prodject2=request.COOKIES.get('prodject2')
        pdate2=request.COOKIES.get('pdate2')
        pdesc2=request.COOKIES.get('pdesc2')
        pplace2=request.COOKIES.get('pplace2')

        cert1=request.COOKIES.get('cert1')
        cdate1=request.COOKIES.get('cdate1')
        cdesc1=request.COOKIES.get('cdesc1')
        cplace1=request.COOKIES.get('cplace1')

        cert2=request.COOKIES.get('cert2')
        cdate2=request.COOKIES.get('cdate2')
        cdesc2=request.COOKIES.get('cdesc2')
        cplace2=request.COOKIES.get('cplace2')

        skills1=request.COOKIES.get('skills1')
        skills2=request.COOKIES.get('skills2')
        skills3=request.COOKIES.get('skills3')
        skills4=request.COOKIES.get('skills4')
        skills5=request.COOKIES.get('skills5')
        skills6=request.COOKIES.get('skills6')

        link1=request.COOKIES.get('link1')
        link2=request.COOKIES.get('link2')
        link3=request.COOKIES.get('link3')
        link4=request.COOKIES.get('link4')
        link5=request.COOKIES.get('link5')
        link6=request.COOKIES.get('link6')


        address=request.COOKIES.get('address') 
        template = get_template('invoice.html')
        context = {
            "name":name,
            "summary":summary,
            "email":email,
            "contact":contact,
            
            "employment1":employment1,
            "date1":date1,
            "desc1":desc1,
            "place1":place1,

            "employment2":employment2,
            "date2":date2,
            "desc2":desc2,
            "place2":place2,

            # "employment3":employment3,
            # "date3":date3,
            # "desc3":desc3,
            # "place3":place3,

            "education1":education1,
            "edate1":edate1,
            "edesc1":edesc1,
            "eplace1":eplace1,

            "education2":education2,
            "edate2":edate2,
            "edesc2":edesc2,
            "eplace2":eplace2,

            "education3":education3,
            "edate3":edate3,
            "edesc3":edesc3,
            "eplace3":eplace3,

            "address":address,

            "prodject1":prodject1,
            "pdate1":pdate1,
            "pdesc1":pdesc1,
            "pplace1":pplace1,

            "prodject2":prodject2,
            "pdate2":pdate2,
            "pdesc2":pdesc2,
            "pplace2":pplace2,

            "cert1":cert1,
            "cdate1":cdate1,
            "cdesc1":cdesc1,
            "cplace1":cplace1,

            "cert2":cert2,
            "cdate2":cdate2,
            "cdesc2":cdesc2,
            "cplace2":cplace2,

            "skills1":skills1,
            "skills2":skills2,
            "skills3":skills3,
            "skills4":skills4,
            "skills5":skills5,
            "skills6":skills6,

            "link1":link1,
            "link2":link2,
            "link3":link3,
            "link4":link4,
            "link5":link5,
            "link6":link6,



            # "invoice_id": 123,
            # "customer_name": "John Cooper",
            # "amount": 1399.99,
            # "today": "Today",
            
        }
        html = template.render(context)
        # pdf.set_font('Times')
        # pdf.add_font('Comic Sans','','/usr/share/fonts/truetype/msttcorefonts/Comic_Sans_MS.ttf', uni=True)
        # # Set font family to Comic Sans, 'U'nderlined, size 14.0 pt
        # pdf.set_font('Comic Sans','U',14.0)
        pdf = render_to_pdf('invoice2.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def index(request):
    return render(request, "index.html")
