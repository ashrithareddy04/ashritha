"""
Simple unit tests for CycleGAN Style Transfer application
"""
import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestCycleGANModel(unittest.TestCase):
    """Test CycleGAN model architecture"""
    
    def test_imports(self):
        """Test that all modules can be imported"""
        try:
            import cyclegan_model
            import style_transfer
            import app
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")
    
    def test_generator_class_exists(self):
        """Test that Generator class exists"""
        from cyclegan_model import Generator
        self.assertTrue(callable(Generator))
    
    def test_residual_block_class_exists(self):
        """Test that ResidualBlock class exists"""
        from cyclegan_model import ResidualBlock
        self.assertTrue(callable(ResidualBlock))


class TestStyleTransfer(unittest.TestCase):
    """Test style transfer functionality"""
    
    def test_style_transfer_class_exists(self):
        """Test that StyleTransfer class exists"""
        from style_transfer import StyleTransfer
        self.assertTrue(callable(StyleTransfer))
    
    def test_available_styles(self):
        """Test that styles are defined"""
        from style_transfer import StyleTransfer
        st = StyleTransfer()
        self.assertEqual(st.styles, ['monet', 'vangogh', 'picasso'])


class TestFlaskApp(unittest.TestCase):
    """Test Flask application"""
    
    def test_flask_app_exists(self):
        """Test that Flask app is defined"""
        from app import app
        self.assertIsNotNone(app)
    
    def test_allowed_extensions(self):
        """Test allowed file extensions"""
        from app import allowed_file
        self.assertTrue(allowed_file('test.jpg'))
        self.assertTrue(allowed_file('test.jpeg'))
        self.assertTrue(allowed_file('test.png'))
        self.assertFalse(allowed_file('test.gif'))
        self.assertFalse(allowed_file('test.txt'))
        self.assertFalse(allowed_file('test'))


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
