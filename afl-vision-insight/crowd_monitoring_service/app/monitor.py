import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

class CrowdMonitor:
    def __init__(self):
        self.max_resolution = (4000, 4000)  # Arbitrary upper limit to avoid OOM

    def process_image(self, input_path: str, output_path: str) -> dict:
        try:
            # Load image
            image = cv2.imread(input_path)
            if image is None:
                return {"status": "error", "message": "Invalid image format.", "code": 400}

            height, width, _ = image.shape
            if height > self.max_resolution[0] or width > self.max_resolution[1]:
                return {
                    "status": "error",
                    "message": "Image resolution too high. Please use HD or lower.",
                    "code": 413
                }

            # Simulate heatmap generation
            heatmap = self._generate_dummy_heatmap(height, width)
            self._overlay_heatmap(image, heatmap, output_path)

            # Simulate crowd estimation
            crowd_estimates = self._mock_crowd_estimates()

            return {
                "status": "success",
                "message": "Crowd analysis completed.",
                "heatmap_path": output_path,
                "crowd_estimates": crowd_estimates
            }

        except Exception as e:
            return {"status": "error", "message": f"Internal error: {str(e)}", "code": 500}

    def _generate_dummy_heatmap(self, height, width):
        # Create a random density matrix
        return np.random.rand(height, width)

    def _overlay_heatmap(self, image, heatmap, output_path):
        # Normalize heatmap and apply colormap
        heatmap_normalized = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
        heatmap_colored = cv2.applyColorMap(heatmap_normalized.astype(np.uint8), cv2.COLORMAP_JET)

        # Blend heatmap with original image
        blended = cv2.addWeighted(image, 0.6, heatmap_colored, 0.4, 0)
        cv2.imwrite(output_path, blended)

    def _mock_crowd_estimates(self):
        # Dummy stage-wise crowd count
        return {
            "Stage A": np.random.randint(300, 500),
            "Stage B": np.random.randint(400, 600),
            "Stage C": np.random.randint(200, 400)
        }
