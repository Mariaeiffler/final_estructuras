from datetime import *
from FuncionesFinal import *
from unidecode import unidecode

class Proyecto():
    def __init__(self,proyecto_id,proyecto_fuente,titulo,fecha_inicio,fecha_finalizacion,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director,anio,disciplina):
        self.proyecto_id = proyecto_id
        self.proyecto_fuente = proyecto_fuente
        self.titulo = unidecode(titulo)
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.resumen = unidecode(resumen)
        self.moneda_id = moneda_id
        self.monto_total_solicitado = monto_total_solicitado
        self.monto_total_adjudicado = monto_total_adjudicado
        self.monto_financiado_solicitado = monto_financiado_solicitado
        self.monto_financiado_adjudicado = monto_financiado_adjudicado
        self.tipo_proyecto_id = tipo_proyecto_id
        self.codigo_identificacion = codigo_identificacion
        self.palabras_clave = unidecode(palabras_clave)
        self.estado_id = estado_id
        self.fondo_anpcyt = fondo_anpcyt
        self.cantidad_miembros_F = cantidad_miembros_F
        self.cantidad_miembros_M = cantidad_miembros_M
        self.sexo_director = sexo_director
        self.anio = anio
        self.disciplina = disciplina
 
    def __str__(self):
        return ('{} - {}'.format(convertirfecha_datetime(self.fecha_inicio).strftime('%d/%m/%Y'),(self.titulo)))