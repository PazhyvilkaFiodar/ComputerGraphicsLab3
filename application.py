import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import transform
import numpy as np
from PIL import Image, ImageTk


class Application:
    def __init__(self):
        self._window = tk.Tk()
        self._window.geometry("1280x700")
        self._window.resizable(False, False)

        self._button_choose_image = tk.Button(self._window, text="Choose image", command=self._choose_image)
        self._button_choose_image.pack(side=tk.TOP)
        
        self._image = np.array([])
        self._photo = np.array([])
        self._transformed_photo = np.array([])

        self._label_before = tk.Label(self._window)
        self._label_before.pack(side=tk.LEFT)

        self._label_after = tk.Label(self._window)
        self._label_after.pack(side=tk.RIGHT)

        self._add_constant_button = tk.Button(self._window, text="Add constant", command=self._add_constant_click)
        self._make_negative_button = tk.Button(self._window, text="Make negative", command=self._make_negative_click)
        self._multiply_by_constant_button = tk.Button(self._window, text="Multiply by constant", command=self._multiply_by_constant_click)
        self._power_button = tk.Button(self._window, text="Power", command=self._power_click)
        self._logarithm_button = tk.Button(self._window, text="Logarithm", command=self._logarithm_click)
        self._linear_contrast_button = tk.Button(self._window, text="Linear contrast", command=self._linear_contrast_click)
        self._local_otsu_thresholding_button = tk.Button(self._window, text="Local Otsu thresholding", command=self._local_otsu_thresholding_click)
        self._local_triangle_thresholding_button = tk.Button(self._window, text="Local triangle thresholding", command=self._local_triangle_thresholding_click)
        self._mean_adaptive_thresholding_button = tk.Button(self._window, text="Mean adaptive thresholding", command=self._mean_adaptive_thresholding_click)
        self._gaussian_adaptive_thresholding_button = tk.Button(self._window, text="Gaussian adaptive thresholding", command=self._gaussian_adaptive_thresholding_click)

    def run(self) -> None:
        self._window.mainloop()


    def _choose_image(self) -> None:
        filepath = filedialog.askopenfilename()
        self._image = transform.open_image(filepath)
        self._photo = ImageTk.PhotoImage(Image.fromarray(self._image))
        self._label_before.config(width=500, height=300, image=self._photo)
        self._add_constant_button.place(x=50, y=30)
        self._make_negative_button.place(x=175, y=30)
        self._multiply_by_constant_button.place(x=310, y=30)
        self._power_button.place(x=480, y=30)
        self._logarithm_button.place(x=570, y=30)
        self._linear_contrast_button.place(x=680, y=30)
        self._local_otsu_thresholding_button.place(x=820, y=30)
        self._local_triangle_thresholding_button.place(x=1020, y=30)
        self._mean_adaptive_thresholding_button.place(x=425, y=60)
        self._gaussian_adaptive_thresholding_button.place(x=650, y=60)
        
    def _add_constant_click(self) -> None:
        constant = simpledialog.askinteger("Constant", "Enter constant")
        transformed_image = transform.add_constant(self._image, constant)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)
    
    def _make_negative_click(self) -> None:
        transformed_image = transform.make_negative(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _multiply_by_constant_click(self) -> None:
        constant = simpledialog.askfloat("Constant", "Enter constant")
        transformed_image = transform.multiply_by_constant(self._image, constant)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _power_click(self) -> None:
        power = simpledialog.askfloat("Constant", "Enter constant")
        transformed_image = transform.power(self._image, power)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)
    
    def _logarithm_click(self) -> None:
        transformed_image = transform.logarithm(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _linear_contrast_click(self) -> None:
        transformed_image = transform.linear_contrast(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _local_otsu_thresholding_click(self) -> None:
        transformed_image = transform.local_otsu_thresholding(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _local_triangle_thresholding_click(self) -> None:
        transformed_image = transform.local_triangle_thresholding(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _mean_adaptive_thresholding_click(self) -> None:
        transformed_image = transform.mean_adaptive_thresholding(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)

    def _gaussian_adaptive_thresholding_click(self) -> None:
        transformed_image = transform.gaussian_adaptive_thresholding(self._image)
        self._transformed_photo = ImageTk.PhotoImage(Image.fromarray(transformed_image))
        self._label_after.config(width=500, height=300, image=self._transformed_photo)
