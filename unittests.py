import unittest

class Color_space_converter():
    #def rgb_to_yuv_full(rgbColor):
    def rgb_to_yuv_limited(rgbColor):
        [R, G, B] = rgbColor
        Kb = 0.114
        Kr = 0.299
        Y = Kr * R + (1.0 - Kr - Kb) * G + Kb * B
        Cb = 128.0 + 224.0 * (0.5 * ((B - Y) / (1.0 - Kb)))
        Cr = 128.0 + 224.0 * (0.5 * ((R - Y) / (1.0 - Kr)))
        Yamp = 16.0 + 219.0 * Y
        Yamp = round(Yamp)
        Cb = round(Cb)
        Cr = round(Cr)
        return [Yamp, Cb, Cr]

    #def rgb_to_yuv_limited(rgbColor):
    def rgb_to_yuv_full(rgbColor):
        [R, G, B] = rgbColor
        Kb = 0.114
        Kr = 0.299
        Y = Kr * R + (1.0 - Kr - Kb) * G + Kb * B
        Cb = 0.5 + (0.5 * ((B - Y) / (1.0 - Kb)))
        Cr = 0.5 + (0.5 * ((R - Y) / (1.0 - Kr)))
        #Y = round(255.0 * Y)
        Y = round(Y)
        Cb = round(255.0 * Cb)
        Cr = round(255.0 * Cr)
        return [Y, Cb, Cr]

class TestConversionMethods(unittest.TestCase):
    def test_black_full(self):
        rgb = [0, 0, 0]
        expected_yuv = [0, 128, 128]
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv)
    
    def test_black_limited(self):
        rgb = [0, 0, 0]
        expected_yuv = [16, 128, 128]
        actual_yuv = Color_space_converter.rgb_to_yuv_limited(rgb)
        self.assertEqual(expected_yuv, actual_yuv)

    def test_white_full(self):
        rgb = [255, 255, 255]
        expected_yuv = [255, 128, 128]    
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv) 
    
    def test_white_limited(self):
        rgb = [255, 255, 255]
        expected_yuv = [235, 128, 128]    
        actual_yuv = Color_space_converter.rgb_to_yuv_limited(rgb)
        self.assertEqual(expected_yuv, actual_yuv)

    def test_gray_full(self):
        rgb = [128, 128, 128]
        expected_yuv = [128, 128, 128]    
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv) 
    
    def test_gray_limited(self):
        rgb = [128, 128, 128]
        expected_yuv = [128, 128, 128]    
        actual_yuv = Color_space_converter.rgb_to_yuv_limited(rgb)
        self.assertEqual(expected_yuv, actual_yuv) 
    
    def test_red_full(self):
        rgb = [255, 0, 0]
        expected_yuv = [76, 84, 255]    
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv)
    
    def test_red_limited(self):
        rgb = [255, 0, 0]
        actual_yuv = Color_space_converter.rgb_to_yuv_limited(rgb)
        self.assertEqual(240, actual_yuv[2])

    def test_green_full(self):
        rgb = [0, 255, 0]
        expected_yuv = [149, 43, 21]    
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv)

    def test_blue_full(self):
        rgb = [0, 0, 255]
        expected_yuv = [29, 255, 107]    
        actual_yuv = Color_space_converter.rgb_to_yuv_full(rgb)
        self.assertEqual(expected_yuv, actual_yuv)

    def test_blue_limited(self):
        rgb = [0, 0, 255]
        actual_yuv = Color_space_converter.rgb_to_yuv_limited(rgb)
        self.assertEqual(240, actual_yuv[1])

    def test_invalid_type_r_full(self):
        rgb = ['string', 0, 0]
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_type_r_limited(self):
        rgb = ['string', 0, 0]
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_invalid_type_g_full(self):
        rgb = [0, 'string', 0]
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_type_g_limited(self):
        rgb = [0, 'string', 0]
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_invalid_type_b_full(self):
        rgb = [0, 0, 'string']
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_type_b_limited(self):
        rgb = [0, 0, 'string']
        with self.assertRaises(TypeError):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_invalid_value_r_full(self):
        rgb = [256, 0, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_value_r_limited(self):
        rgb = [256, 0, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_invalid_value_g_full(self):
        rgb = [0, 256, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_value_g_limited(self):
        rgb = [0, 256, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_invalid_value_b_full(self):
        rgb = [0, 0, 256]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_invalid_value_b_limited(self):
        rgb = [0, 0, 256]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_negative_value_r_full(self):
        rgb = [-1, 0, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_negative_value_r_limited(self):
        rgb = [-1, 0, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_negative_value_g_full(self):
        rgb = [0, -1, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_negative_value_g_limited(self):
        rgb = [0, -1, 0]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

    def test_negative_value_b_full(self):
        rgb = [0, 0, -1]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_full(rgb)
    
    def test_negative_value_b_limited(self):
        rgb = [0, 0, -1]
        with self.assertRaises(Exception):
            Color_space_converter.rgb_to_yuv_limited(rgb)

if __name__ == '__main__':
    unittest.main()