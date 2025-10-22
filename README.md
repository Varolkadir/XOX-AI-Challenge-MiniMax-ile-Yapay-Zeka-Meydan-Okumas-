# ⚔️ XOX-AI-Challenge: MiniMax ile Yapay Zeka Meydan Okuması

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)]()
[![Pygame Library](https://img.shields.io/badge/Library-Pygame-FF1493?style=flat&logo=pygame&logoColor=white)]()
[![AI Algorithm](https://img.shields.io/badge/Challenge-Impossible_to_Win-red?style=flat)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

## 🇹🇷 Türkçe Açıklama

Bu proje, klasik Tic-Tac-Toe (XOX) oyununun Pygame tabanlı görsel arayüzü ile geliştirilmiş bir uygulamasıdır. Arka planda çalışan **MiniMax algoritması**, yapay zekayı (AI) yenilmez kılar; AI ya kazanır ya da berabere kalır. Amacımız, bu AI'a karşı ne kadar dayanabileceğinizi test etmek ve MiniMax'ın karar verme gücünü deneyimlemenizi sağlamaktır.

### 🎯 Meydan Okumanın Temeli

Oyun, kullanıcının "X" veya "O" seçimiyle başlar. AI, her hamlesinde oyun ağacındaki binlerce olasılığı hesaplayarak, sizin kazanmanızı engelleyecek en optimal hamleyi yapar.

### ✨ Ana Özellikler ve Teknik Yapı

| Kategori | Özellik | Odak Noktası |
| :--- | :--- | :--- |
| **Oynanış** | **Yenilmez Yapay Zeka** | MiniMax Çözücü, AI'ın asla kaybetmemesini garantiler. (`ajan.py`) |
| **Arayüz** | **Pygame Tabanlı UI** | Akıcı ve kolay anlaşılır görsel arayüzde hamleleri takip etme. (`main.py`) |
| **Karar Verme** | **Modüler Mantık** | Oyun kuralları (`terminal`, `winner`) ve hamle hesaplama (`minimax`) net bir şekilde ayrılmıştır. |
| **Seçim** | **Dinamik Rol Seçimi** | Kullanıcı, oyuna 'X' (ilk başlayan) veya 'O' olarak başlayabilir. |

### 🚀 Kurulum ve Başlatma

Yapay zekaya karşı mücadeleye başlamak için bu adımları takip edin.

1.  **Klonlama:** Projeyi yerel makinenize indirin:
    ```bash
    git clone [https://github.com/](https://github.com/)[KullanıcıAdınız]/XOX-AI-Challenge.git
    cd XOX-AI-Challenge
    ```

2.  **Bağımlılık Yükleme:** Pygame kütüphanesini yükleyin:
    ```bash
    pip install pygame
    ```

3.  **Oyunu Başlatma:** Ana uygulamayı çalıştırın:
    ```bash
    python main.py
    ```

### ⚙️ Kod Yapısı: AI ve Oyun Mantığı

Proje, oyunun mantığını ve arayüzünü ayırarak temiz bir mimari sunar.

* **1. `ajan.py` (MiniMax Motoru):** `initial_state()`, `player(board)`, `actions(board)`, `terminal(board)`, `utility(board)` ve **`minimax(board)`** gibi AI'ın karar verme fonksiyonlarını içerir.
* **2. `main.py` (Pygame Arayüzü):** Oyun penceresini, menüleri yönetir ve kullanıcı ile AI hamlelerinin görselleştirilmesinden sorumludur.

---
---

## 🇬🇧 English Description

This project is an application of the classic Tic-Tac-Toe (XOX) game, developed with a Pygame-based graphical interface. The **MiniMax algorithm**, running in the background, renders the artificial intelligence (AI) unbeatable; the AI either wins or draws. Our goal is to test your endurance against this AI and let you experience the decision-making power of MiniMax.

### 🎯 The Core of the Challenge

The game starts with the user selecting "X" or "O". For every move, the AI calculates thousands of possibilities in the game tree, making the most optimal move to prevent you from winning.

### ✨ Key Features and Technical Structure

| Category | Feature | Focus Point |
| :--- | :--- | :--- |
| **Gameplay** | **Unbeatable AI** | The MiniMax Solver guarantees the AI will never lose. (`ajan.py`) |
| **Interface** | **Pygame-based UI** | Follow the moves on a fluid and easy-to-understand graphical interface. (`main.py`) |
| **Decision** | **Modular Logic** | Game rules (`terminal`, `winner`) and move calculation (`minimax`) are clearly separated. |
| **Selection** | **Dynamic Role Selection** | The user can choose to start the game as 'X' (first player) or 'O'. |

### 🚀 Setup and Running

Follow these steps to start your battle against the artificial intelligence.

1.  **Cloning:** Clone the project to your local machine:
    ```bash
    git clone [https://github.com/](https://github.com/)[YourUsername]/XOX-AI-Challenge.git
    cd XOX-AI-Challenge
    ```

2.  **Dependency Installation:** Install the required Pygame library:
    ```bash
    pip install pygame
    ```

3.  **Launching the Game:** Run the main application:
    ```bash
    python main.py
    ```

### ⚙️ Code Structure: AI and Game Logic

The project provides a clean architecture by separating the game logic and the interface.

* **1. `ajan.py` (MiniMax Engine):** Contains the AI decision functions like `initial_state()`, `player(board)`, `actions(board)`, `terminal(board)`, `utility(board)`, and the core **`minimax(board)`**.
* **2. `main.py` (Pygame Interface):** Manages the game window, menus, and is responsible for the visualization of user and AI moves.

---

## 📞 İletişim / Contact

* **Geliştirici / Developer:** \[Adınız Soyadınız]
* **GitHub Profil / Profile:** \[GitHub Profil Linkiniz]
* **Lisans / License:** This project is released under the [Lisans Türü - Örn: MIT] License.
