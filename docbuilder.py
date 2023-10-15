import docxtpl
import jinja2
import contextbuilder
import pathlib
import numpy



def create_tpl_instance(template):
    tpl = docxtpl.DocxTemplate(template)
    return tpl


def builddocx(tpl, context, filename, gde, hhj):
    
    def ec(number):
        
        if type(number) == int or type(number) == float or type(number) == numpy.int64 or type(number) == numpy.int32 or numpy.float64 or numpy.float32 :
            eurofied = "{:,.2f}".format(number).replace(",", "x").replace(".", ",").replace("x", ".")
        elif number == None:
            eurofied = "LEERE VARIABLE"
        
        else:
            eurofied = number
        
        return eurofied

    def ecp(number):
        
        if type(number) == int or type(number) == numpy.int64 or type(number) == numpy.int32:
            euro = "{:,}".format(number).replace(",", ".")
        elif number == None:
            euro = "LEERE VARIABLE"
        else:
            euro = number
        return euro


    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."), 
                             trim_blocks=True,
                             lstrip_blocks=True)
    env.filters["ec"] = ec
    #env.filters["ecp"] = ec
    env.filters["ecp"] = ecp
    
    gdepfad = pathlib.Path.cwd() /f"Ausgabe/{gde}"
    hhpfad = pathlib.Path.cwd() /f"Ausgabe/{gde}/{hhj}"
    print(hhpfad)
    print(context)

    
    tpl.render(context, env)

    if not pathlib.Path(gdepfad).exists():
        print(f"gdefad wird angelegt: {gdepfad}")
        pathlib.Path.mkdir(gdepfad)

    
    if not pathlib.Path(hhpfad).exists():
        print(f"hhpfad wird angelegt: {hhpfad}")
        pathlib.Path.mkdir(hhpfad)

    tpl.save(pathlib.Path(f"{hhpfad}/{gde}-{hhj}-{filename}.docx"))