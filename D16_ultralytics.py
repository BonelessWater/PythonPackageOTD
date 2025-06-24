'''
Day 16, June 23rd 2025: 

Welcome to YOLOv11!

You Only Look Once, but when you do, you see everything. YOLOv11 
represents the cutting edge of real-time object detection, capable 
of identifying and localizing multiple objects in images and videos 
with incredible speed and accuracy. From autonomous vehicles to 
security systems, YOLO powers the eyes of AI.
'''

from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path
import time

class YOLODetector:
    def __init__(self, model_size='n'):
        """
        Initialize YOLO detector
        model_size: 'n' (nano), 's' (small), 'm' (medium), 'l' (large), 'x' (extra large)
        """
        self.model = YOLO(f'yolo11{model_size}.pt')  # Auto-downloads on first use
        self.class_names = self.model.names
        
    def detect_image(self, image_path, conf_threshold=0.5, save_result=True):
        """Detect objects in a single image"""
        results = self.model(image_path, conf=conf_threshold)
        
        if save_result:
            # Save annotated image
            annotated = results[0].plot()
            output_path = f"detected_{Path(image_path).name}"
            cv2.imwrite(output_path, annotated)
            print(f"Annotated image saved as: {output_path}")
        
        # Print detection results
        for r in results:
            boxes = r.boxes
            if boxes is not None:
                for box in boxes:
                    cls_id = int(box.cls[0])
                    conf = float(box.conf[0])
                    coords = box.xyxy[0].tolist()
                    
                    print(f"Detected: {self.class_names[cls_id]} "
                          f"(confidence: {conf:.2f}) "
                          f"at [{coords[0]:.0f}, {coords[1]:.0f}, "
                          f"{coords[2]:.0f}, {coords[3]:.0f}]")
        
        return results
    
    def detect_video(self, video_path, conf_threshold=0.5, save_output=True):
        """Detect objects in video"""
        cap = cv2.VideoCapture(video_path)
        
        if save_output:
            # Setup video writer
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            output_path = f"detected_{Path(video_path).stem}.mp4"
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        frame_count = 0
        total_time = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            start_time = time.time()
            results = self.model(frame, conf=conf_threshold)
            inference_time = time.time() - start_time
            
            # Annotate frame
            annotated_frame = results[0].plot()
            
            # Add FPS info
            fps_text = f"FPS: {1/inference_time:.1f}"
            cv2.putText(annotated_frame, fps_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            if save_output:
                out.write(annotated_frame)
            
            frame_count += 1
            total_time += inference_time
            
            # Optional: Display real-time (comment out for headless)
            # cv2.imshow('YOLOv11 Detection', annotated_frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        
        cap.release()
        if save_output:
            out.release()
            print(f"Processed video saved as: {output_path}")
        
        avg_fps = frame_count / total_time
        print(f"Average FPS: {avg_fps:.1f}")
        
        cv2.destroyAllWindows()
    
    def detect_webcam(self, conf_threshold=0.5):
        """Real-time detection from webcam"""
        cap = cv2.VideoCapture(0)  # Use default camera
        
        print("Starting webcam detection. Press 'q' to quit.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            start_time = time.time()
            results = self.model(frame, conf=conf_threshold)
            inference_time = time.time() - start_time
            
            # Annotate frame
            annotated_frame = results[0].plot()
            
            # Add performance info
            fps = 1 / inference_time
            cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Count detections
            detection_count = len(results[0].boxes) if results[0].boxes else 0
            cv2.putText(annotated_frame, f"Objects: {detection_count}", (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('YOLOv11 Webcam Detection', annotated_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    def train_custom_model(self, dataset_yaml, epochs=100, img_size=640):
        """Train YOLOv11 on custom dataset"""
        print(f"Training custom YOLOv11 model...")
        print(f"Dataset: {dataset_yaml}")
        print(f"Epochs: {epochs}, Image size: {img_size}")
        
        # Train the model
        results = self.model.train(
            data=dataset_yaml,
            epochs=epochs,
            imgsz=img_size,
            save=True,
            plots=True
        )
        
        print("Training completed!")
        return results
    
    def export_model(self, format='onnx'):
        """Export model to different formats"""
        supported_formats = ['onnx', 'torchscript', 'tflite', 'edgetpu', 'tfjs']
        
        if format not in supported_formats:
            print(f"Unsupported format. Choose from: {supported_formats}")
            return
        
        print(f"Exporting model to {format.upper()}...")
        self.model.export(format=format)
        print(f"Model exported successfully!")

def demo_yolo():
    """Demonstrate YOLOv11 capabilities"""
    print("🚀 YOLOv11 Object Detection Demo")
    print("=" * 40)
    
    # Initialize detector (nano model for speed)
    detector = YOLODetector('n')
    
    # Create a sample image for testing
    print("\n📸 Creating sample test image...")
    sample_image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    
    # Add some geometric shapes that might be detected as objects
    cv2.rectangle(sample_image, (100, 100), (200, 200), (255, 0, 0), -1)
    cv2.circle(sample_image, (400, 300), 50, (0, 255, 0), -1)
    
    cv2.imwrite('sample_image.jpg', sample_image)
    print("Sample image created: sample_image.jpg")
    
    # Detect objects in the sample image
    print("\n🔍 Detecting objects in sample image...")
    results = detector.detect_image('sample_image.jpg')
    
    # Show model info
    print(f"\n📊 Model Information:")
    print(f"Model type: YOLOv11n")
    print(f"Classes: {len(detector.class_names)}")
    print(f"Sample classes: {list(detector.class_names.values())[:10]}")
    
    # Performance benchmark
    print(f"\n⚡ Performance Benchmark:")
    start_time = time.time()
    for _ in range(10):
        detector.model('sample_image.jpg', verbose=False)
    avg_time = (time.time() - start_time) / 10
    print(f"Average inference time: {avg_time*1000:.1f}ms")
    print(f"Theoretical max FPS: {1/avg_time:.1f}")
    
    print(f"\n✅ Demo completed! Check 'detected_sample_image.jpg' for results.")

if __name__ == "__main__":
    # Run the demo
    #demo_yolo()
    
    # Uncomment below for specific use cases:
    
    detector = YOLODetector('s')  # Small model for balance of speed/accuracy
    
    # Detect in your own image
    #detector.detect_image('your_image.jpg')
    
    # Detect in video
    #detector.detect_video('your_video.mp4')
    
    # Real-time webcam detection
    detector.detect_webcam()
    
    # Train on custom dataset (requires dataset.yaml)
    # detector.train_custom_model('path/to/dataset.yaml', epochs=50)
    
    # Export for deployment
    # detector.export_model('onnx')  # For production deployment