from django.shortcuts import render
import io, os
from pathlib import Path
from rembg import remove
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
import requests

def upload_image(request):
    file_url = None
    full_fs_path = None
    error = None


    if request.method == "POST" and request.FILES.get("image"):
        try:
            # open uploaded image
            img = Image.open(request.FILES["image"]).convert("RGBA")

            # remove background
            output = remove(img)

            # save to Django media
            buffer = io.BytesIO()
            output.save(buffer, format="PNG")
            filename = f"no_bg_{request.FILES['image'].name.rsplit('.',1)[0]}.png"
            saved_path = default_storage.save(
                os.path.join("no_bg", filename),
                ContentFile(buffer.getvalue())
            )

            # FIXED: Use MEDIA_URL for template display (URL path)
            file_url = settings.MEDIA_URL + saved_path.replace('\\', '/') if settings.MEDIA_URL else '/' + saved_path.replace('\\', '/')
            
            # Build filesystem path for logging/display
            full_fs_path = Path(settings.MEDIA_ROOT) / saved_path

            # Debug prints
            print(f'File URL for template: "{file_url}"')
            print(f'MEDIA_URL setting: "{settings.MEDIA_URL}"')
            print(f'MEDIA_ROOT setting: "{settings.MEDIA_ROOT}"')
            print(f'Filesystem path: {full_fs_path}')
            print(f'Raw saved_path: {saved_path}')
            
        except Exception as e:
            error = str(e)
            print(f'Error processing image: {error}')

    return render(request, "upload.html", {
        "file_url": file_url,        # for <img src> - this is now a proper URL
        "fs_path": full_fs_path,     # filesystem path for display
        "error": error,
    })
'''
import io, os, requests
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def upload_image(request):
    file_url = None
    full_fs_path = None
    error = None

    if request.method == "POST" and request.FILES.get("image"):
        try:
            # 1) Save the original upload to MEDIA_ROOT/uploads/
            upload_dir = "uploads"
            orig_file = request.FILES["image"]
            saved_orig = default_storage.save(
                os.path.join(upload_dir, orig_file.name),
                ContentFile(orig_file.read())
            )
            orig_path = Path(settings.MEDIA_ROOT) / saved_orig
            print(f"Saved original: {orig_path}")

            # 2) Call remove.bg API
            api_key = os.getenv("REMOVE_BG_API_KEY", "")
            with open(orig_path, "rb") as image_file:
                response = requests.post(
                    "https://api.remove.bg/v1.0/removebg",
                    files={"image_file": image_file},
                    data={"size": "auto"},
                    headers={"X-Api-Key": api_key},
                )

            if response.status_code != requests.codes.ok:
                raise RuntimeError(f"API error {response.status_code}: {response.text}")

            # 3) Save the background‑removed result to MEDIA_ROOT/no_bg/
            no_bg_dir = "no_bg"
            base, _ = os.path.splitext(orig_file.name)
            out_name = f"{base}_no_bg.png"
            saved_out = default_storage.save(
                os.path.join(no_bg_dir, out_name),
                ContentFile(response.content)
            )

            # 4) Build URL for template and filesystem path for logging
            file_url = settings.MEDIA_URL.rstrip("/") + "/" + saved_out.replace("\\", "/")
            full_fs_path = Path(settings.MEDIA_ROOT) / saved_out

            # Debug logs
            print(f'File URL for template: "{file_url}"')
            print(f'MEDIA_ROOT: "{settings.MEDIA_ROOT}"')
            print(f'Filesystem path: {full_fs_path}')

        except Exception as e:
            error = str(e)
            print(f'Error processing image: {error}')

    return render(request, "upload.html", {
        "file_url": file_url,    # e.g. "/media/no_bg/myfile_no_bg.png"
        "fs_path": full_fs_path, # for display/logging only
        "error": error,
    })
'''

   