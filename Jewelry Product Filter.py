import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QVBoxLayout, QScrollArea, QFrame, QGridLayout, QSizePolicy, QHBoxLayout, QDialog, QGraphicsView, QGraphicsScene
)
from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtCore import Qt, QSize

# Veri setini yükleme
df = pd.read_csv('products.csv')

class JewelryFilterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Jewelry Product Filter')
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowIcon(QIcon('icons/app_icon.png'))
        self.data = df
        self.initUI()
    
    def initUI(self):
        # Stil ayarları
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
                color: #333;
            }
            QLabel {
                font-weight: bold;
            }
            QLineEdit, QComboBox {
                background-color: #fff;
                color: #333;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #007BFF;
            }
            QPushButton {
                background-color: #007BFF;
                color: #fff;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
            }
            QPushButton#ResetButton {
                background-color: #6c757d;
            }
            QPushButton#ResetButton:hover {
                background-color: #5a6268;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QScrollArea {
                background-color: #f9f9f9;
            }
            QFrame {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
                margin: 5px;
            }
        """)

        # Ana düzen
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Girdi düzeni
        input_layout = QGridLayout()
        input_layout.setSpacing(10)

        # Taş Çeşidi
        stone_label = QLabel('Stone Type')
        self.stone_input = QLineEdit()
        self.stone_input.setPlaceholderText('Enter or select stone type')
        self.stone_dropdown = QComboBox()
        self.stone_dropdown.setEditable(True)
        self.stone_dropdown.addItems(sorted(df['Stone Type'].unique()))
        self.stone_dropdown.setInsertPolicy(QComboBox.NoInsert)
        self.stone_dropdown.setCurrentText('Select Stone Type')
        self.stone_dropdown.currentTextChanged.connect(self.stone_dropdown_changed)

        # Ürün
        product_label = QLabel('Product')
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText('Enter or select product')
        self.product_dropdown = QComboBox()
        self.product_dropdown.setEditable(True)
        self.product_dropdown.addItems(sorted(df['Product'].unique()))
        self.product_dropdown.setInsertPolicy(QComboBox.NoInsert)
        self.product_dropdown.setCurrentText('Select Product')
        self.product_dropdown.currentTextChanged.connect(self.product_dropdown_changed)

        # Özellik
        feature_label = QLabel('Feature')
        self.feature_input = QLineEdit()
        self.feature_input.setPlaceholderText('Enter or select feature')
        self.feature_dropdown = QComboBox()
        self.feature_dropdown.setEditable(True)
        self.feature_dropdown.addItems(sorted(df['Feature'].unique()))
        self.feature_dropdown.setInsertPolicy(QComboBox.NoInsert)
        self.feature_dropdown.setCurrentText('Select Feature')
        self.feature_dropdown.currentTextChanged.connect(self.feature_dropdown_changed)

        # Arama Butonu
        search_button = QPushButton('Search')
        search_button.setIcon(QIcon('icons/search.png'))
        search_button.setIconSize(QSize(16, 16))
        search_button.clicked.connect(self.search)

        # Reset Butonu
        reset_button = QPushButton('Reset')
        reset_button.setObjectName('ResetButton')
        reset_button.setIcon(QIcon('icons/reset.png'))
        reset_button.setIconSize(QSize(16, 16))
        reset_button.clicked.connect(self.reset_fields)

        # Girdi düzenine widget'ları ekleme
        input_layout.addWidget(stone_label, 0, 0)
        input_layout.addWidget(self.stone_input, 1, 0)
        input_layout.addWidget(self.stone_dropdown, 2, 0)

        input_layout.addWidget(product_label, 0, 1)
        input_layout.addWidget(self.product_input, 1, 1)
        input_layout.addWidget(self.product_dropdown, 2, 1)

        input_layout.addWidget(feature_label, 0, 2)
        input_layout.addWidget(self.feature_input, 1, 2)
        input_layout.addWidget(self.feature_dropdown, 2, 2)

        # Butonları ekleme
        button_layout = QHBoxLayout()
        button_layout.addWidget(search_button)
        button_layout.addWidget(reset_button)
        input_layout.addLayout(button_layout, 1, 3)

        # Sonuç alanı
        self.results_widget = QWidget()
        self.results_layout = QGridLayout()
        self.results_layout.setSpacing(20)
        self.results_widget.setLayout(self.results_layout)

        self.results_area = QScrollArea()
        self.results_area.setWidgetResizable(True)
        self.results_area.setWidget(self.results_widget)

        # Düzenleri ana düzene ekleme
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.results_area)

        self.setLayout(main_layout)
    
    def stone_dropdown_changed(self, text):
        if text != "Select Stone Type":
            self.stone_input.setText(text)
        else:
            self.stone_input.clear()
    
    def product_dropdown_changed(self, text):
        if text != "Select Product":
            self.product_input.setText(text)
        else:
            self.product_input.clear()
    
    def feature_dropdown_changed(self, text):
        if text != "Select Feature":
            self.feature_input.setText(text)
        else:
            self.feature_input.clear()
    
    def search(self):
        # Önceki sonuçları temizleme
        for i in reversed(range(self.results_layout.count())):
            widget = self.results_layout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Girdi değerlerini alma
        stone = self.stone_input.text()
        product = self.product_input.text()
        feature = self.feature_input.text()

        # Verileri filtreleme
        result_df = self.filter_products(stone_type=stone, product=product, feature=feature)

        if not result_df.empty:
            row = 0
            col = 0
            for index, row_data in result_df.iterrows():
                # Her ürün için bir çerçeve oluşturma
                product_frame = QFrame()
                product_layout = QVBoxLayout()
                product_frame.setLayout(product_layout)
                product_frame.setFixedWidth(220)
                product_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

                # Görseli gösterme
                pixmap = QPixmap(row_data['Image'])
                pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label = QLabel()
                img_label.setPixmap(pixmap)
                img_label.setAlignment(Qt.AlignCenter)
                img_label.setCursor(Qt.PointingHandCursor)
                img_label.mousePressEvent = lambda event, image_path=row_data['Image']: self.open_image_viewer(image_path)
                product_layout.addWidget(img_label)

                # Ürün adını gösterme
                product_name_label = QLabel(row_data['Product Name'])
                product_name_label.setStyleSheet("font-weight: bold; font-size: 12px; color: #333;")
                product_name_label.setAlignment(Qt.AlignCenter)
                product_layout.addWidget(product_name_label)

                # Ek ürün bilgilerini gösterme
                product_info_label = QLabel(f"{row_data['Stone Type']} | {row_data['Product']} | {row_data['Feature']}")
                product_info_label.setStyleSheet("color: #555; font-size: 10px;")
                product_info_label.setAlignment(Qt.AlignCenter)
                product_layout.addWidget(product_info_label)

                # Ürün çerçevesini grid'e ekleme
                self.results_layout.addWidget(product_frame, row, col)
                col += 1
                if col > 3:
                    col = 0
                    row += 1
        else:
            no_results_label = QLabel("No products found matching the criteria.")
            no_results_label.setStyleSheet("color: #333;")
            self.results_layout.addWidget(no_results_label)
    
    def reset_fields(self):
        # Girdi alanlarını temizleme
        self.stone_input.clear()
        self.product_input.clear()
        self.feature_input.clear()
        
        # Dropdownları sıfırlama
        self.stone_dropdown.setCurrentText('Select Stone Type')
        self.product_dropdown.setCurrentText('Select Product')
        self.feature_dropdown.setCurrentText('Select Feature')
        
        # Sonuç alanını temizleme
        for i in reversed(range(self.results_layout.count())):
            widget = self.results_layout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
    
    def filter_products(self, stone_type=None, product=None, feature=None):
        filtered_df = self.data.copy()
        
        if stone_type:
            filtered_df = filtered_df[filtered_df['Stone Type'].str.contains(stone_type, case=False, na=False)]
        if product:
            filtered_df = filtered_df[filtered_df['Product'].str.contains(product, case=False, na=False)]
        if feature:
            filtered_df = filtered_df[filtered_df['Feature'].str.contains(feature, case=False, na=False)]
        
        return filtered_df

    def open_image_viewer(self, image_path):
        viewer = ImageViewer(image_path)
        viewer.exec_()

class ImageViewer(QDialog):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.image_path = image_path
        self.is_fullscreen = True  # Pencerenin tam ekran durumunu takip etmek için
        self.initUI()
        self.showFullScreen()  # Pencereyi tam ekran olarak aç

    def initUI(self):
        layout = QVBoxLayout()
        self.graphicsView = QGraphicsView()
        self.scene = QGraphicsScene()
        self.pixmap = QPixmap(self.image_path)
        self.pixmap_item = self.scene.addPixmap(self.pixmap)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
        self.setMinimumSize(800, 600)

        # Zoom özellikleri için
        self._zoom = 0
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == event.Wheel and source is self.graphicsView.viewport():
            if event.angleDelta().y() > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            return True
        return super().eventFilter(source, event)

    def zoom_in(self):
        self._zoom += 1
        self.graphicsView.scale(1.25, 1.25)

    def zoom_out(self):
        if self._zoom > 0:
            self._zoom -= 1
            self.graphicsView.scale(0.8, 0.8)

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.showNormal()
            self.is_fullscreen = False
        else:
            self.showFullScreen()
            self.is_fullscreen = True

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            self.toggle_fullscreen()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def mouseDoubleClickEvent(self, event):
        self.toggle_fullscreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = JewelryFilterApp()
    ex.show()
    sys.exit(app.exec_())
