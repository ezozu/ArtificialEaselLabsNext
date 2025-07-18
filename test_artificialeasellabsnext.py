# test_artificialeasellabsnext.py
"""
Tests for ArtificialEaselLabsNext module.
"""

import unittest
from artificialeasellabsnext import ArtificialEaselLabsNext

class TestArtificialEaselLabsNext(unittest.TestCase):
    """Test cases for ArtificialEaselLabsNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselLabsNext()
        self.assertIsInstance(instance, ArtificialEaselLabsNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselLabsNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
