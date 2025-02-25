from PIL import Image

def encode_image(image_path, message, output_path):
    """Hide a message in an image."""
    img = Image.open(image_path)
    encoded_img = img.copy()
    
    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'  # Add a null byte as a delimiter
    data_index = 0
    
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                pixel = list(encoded_img.getpixel((x, y)))
                
                for i in range(3):  # For RGB channels
                    if data_index < len(binary_message):
                        pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])  # Set LSB
                        data_index += 1
                
                encoded_img.putpixel((x, y), tuple(pixel))
            else:
                break
    
    encoded_img.save(output_path)
    print("Message encoded and saved to", output_path)

def decode_image(image_path):
    """Extract the hidden message from the image."""
    img = Image.open(image_path)
    
    binary_message = ""
    
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            
            for i in range(3):  # For RGB channels
                binary_message += str(pixel[i] & 1)  # Get LSB
    
    # Split the binary message into bytes
    message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    # Convert binary to characters until the null byte is found
    message = ""
    for byte in message_bytes:
        if byte == '00000000':  # Stop at the null byte delimiter
            break
        message += chr(int(byte, 2))
    
    return message

# Example usage:
if __name__ == "__main__":
    original_image_path = "input_image.png"  # Path to your input image
    secret_message = "Hello, this is a secret message!"
    
    encoded_image_path = "path_to_your_encoded_image.png"  # Path to save the encoded image
    
    # Encode the message into the image
    encode_image(original_image_path, secret_message, encoded_image_path)
    
    # Decode the message from the image
    decoded_message = decode_image("path_to_your_encoded_image.png")
print("Decoded Message:", decoded_message)
