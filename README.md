PyQt5 Jewelry Product Filter

## Project Description

This project is a desktop application developed using Python and the PyQt5 library. It provides a graphical user interface (GUI) to filter and view jewelry products listed in a `products.csv` file. Users can search for products based on criteria such as stone type, product category, and specific features, and then view the images and basic information of the matching items.

## Purpose and Workflow

**Purpose:** To provide an easy way for users to find specific jewelry products within a potentially large collection, primarily through a visually-oriented search experience that allows for quick browsing of product images.

**Workflow:**

1.  **Data Loading:** Upon starting, the application loads the `products.csv` file into a Pandas DataFrame. This file is expected to contain columns like 'Stone Type', 'Product', 'Feature', 'Product Name', and 'Image' (containing the file path to the product image).
2.  **Interface:** The GUI presents the user with the following filtering options:
    *   **Stone Type:** Offers both a text input field and a dropdown list populated with unique stone types from the dataset.
    *   **Product:** Offers both a text input field and a dropdown list populated with unique product categories.
    *   **Feature:** Offers both a text input field and a dropdown list populated with unique features.
    *   Selecting an item from a dropdown list automatically fills the corresponding text input field.
3.  **Filtering:** When the "Search" button is clicked, the application takes the text from the input fields and filters the DataFrame. The filtering is *case-insensitive* and uses *partial matching* (`str.contains`) on the respective columns ('Stone Type', 'Product', 'Feature').
4.  **Results Display:** The filtered products are displayed in a grid layout within a scrollable area at the bottom. For each product, the following are shown:
    *   Product image (clickable)
    *   Product Name
    *   Basic info string: "Stone Type | Product | Feature"
5.  **Image Viewer:** Clicking on a product image opens a dedicated image viewer window (initially fullscreen, but adjustable). This viewer allows users to see the image in more detail, supporting zooming with the mouse wheel and panning by dragging. Pressing F11 toggles fullscreen mode, and Esc closes the viewer.
6.  **Reset:** The "Reset" button clears all filter input fields and removes any currently displayed results from the scroll area.

## Project Requirements

*   Python 3.x
*   Pandas Library (`pip install pandas`)
*   PyQt5 Library (`pip install PyQt5`)
*   A `products.csv` file located in the same directory as the script (or with its path correctly specified). This file must contain at least the columns: `Stone Type`, `Product`, `Feature`, `Product Name`, `Image`. The `Image` column must contain valid file paths (relative or absolute) to the product images.
*   An `icons` folder in the same directory, containing `app_icon.png`, `search.png`, and `reset.png`.
*   The actual product image files accessible at the paths specified in the `products.csv` file.

## Usage

1.  Install the required libraries: `pip install pandas PyQt5`.
2.  Prepare your `products.csv` file and ensure all product images exist at the specified paths.
3.  Make sure the `icons` folder with the necessary `.png` files is present in the same directory as the script.
4.  Run the Python script: `python your_script_name.py` (replace `your_script_name.py` with the actual filename).

## To-Do / Potential Improvements

*   **Error Handling:**
    *   Gracefully handle cases where `products.csv` is missing or cannot be read.
    *   Display a placeholder image or error message if an image file specified in the CSV is not found.
    *   Provide more informative errors if the CSV format is incorrect (e.g., missing columns).
*   **Advanced Filtering/Sorting:**
    *   Add more filters (e.g., price range, material, brand).
    *   Implement an "exact match" option for filters.
    *   Add functionality to sort the results (by name, price, etc.).
*   **Performance:**
    *   For very large datasets (thousands of products), implement pagination or lazy loading of results to improve performance and reduce initial load time.
*   **Database Integration:**
    *   Replace the CSV file with an SQLite database or another database system for better scalability and data management.
*   **UI/UX Enhancements:**
    *   Apply a more modern theme or custom styling.
    *   Improve the responsiveness of UI elements to window resizing.
    *   Dynamically update dropdown options based on other active filters.
*   **Additional Features:**
    *   Implement a "favorites" system to save specific products.
    *   Create a dedicated product detail view/page showing more information and a larger image.
    *   Add an option to export search results (e.g., to CSV or Excel).
*   **Packaging:**
    *   Bundle the application into a standalone executable using tools like `PyInstaller` or `cx_Freeze` for easier distribution.
*   **Testing:**
    *   Add unit tests to verify the filtering logic and UI interactions under different scenarios.

---
Türkçe Açıklama 

PyQt5 Jewelry Product Filter (Mücevher Ürün Filtreleme Uygulaması)

## Proje Açıklaması

Bu proje, `products.csv` dosyasında listelenen mücevher ürünlerini görsel bir arayüz üzerinden filtrelemeye ve görüntülemeye olanak tanıyan bir masaüstü uygulamasıdır. Python programlama dili ve PyQt5 kütüphanesi kullanılarak geliştirilmiştir. Kullanıcılar, taş tipi, ürün kategorisi ve özellik gibi kriterlere göre arama yapabilir ve eşleşen ürünlerin görsellerini ve temel bilgilerini görüntüleyebilirler.

## Programın Amacı ve İşleyişi

**Amaç:** Kullanıcıların geniş bir mücevher koleksiyonu içinde aradıkları belirli ürünleri kolayca bulmalarını sağlamak. Özellikle görsel odaklı bir arama deneyimi sunarak, ürünleri hızlıca inceleme imkanı tanır.

**İşleyiş:**

