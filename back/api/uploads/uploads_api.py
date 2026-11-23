import os
from flask import Blueprint, request, send_file, abort

uploads_api = Blueprint('uploads', __name__)

# Définition du dossier d'uploads
UPLOAD_FOLDER = os.path.abspath('uploads')
@uploads_api.route('/')
def get_upload():

   filename = request.args.get("name")
   if not filename:
      abort(400, description="Filename is required")

   # Sécursiation : Construction du chemin absolu cible
   safe_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, filename))

   #Vérification que le chemin cible est bien dans le dossier d'uploads
   if not safe_path.startswith(UPLOAD_FOLDER + os.sep) and safe_path != UPLOAD_FOLDER:
      abort(403, description="Access denied")

   # Vérification que le fichier existe réellement
   if not os.path.isfile(safe_path) or not os.path.isfile(safe_path):
      abort(404, description="File not found")
   
   return send_file(safe_path)
