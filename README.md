# VALLEX GUI Launcher

VALL-E-X ベースの日本語対応 音声合成アプリケーションです。  
Windows環境向けにGUIと自動仮想環境構築バッチによって、誰でも簡単に使える形で提供しています。

**Gitがインストールされている環境を想定しています。**

## 🔧 特徴

- [VALL-E-X](https://github.com/Plachtaa/VALL-E-X) をベースとしたゼロショット音声合成
- Tkinterによるインターフェース
- Python本体と仮想環境を含めて配布可能（インストール不要）
- `installer.bat` 実行で仮想環境作成と依存ライブラリの導入が完了


## 📦 セットアップ手順

1. このリポジトリをクローン、またはZipでダウンロードして展開
2. `installer.bat` をダブルクリック  
   - Python仮想環境 (`valle_env/`) が作成され、依存ライブラリが自動でインストールされます
3. `run.bat` でGUIアプリを起動

## 📁 フォルダ構成

VALLEX_Distributable\
 ├─ Python310\
 │   └─ # 通常版Python（パス未設定） 
 ├─ valle_env\
 │   └─ # 仮想環境（初回setupで自動生成） 
 ├─ VALLEX\
 │   └─ VALL-E-X本体及びGUIスクリプト 
 ├─ installer.bat # セットアップバッチ 
 ├─ run.bat # GUI起動バッチ 
 └─ README.md

## 💬 使用技術

- Python 3.10
- [VALL-E-X](https://github.com/Plachtaa/VALL-E-X) (MIT License)
- Tkinter
- PyTorch / torchaudio

## ⚖️ ライセンス

このプロジェクトは [MIT License](./LICENSE) の下で公開されています。  
VALL-E-X本体およびその著作権は Microsoft および [Plachtaa/VALL-E-X](https://github.com/Plachtaa/VALL-E-X) に帰属します。


This project includes an official CPython distribution (Python 3.10.x),
which is licensed under the Python Software Foundation License Version 2.  
See [https://docs.python.org/3/license.html](https://docs.python.org/3/license.html) for details.

© 2001-2024 Python Software Foundation. All Rights Reserved.
