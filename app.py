from flask import Flask, render_template, request
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()
app = Flask(__name__)
config = cloudinary.config(secure=True)

# Uploading the image to Cloudinary with eager transformation and upload preset
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file:
            response=cloudinary.uploader.upload(file, 
                                 upload_preset = "python",
                                 unique_filename = True, 
                                 overwrite=True,
                                 eager=[{"width": 500, "crop": "fill"}])

            image_url = response['eager'][0]['secure_url']
            tags = response['info']['categorization']['aws_rek_tagging']['data'][:3]

            return render_template('index.html', image_url=image_url, tags=tags)

    return render_template('index.html')

# Replace the color of an object on the image
@app.route('/recolor', methods=['POST'])
def recolor():
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        public_id = "/".join(image_url.split('/')[-2:])[:-4]
        color = request.form['color']
        color_for_url = color[1:]
        chosen_object = request.form['object']
        transformation = f"gen_recolor:prompt_{chosen_object};to-color_{color_for_url}/c_fill,w_500"
        
        recolor_url = cloudinary.utils.cloudinary_url(public_id, effect=transformation)[0]
        
        response = cloudinary.api.resource(public_id, tags=True)
        tags = response['info']['categorization']['aws_rek_tagging']['data'][:3]

        return render_template ('index.html', recolor_url=recolor_url, image_url=image_url, tags=tags)

# Deleting the uploaded image from the Cloudinary account
@app.route('/delete', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        public_id = "/".join(image_url.split('/')[-2:])[:-4]
        result = cloudinary.uploader.destroy(public_id)
        return render_template ('index.html')
    
    return "Something went wrong, not able to find the image"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