1.  **Veri Yükleme:** Uygulama başladığında, `products.csv` dosyasını Pandas DataFrame olarak yükler. Bu dosya, her bir ürün için 'Stone Type', 'Product', 'Feature', 'Product Name' ve 'Image' (görsel dosya yolu) gibi sütunları içermelidir.
2.  **Arayüz:** Kullanıcıya şu filtreleme seçeneklerini sunar:
    *   **Taş Tipi (Stone Type):** Hem metin girişi hem de mevcut taş tiplerini içeren bir açılır liste sunar.
    *   **Ürün (Product):** Hem metin girişi hem de mevcut ürün kategorilerini içeren bir açılır liste sunar.
    *   **Özellik (Feature):** Hem metin girişi hem de mevcut özellikleri içeren bir açılır liste sunar.
    *   Açılır listelerden yapılan seçimler, ilgili metin giriş alanlarını otomatik olarak doldurur.
3.  **Filtreleme:** "Search" (Ara) butonuna tıklandığında, girilen metinleri alır ve DataFrame üzerinde ilgili sütunlarda *büyük/küçük harf duyarsız* ve *kısmi eşleşme* yaparak filtreleme gerçekleştirir (`str.contains`).
4.  **Sonuç Gösterimi:** Filtrelenen ürünler, alt kısımdaki kaydırılabilir alanda (ScrollArea) bir grid düzeninde gösterilir. Her ürün için:
    *   Ürün görseli (tıklanabilir)
    *   Ürün Adı
    *   Taş Tipi | Ürün | Özellik bilgisi
5.  **Görsel Görüntüleyici:** Bir ürün görseline tıklandığında, görseli daha büyük ve detaylı incelemek için tam ekran (veya ayarlanabilir boyutta) bir pencere açılır. Bu pencerede fare tekerleği ile yakınlaştırma/uzaklaştırma ve sürükleyerek gezinme (pan) yapılabilir. F11 ile tam ekran modu açılıp kapatılabilir, Esc ile kapatılabilir.
6.  **Sıfırlama:** "Reset" (Sıfırla) butonu, tüm filtre alanlarını temizler ve sonuç alanını boşaltır.

## Projenin Gereksinimleri

*   Python 3.x
*   Pandas Kütüphanesi (`pip install pandas`)
*   PyQt5 Kütüphanesi (`pip install PyQt5`)
*   `products.csv` dosyası (uygulama ile aynı dizinde veya doğru yolda belirtilmiş olmalı). Bu dosya en az şu sütunları içermelidir: `Stone Type`, `Product`, `Feature`, `Product Name`, `Image`. `Image` sütunu, ürün görsellerinin dosya yollarını içermelidir (göreceli veya mutlak olabilir).
*   `icons` klasörü (uygulama ile aynı dizinde) içinde `app_icon.png`, `search.png`, `reset.png` ikon dosyaları.
*   CSV dosyasında belirtilen yollarda bulunan ürün görselleri.

## Kullanım

1.  Gerekli kütüphaneleri kurun (`pip install pandas PyQt5`).
2.  `products.csv` dosyasını ve ürün görsellerini hazırlayın. Görsel yollarının CSV dosyasında doğru olduğundan emin olun.
3.  `icons` klasörünü ve içindeki ikonları temin edin.
4.  Python betiğini çalıştırın: `python your_script_name.py`

## Yapılması Gerekenler ve Olası Geliştirmeler (To-Do / Improvements)

*   **Hata Yönetimi:**
    *   `products.csv` dosyası bulunamazsa veya okunamzsa kullanıcıya bilgi ver.
    *   CSV içinde belirtilen görsel dosyaları bulunamazsa varsayılan bir görsel göster veya hata mesajı ver.
    *   CSV formatı bozuksa (eksik sütun vb.) daha açıklayıcı hatalar ver.
*   **Daha Gelişmiş Filtreleme/Sıralama:**
    *   Fiyat aralığı, materyal, marka gibi ek filtreler ekle.
    *   "Tam eşleşme" seçeneği ekle.
    *   Sonuçları fiyata, isme vb. göre sıralama özelliği ekle.
*   **Performans:**
    *   Çok fazla ürün varsa (binlerce), sonuçları sayfalandırma (pagination) veya "lazy loading" (kaydırdıkça yükleme) ile göstererek performansı artır.
*   **Veritabanı Entegrasyonu:** CSV yerine SQLite veya başka bir veritabanı kullanarak daha ölçeklenebilir ve yönetilebilir bir yapı oluştur.
*   **UI/UX İyileştirmeleri:**
    *   Daha modern bir tema veya stil uygulama.
    *   Arayüz elemanlarının yeniden boyutlandırılmaya daha duyarlı hale getirilmesi.
    *   Filtre seçeneklerini dinamik olarak (mevcut sonuçlara göre) güncelleme.
*   **Ek Özellikler:**
    *   Seçili ürünleri favorilere ekleme.
    *   Ürün detay sayfası (daha fazla bilgi ve daha büyük görselle).
    *   Sonuçları dışa aktarma (CSV, Excel vb.).
*   **Paketleme:** Uygulamayı `PyInstaller` veya `cx_Freeze` gibi araçlarla tek başına çalıştırılabilir bir `.exe` dosyası haline getirme.
*   **Testler:** Uygulamanın farklı senaryolarda doğru çalıştığını doğrulamak için birim testleri (unit tests) ekleme.

---
