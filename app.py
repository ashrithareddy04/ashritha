"""
Flask Web Application for CycleGAN Style Transfer
"""
from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from style_transfer import StyleTransfer
import uuid


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize style transfer
style_transfer = StyleTransfer()


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/styles')
def get_styles():
    """Get available artistic styles"""
    return jsonify({'styles': style_transfer.styles})


@app.route('/transfer', methods=['POST'])
def transfer():
    """Handle style transfer request"""
    try:
        # Check if image file is present
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check if style is provided
        style = request.form.get('style')
        if not style or style not in style_transfer.styles:
            return jsonify({'error': 'Invalid or missing style'}), 400
        
        # Validate file
        if file and allowed_file(file.filename):
            # Save uploaded file
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(input_path)
            
            # Perform style transfer
            output_image = style_transfer.transfer_style(input_path, style)
            
            # Save output image
            output_filename = f"styled_{unique_filename}"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            output_image.save(output_path)
            
            # Clean up input file
            os.remove(input_path)
            
            return jsonify({
                'success': True,
                'output_image': output_filename
            })
        else:
            return jsonify({'error': 'Invalid file type. Only PNG, JPG, and JPEG are allowed'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/result/<filename>')
def get_result(filename):
    """Serve the styled image"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'File not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
