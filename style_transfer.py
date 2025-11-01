"""
Style Transfer Processor using CycleGAN
"""
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import os
from cyclegan_model import Generator


class StyleTransfer:
    """Handles style transfer operations"""
    
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.generators = {}
        self.styles = ['monet', 'vangogh', 'picasso']
        
        # Image transformation pipeline
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])
        
        self.denormalize = transforms.Normalize(mean=[-1, -1, -1], std=[2, 2, 2])
        
    def load_generator(self, style):
        """Load a pre-trained generator for a specific style"""
        if style not in self.generators:
            generator = Generator().to(self.device)
            generator.eval()
            
            # In a production environment, you would load pre-trained weights here:
            # model_path = f'models/generator_{style}.pth'
            # if os.path.exists(model_path):
            #     generator.load_state_dict(torch.load(model_path, map_location=self.device))
            
            self.generators[style] = generator
        
        return self.generators[style]
    
    def preprocess_image(self, image_path):
        """Load and preprocess an image"""
        image = Image.open(image_path).convert('RGB')
        image_tensor = self.transform(image).unsqueeze(0).to(self.device)
        return image_tensor
    
    def postprocess_image(self, tensor):
        """Convert tensor back to PIL Image"""
        tensor = self.denormalize(tensor.squeeze(0).cpu())
        tensor = torch.clamp(tensor, 0, 1)
        image = transforms.ToPILImage()(tensor)
        return image
    
    def transfer_style(self, image_path, style):
        """Apply style transfer to an image"""
        if style not in self.styles:
            raise ValueError(f"Style must be one of {self.styles}")
        
        # Load generator
        generator = self.load_generator(style)
        
        # Preprocess image
        input_tensor = self.preprocess_image(image_path)
        
        # Apply style transfer
        with torch.no_grad():
            output_tensor = generator(input_tensor)
        
        # Postprocess result
        output_image = self.postprocess_image(output_tensor)
        
        return output_image
