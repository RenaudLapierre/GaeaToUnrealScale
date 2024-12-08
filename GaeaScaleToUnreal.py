import tkinter as tk
from tkinter import ttk

class ScaleConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gaea to Unreal Engine Scale Converter")

        self.create_widgets()

    def create_widgets(self):
        # Gaea Scale
        self.gaea_scale_label = ttk.Label(self.root, text="Gaea Scale (m):")
        self.gaea_scale_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.gaea_scale_var = tk.DoubleVar(value=5000.0)
        self.gaea_scale_entry = ttk.Entry(self.root, textvariable=self.gaea_scale_var)
        self.gaea_scale_entry.grid(row=0, column=1, padx=10, pady=5)

        # Height Map Resolution
        self.height_map_resolution_label = ttk.Label(self.root, text="Height Map Resolution:")
        self.height_map_resolution_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.height_map_resolution_var = tk.IntVar(value=4033)
        self.height_map_resolution_entry = ttk.Entry(self.root, textvariable=self.height_map_resolution_var)
        self.height_map_resolution_entry.grid(row=1, column=1, padx=10, pady=5)

        # Gaea Height
        self.gaea_height_label = ttk.Label(self.root, text="Gaea Height (m):")
        self.gaea_height_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.gaea_height_var = tk.DoubleVar(value=2000.0)
        self.gaea_height_entry = ttk.Entry(self.root, textvariable=self.gaea_height_var)
        self.gaea_height_entry.grid(row=2, column=1, padx=10, pady=5)

        # Gaea Clamped Scale
        self.gaea_clamped_scale_label = ttk.Label(self.root, text="Gaea Clamped Scale (m):")
        self.gaea_clamped_scale_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.gaea_clamped_scale_var = tk.DoubleVar(value=500.0)
        self.gaea_clamped_scale_entry = ttk.Entry(self.root, textvariable=self.gaea_clamped_scale_var)
        self.gaea_clamped_scale_entry.grid(row=3, column=1, padx=10, pady=5)

        # Gaea Height-Scale Ratio
        self.gaea_height_scale_ratio_label = ttk.Label(self.root, text="Gaea Height-Scale Ratio:")
        self.gaea_height_scale_ratio_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.gaea_height_scale_ratio_var = tk.DoubleVar(value=0.40)
        self.gaea_height_scale_ratio_entry = ttk.Entry(self.root, textvariable=self.gaea_height_scale_ratio_var)
        self.gaea_height_scale_ratio_entry.grid(row=4, column=1, padx=10, pady=5)

        # Calculate Button
        self.calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate_scale)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Result for Unreal X/Y Scale
        self.result_xy_label = ttk.Label(self.root, text="Unreal Engine X/Y Scale:")
        self.result_xy_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.result_xy_var = tk.StringVar(value="")
        self.result_xy_entry = ttk.Entry(self.root, textvariable=self.result_xy_var, state='readonly')
        self.result_xy_entry.grid(row=6, column=1, padx=10, pady=5)

        # Result for Unreal Z Scale
        self.result_z_label = ttk.Label(self.root, text="Unreal Engine Z Scale:")
        self.result_z_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.result_z_var = tk.StringVar(value="")
        self.result_z_entry = ttk.Entry(self.root, textvariable=self.result_z_var, state='readonly')
        self.result_z_entry.grid(row=7, column=1, padx=10, pady=5)

    def calculate_scale(self):
        gaea_scale = self.gaea_scale_var.get()
        height_map_resolution = self.height_map_resolution_var.get()
        gaea_height = self.gaea_height_var.get()
        gaea_clamped_scale = self.gaea_clamped_scale_var.get()
        gaea_height_scale_ratio = self.gaea_height_scale_ratio_var.get()

        # Calculate Unreal X/Y Scale
        unreal_scale_xy = (gaea_scale * 100) / height_map_resolution
        self.result_xy_var.set(f"{unreal_scale_xy:.6f}")

        # Calculate Unreal Z Scale
        value1 = gaea_clamped_scale / gaea_height_scale_ratio
        value2 = gaea_height / gaea_clamped_scale
        value3 = value1 * value2
        unreal_scale_z = value3 * 100 * 0.001953125
        self.result_z_var.set(f"{unreal_scale_z:.6f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScaleConverterApp(root)
    root.mainloop()
