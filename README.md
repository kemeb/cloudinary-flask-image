# Cloudinary Image Manipulation with Flask

This repository contains a Flask web application that uses Cloudinary to perform image uploading, various image transformations, tagging, and image destruction.

## Purpose

The application serves as a demonstration of how to:

- Upload images to Cloudinary with specified transformations using eager transformation and upload preset.
- Display the image tags via Amazon Rekognition Auto Tagging.
- Replace the color of an object within an image.
- Delete uploaded images from the Cloudinary account.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Cloudinary Python SDK

### Installation

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up your Cloudinary account and get API credentials, [Cloudinary Integration Documentation](https://cloudinary.com/documentation/cloudinary_integration_and_setup#integration_and_setup).
4. Create a `.env` file and add your Cloudinary credentials:
```
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```
5. In your Settings menu go to Add-ons, and subscribe to the "Rekognition Auto Tagging"
6. Create a new folder in your Media Library and name it to python (or feel free to choose a different folder name)
7. Create an upload preset in your Cloudinary account, under Settings and Upload, with the following settings:
  - Upload preset name: python
  - Add the folder name you chose in step 6.
  - Turn the "Use filename or externally defined Public" to on
  - Under Media Analysis and AI add the Amazon Rekognition Auto Tagging to the list of Categorization

### Running the Application

1. Run the Flask app: `python app.py`.
2. Access the application via your web browser at [http://localhost:5000](http://localhost:5000).

## Functionality

### Uploading Images

- Navigate to the homepage and select an image file to upload.
- The uploaded image undergoes an eager transformation with a width of 500 pixels and a crop to fill the specified dimensions.
- The uploading is done using an upload preset, where the upload folder is defined, and the Amazon Rekognition Auto Tagging is added as an add-on.
- After uploading, the image and the top 3 associated tags are displayed.

### Recoloring Images

- Utilizing Cloudinary's `gen_recolor` effect, the application enables users to change the color of a specified object in the image. The object needs to be specified within the app in the text area.
- The color change is performed alongside the existing transformations of crop and width.

### Deleting Images

- Users can delete uploaded images from their Cloudinary account by  clicking the "Delete Image" button.

