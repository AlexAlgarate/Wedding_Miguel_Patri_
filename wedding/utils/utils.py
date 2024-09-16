import os
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()

menu_data: Dict[str, str] = {
    "Confirmación": "/#confirmation_section",
    "Dirección": "/#celebration_section",
    "Autobús": "/#bus_service_section",
    "Contacto": "/#contact_section",
    "Fotos": "/#photos_section",
}


# Web descriptions
title_main = "Invitación de boda de Patri y Miguel 30/05/2025"
description_main = """
    ¡Quedas invitada a nuestra boda! ¡Acompáñanos en este día mágico e inolvidable!
"""


# Header texts
title_header = "¡Nos casamos!"
wedding_date: List[str] = [
    "30",
    "mayo",
    "2025",
]
wedding_hour = "12:00"


# Image descriptions
alt_image_celebration = "Foto de la entrada de La Agripina."
alt_image_partners = "Foto principal de los novios."
label_image_celebration = "Pincha en la imagen para visitar el sitio web de La Agripina"
alt_image_leafs = "Foto de unas hojas amarillas."
alt_image_lavender = "Foto de unas ramas de lavanda con sus hojas"

# Icons desriptions
alt_icon_confirmation = "Icono de un sobre morado"
alt_icon_celebration = "Icono de un pórtico con velo morado"
alt_icon_bus = "Icono de un bus morado"
alt_icon_ubication = "Icono de ubicación morado"
alt_icon_contact = "Icono de un teléfono y un mensaje de texto morado"
alt_icon_whatsapp = "Icono de Whatsapp morado"
alt_icon_camera = "Icono de una cámara de fotos morada"


# SECTION TEXTS
# Countdown texts
countdown_title: str = "¡Cuenta atrás!"
countdown_text = "¡Ven a acompañarnos en el día más feliz de nuestras vidas!"
countdown_button = "Guardar fecha"

# Confirmation
confirmation_title = "Confirmación"
confirmation_button = "Confirmar asistencia"
confirmation_text = """Seguro que tienes muchas ganas de compartir este día con nosotros.\n
    ¿Confirmas tu asistencia?"""


# Celebration
celebration_title = "¿Dónde nos casamos"
celebration_button = "Abrir en Google Maps"
celebration_text = "Hemos elegido un sitio muy especial para celebrar este gran día."
wedding_place = "Finca Montealvar"
wedding_address_street = "Yebes"
wedding_address_province = "Guadalajara"


# Bus
but_title = "Servicio de autobús"
bus_text = """
    Para facilitar la asistencia habrá un servicio de autobuses tanto a la ida como a la vuelta.
"""
bus_origin_title = "Ida a la ceremonia"
bur_origin_address = "El Carpe"
hotel_name = "Hotel Pax"
hotel_address = "C/ Mayor"
origin_bus_schedule = "12:00"

bus_destination_title = "Regreso a casa"

destination_address = "Cjón. los Romanos, 1 (Punta Umbría, Huelva)"


# Photo Album
title_photo = "Álbum de Fotos"
google_photo_text_one = "¿Quieres recordar este día para siempre?"
google_photo_text_two = """
    Comparte tus fotos de la boda subiéndolas al albúm compartido de Google Fotos.
"""
google_photo_button = "Abrir álbum"


# Gift
gift_title = "Lista de regalos"
gift_text = """
    Vuestra presencia es nuestro mayor regalo,
    pero si nos queréis hacer una aportacion para ayudarnos a celebrar,
    este es nuestro número de cuenta
"""
account_number_text = os.getenv("ACCOUNT_NUMBER")


# Contact
contact_title = "Contacta con nosotros"
contact_bride = dict(
    name="Patri",
    email=os.getenv("PATRI_EMAIL"),
    phone_number=os.getenv("PATRI_PHONE"),
)
contact_groom = dict(
    name="Miguel",
    email=os.getenv("MIGUEL_EMAIL"),
    phone_number=os.getenv("MIGUEL_PHONE"),
)
contact_text_whatsapp = """
Ponte en contacto con nosotros a través de Whatsapp haciendo click directamente en el botón
"""
contact_text_email = "Si te es más cómodo, puedes mandarnos un correo a:"


# Bottom web message
bottom_text = "Te esperamos"


OPTIONS_CONFIRMATION = ["Sí, ¡por supuesto!", "No puedo, lo siento :("]
OPTIONS_CONFIRMATION_DICT = {
    "Yes": "Sí, ¡por supuesto!",
    "No": "No puedo, lo siento :(",
}
OPTIONS_COMPANIONN_DICT = {
    "Yes_companion": "Sí, voy con acompañantes",
    "No_companion": "No, solo yo",
}

FOOD_ALLERGIES = [
    "No",
    "Pescado",
    "Frutos Secos",
    "Soja",
    "Mariscos",
    "Lácteos",
    "Otros",
]

personal_info_dict: List[Dict[str, str]] = [
    {
        "name": "first_name",
        "placeholder": "Nombre...",
        "type": "text",
    },
    {
        "name": "last_name",
        "placeholder": "Apellidos...",
        "type": "text",
    },
    {
        "name": "phone_number",
        "placeholder": "Teléfono...",
        "type": "tel",
    },
    # {
    #     "name": "email",
    #     "placeholder": "Email...",
    #     "type": "email",
    # },
]

number_adults = ["1", "2", "3", "4", "5", "Otros"]
number_kids = ["0", "1", "2", "3", "4", "Otros"]

supabase_name_columns = [
    "confirm_invitation",
    "first_name",
    "last_name",
    "phone_number",
    "wedding_companion",
    "number_adults",
    "number_kids",
    "name_companion",
    "food_allergies",
    "songs",
    "created_at",
]

supabase_table_name = "wedding_invitations"
toast_accepts_invitation = (
    "¡Genial! ¡Te esperamos en el día más importante de nuestras vidas"
)
toast_decline_invitation = "¿Estás segura? Si cambias de idea háznoslo saber por favor."
